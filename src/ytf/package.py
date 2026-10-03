from __future__ import annotations
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
import yaml

from . import paths
from .jobs import sha256_file, write_json
from .models import Episode
from .tts import Timeline


def _chapters(ep: Episode, tl: Timeline) -> list[tuple[str, str]]:
    out = []
    for sc, st in zip(ep.scenes, tl.scenes):
        title = sc.params.get("chapter") or sc.params.get("title")
        if title and (not out or st.start - 0 >= 10):
            m, s = divmod(int(st.start), 60)
            out.append((f"{m:02d}:{s:02d}", str(title).replace("**", "")))
    if out and out[0][0] != "00:00":
        out.insert(0, ("00:00", "Intro"))
    return out


def description_text(ep: Episode, tl: Timeline, fmt: str) -> str:
    L = [ep.description.strip(), ""]
    if fmt == "long" and len(_chapters(ep, tl)) >= 3:
        L += ["Chapters:"] + [f"{t} {n}" for t, n in _chapters(ep, tl)] + [""]
    L += ["Sources and data:"] + [f"- {s.name}{(' — ' + s.url) if s.url else ''}{(' (' + s.license + ')') if s.license else ''}" for s in ep.sources]
    L += ["", "Transparency: narration is a synthetic voice (Kokoro-82M, Apache-2.0). All charts are generated from the cited data; "
          "no stock footage. Code and sources: github.com/brsctncnbrk7-byte/Claude-code-YouTube-"]
    if ep.tags:
        L += ["", " ".join("#" + t.replace(" ", "") for t in ep.tags[:6])]
    return "\n".join(L)


def make_package(ep: Episode, fmt: str, bdir: Path, final: Path, tl: Timeline, qc: dict, thumbs: list[Path]) -> Path:
    d = paths.dist_dir(ep.id) if fmt == "long" else paths.dist_dir(ep.id) / "short"
    d.mkdir(parents=True, exist_ok=True)
    files = {}
    files["video"] = shutil.copy(final, d / f"{ep.id}{'' if fmt == 'long' else '-short'}.mp4")
    files["srt"] = shutil.copy(bdir / f"{ep.id}.srt", d / f"{ep.id}{'' if fmt == 'long' else '-short'}.en.srt")
    files["vtt"] = shutil.copy(bdir / f"{ep.id}.vtt", d / f"{ep.id}{'' if fmt == 'long' else '-short'}.en.vtt")
    for t in thumbs:
        files[f"thumb_{t.stem[-1]}"] = shutil.copy(t, d / t.name)
    rep_src = paths.REPORTS / ep.id / fmt / "qc-report.md"
    if rep_src.exists():
        files["qc_report"] = shutil.copy(rep_src, d / f"qc-report{'' if fmt == 'long' else '-short'}.md")
    edir = paths.episode_dir(ep.id)
    for name in ("sources.md", "licenses.md"):
        if (edir / name).exists():
            files[name] = shutil.copy(edir / name, d / name)
    title = ep.title if fmt == "long" else (ep.short.title if ep.short else ep.title)
    meta = {
        "episode": ep.id, "format": fmt, "title": title, "description": description_text(ep, tl, fmt), "tags": ep.tags,
        "playlist": ep.playlist, "language": "en", "category": "Education", "visibility_on_upload": "scheduled",
        "publish_at_utc": ep.publish_at_utc, "audience_made_for_kids": ep.audience_made_for_kids,
        "altered_or_synthetic_content": ep.disclosure.altered_or_synthetic, "disclosure_rationale": ep.disclosure.rationale,
        "ad_suitability_note": ep.ad_suitability_note, "subtitles": "upload .srt as English",
        "thumbnail_chosen": thumbs[ep.thumbnail.chosen].name if thumbs else None, "chapters": _chapters(ep, tl) if fmt == "long" else [],
        "qc_status": qc.get("status"), "duration_seconds": round(tl.total, 2),
        "shorts_note": "Upload as a regular video; vertical ≤60 s is detected as a Short." if fmt == "short" else "",
    }
    (d / ("metadata.yaml" if fmt == "long" else "metadata-short.yaml")).write_text(yaml.safe_dump(meta, sort_keys=False, allow_unicode=True), encoding="utf-8")
    manifest = {"episode": ep.id, "format": fmt, "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "files": {Path(p).name: {"sha256": sha256_file(Path(p)), "bytes": Path(p).stat().st_size} for p in files.values()}}
    write_json(d / ("manifest.json" if fmt == "long" else "manifest-short.json"), manifest)
    checklist = f"""# Upload checklist — {ep.id} ({fmt})
1. YouTube Studio → Create → Upload videos → `{Path(files['video']).name}`
2. Title: `{title}`
3. Description: paste from `metadata{'-short' if fmt=='short' else ''}.yaml → description`
4. Thumbnail: `{meta['thumbnail_chosen']}` (long only) • Playlist: `{ep.playlist}`
5. Audience: {"Yes, made for kids" if ep.audience_made_for_kids else "No, it's not made for kids"} • Altered or synthetic content: {"Yes" if ep.disclosure.altered_or_synthetic else "No"} ({ep.disclosure.rationale})
6. Subtitles: upload `{Path(files['srt']).name}` (English) • Language: English • Category: Education
7. Visibility: Schedule → {ep.publish_at_utc or 'see content/publish-queue.yaml'} (UTC) → Save
8. After publishing: tell Claude the video URL (or that the upload is scheduled). Claude records the publish time in the repo; you never edit repo files.
"""
    (d / ("UPLOAD_CHECKLIST.md" if fmt == "long" else "UPLOAD_CHECKLIST-short.md")).write_text(checklist, encoding="utf-8")
    notes = f"# {title}\n\n{ep.thesis}\n\nQC: `{qc.get('status')}` • duration {tl.total:.1f}s • sha256 in manifest.\n"
    (d / ("RELEASE_NOTES.md" if fmt == "long" else "RELEASE_NOTES-short.md")).write_text(notes, encoding="utf-8")
    return d
