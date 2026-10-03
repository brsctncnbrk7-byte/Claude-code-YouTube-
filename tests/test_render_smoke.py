"""End-to-end mini render: 1 title scene, ~1 s, real Chromium + ffmpeg. Skips if Chromium unavailable."""
import json
import shutil
import subprocess
import pytest
from ytf.models import Episode, Scene
from ytf.render import render_video
from ytf.tts import SceneTiming, Timeline


@pytest.mark.skipif(shutil.which("ffmpeg") is None, reason="ffmpeg missing")
def test_mini_render(tmp_path):
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except Exception:
        pytest.skip("playwright missing")
    ep = Episode(id="ep-test", title="Smoke", scenes=[Scene(id="t", kind="title", narration="x", shows="smoke", params={"title": "Smoke **Test**", "subtitle": "ok"})])
    tl = Timeline([SceneTiming("t", 0.0, 1.0, [])], 1.0)
    try:
        video = render_video(ep, ep.scenes, tl, "long", tmp_path, workers=1)
    except Exception as e:  # browser not installed in CI without playwright install
        if "Executable doesn't exist" in str(e):
            pytest.skip("chromium not installed")
        raise
    info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", str(video)], capture_output=True, text=True).stdout)
    v = info["streams"][0]
    assert v["width"] == 1920 and v["height"] == 1080 and v["codec_name"] == "h264"
    assert int(v["nb_frames"]) == 30
    stats = json.loads((tmp_path / "render_stats.json").read_text())
    assert stats["scenes"][0]["overflow"] == []
