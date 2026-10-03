#!/usr/bin/env bash
# Ortam yetenek raporu. Her oturum başında çalıştır: bash scripts/env_check.sh
# Çıktı: reports/env/<UTC tarih>.md  (ayrıca stdout). Sır/ token içeriği yazmaz.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT/reports/env"; mkdir -p "$OUT_DIR"
TS="$(date -u +%Y-%m-%dT%H%M%SZ)"; OUT="$OUT_DIR/$TS.md"

have() { command -v "$1" >/dev/null 2>&1 && echo "$(command -v "$1")" || echo "MISSING"; }
probe() { curl -sS -o /dev/null -w "%{http_code}" --max-time 12 -L "$1" 2>/dev/null || echo "000"; }

{
echo "# Environment check — $TS"
echo
echo "## Host"
echo "- OS: $(. /etc/os-release 2>/dev/null; echo "${PRETTY_NAME:-unknown}")"
echo "- Kernel: $(uname -r)"
echo "- CPU: $(nproc) vCPU"
echo "- RAM: $(free -h | awk '/Mem:/{print $2" total, "$7" available"}')"
echo "- Disk (repo fs): $(df -h "$ROOT" | awk 'NR==2{print $4" avail of "$2}')"
echo "- Writable dir sanity: $(touch "$ROOT/.envcheck.tmp" 2>/dev/null && rm -f "$ROOT/.envcheck.tmp" && echo ok || echo FAIL)"
echo
echo "## Tools"
for t in python3 uv pip3 node npm ffmpeg ffprobe convert espeak-ng fc-list git gh docker; do
  printf -- "- %-10s %s\n" "$t" "$(have "$t")"
done
echo "- python3 version: $(python3 --version 2>&1)"
echo "- node version: $(node --version 2>&1)"
echo "- ffmpeg: $(ffmpeg -version 2>/dev/null | head -1)"
echo "- ffmpeg encoders: $(ffmpeg -hide_banner -encoders 2>/dev/null | grep -oE 'libx264|aac|libopus|libvpx-vp9' | sort -u | tr '\n' ' ')"
echo "- ffmpeg filters: $(ffmpeg -hide_banner -filters 2>/dev/null | awk '{print $2}' | grep -xE 'drawtext|subtitles|ass|xfade|zoompan|loudnorm|blackdetect|silencedetect' | sort -u | tr '\n' ' ')"
echo "- playwright browsers dir: ${PLAYWRIGHT_BROWSERS_PATH:-unset} → $(ls "${PLAYWRIGHT_BROWSERS_PATH:-/nonexistent}" 2>/dev/null | tr '\n' ' ')"
echo "- fonts (families, first 12): $(fc-list : family 2>/dev/null | sort -u | head -12 | tr '\n' ';')"
echo
echo "## Network reachability (HTTP code; 000 = blocked/unreachable)"
for u in \
  https://pypi.org/simple/ \
  https://registry.npmjs.org/ \
  http://archive.ubuntu.com/ubuntu/dists/noble/Release \
  https://github.com/ \
  https://raw.githubusercontent.com/rhasspy/piper/master/README.md \
  https://api.github.com/ \
  https://support.google.com/youtube/answer/72851 \
  https://www.youtube.com/ \
  https://huggingface.co/ \
  https://docs.github.com/ \
  https://en.wikipedia.org/ \
  https://fonts.google.com/ ; do
  printf -- "- %-70s %s\n" "$u" "$(probe "$u")"
done
echo
echo "## Proxy status (if present)"
if [ -n "${HTTPS_PROXY:-}" ]; then
  curl -sS --max-time 5 "$HTTPS_PROXY/__agentproxy/status" 2>/dev/null | python3 -c 'import sys,json
try:
  d=json.load(sys.stdin); fails=d.get("recentRelayFailures",[])
  hosts=sorted({f.get("host","?") for f in fails})
  print("- recent denied hosts:", ", ".join(hosts) if hosts else "(none recorded)")
except Exception as e: print("- proxy status unavailable:", e)'
else
  echo "- HTTPS_PROXY not set"
fi
echo
echo "## Git"
echo "- branch: $(git -C "$ROOT" rev-parse --abbrev-ref HEAD 2>/dev/null || echo none)"
echo "- head: $(git -C "$ROOT" log -1 --format='%h %s' 2>/dev/null || echo 'no commits')"
echo "- remote: $(git -C "$ROOT" remote get-url origin 2>/dev/null || echo none)"
} | tee "$OUT"

echo
echo "written: $OUT"
