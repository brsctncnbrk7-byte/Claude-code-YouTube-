#!/usr/bin/env bash
# Renders the first episode with status `scripted` in content/queue.yaml (for VPS cron or manual use). No Claude session needed.
# Does NOT change queue status (that is a Claude-session judgement after QC review). Writes logs/render_queue.log.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p logs
EP=$(uv run python -c "import yaml;q=yaml.safe_load(open('content/queue.yaml'));print(next((e['id'] for e in q['episodes'] if e['status']=='scripted'),''))")
if [ -z "$EP" ]; then echo "$(date -u +%FT%TZ) nothing scripted" | tee -a logs/render_queue.log; exit 0; fi
echo "$(date -u +%FT%TZ) rendering $EP" | tee -a logs/render_queue.log
uv run ytf all "$EP" --workers 2 2>&1 | tee -a logs/render_queue.log
uv run ytf all "$EP" --format short --workers 2 2>&1 | tee -a logs/render_queue.log || echo "short failed (no short section?)" | tee -a logs/render_queue.log
echo "$(date -u +%FT%TZ) done $EP → dist/$EP" | tee -a logs/render_queue.log
