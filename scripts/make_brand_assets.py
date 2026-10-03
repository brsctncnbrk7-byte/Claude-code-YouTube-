#!/usr/bin/env python3
"""Generate channel brand assets (logo SVG, profile 800x800, banner 2560x1440, watermark 150x150) with Playwright. Free, deterministic."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "channel" / "assets"; OUT.mkdir(parents=True, exist_ok=True)
FONT = (ROOT / "assets/fonts/Inter-Variable.ttf").as_uri()
LOGO_SVG = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'>
<circle cx='100' cy='100' r='96' fill='#0B1020' stroke='#F2A93B' stroke-width='6'/>
<polyline points='40,140 70,118 95,126 125,84 160,60' fill='none' stroke='#5CC8FF' stroke-width='10' stroke-linecap='round' stroke-linejoin='round'/>
<circle cx='160' cy='60' r='12' fill='#F2A93B'/><circle cx='40' cy='140' r='7' fill='#F4F1EA'/>
<line x1='40' y1='156' x2='164' y2='156' stroke='#8A93A6' stroke-width='4' stroke-dasharray='6 8'/></svg>"""
(OUT / "logo.svg").write_text(LOGO_SVG)

TMP = ROOT / "build" / "_brand"; TMP.mkdir(parents=True, exist_ok=True)

def page_html(body, w, h, extra=""):
    return f"""<html><head><style>@font-face{{font-family:Inter;src:url('{FONT}') format('truetype');font-weight:100 900}}
    body{{margin:0;width:{w}px;height:{h}px;background:#0B1020;color:#F4F1EA;font-family:Inter,'DejaVu Sans',sans-serif;overflow:hidden;position:relative}}{extra}</style></head><body>{body}</body></html>"""

def open_html(b, html, w, h):
    f = TMP / f"page_{w}x{h}.html"; f.write_text(html)
    pg = b.new_page(viewport={"width": w, "height": h}); pg.goto(f.resolve().as_uri(), wait_until="load"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(300)
    return pg

with sync_playwright() as pw:
    b = pw.chromium.launch(); 
    # profile 800x800
    pg = open_html(b, page_html(f"<div style='position:absolute;inset:0;display:flex;align-items:center;justify-content:center'><div style='width:720px;height:720px'>{LOGO_SVG}</div></div>", 800, 800), 800, 800)
    pg.screenshot(path=str(OUT / "profile_800.png")); pg.close()
    # banner 2560x1440, safe area 1546x423 centered
    bars = "".join(f"<rect x='{200+i*62}' y='{1440-120-h}' width='40' height='{h}' fill='#5CC8FF' opacity='{0.08+0.012*i}'/>" for i, h in enumerate([80,120,95,160,210,180,260,300,270,340,390,360,420,470,450,520,560,540,600,650,630,700,740,720,780,820,800,860,900,880,940,980,960,1000,1040,1020]))
    body = f"""<svg style='position:absolute;inset:0' width='2560' height='1440'>{bars}</svg>
    <div style='position:absolute;left:440px;top:440px;width:1680px;height:560px;background:rgba(11,16,32,.82);border-radius:40px'></div>
    <div style='position:absolute;left:507px;top:508px;width:1546px;height:423px;display:flex;align-items:center;gap:40px'>
      <div style='width:300px;height:300px;flex:none'>{LOGO_SVG}</div>
      <div><div style='font-weight:800;font-size:150px;letter-spacing:-.03em;line-height:1'>Plotted Past</div>
      <div style='font-size:48px;color:#8A93A6;margin-top:18px'>Real mysteries solved by a chart — rebuilt from the original numbers</div></div></div>"""
    pg = open_html(b, page_html(body, 2560, 1440), 2560, 1440)
    pg.screenshot(path=str(OUT / "banner_2560x1440.png")); pg.close()
    b.close()
Image.open(OUT / "profile_800.png").resize((150, 150), Image.LANCZOS).save(OUT / "watermark_150.png")
Image.open(OUT / "banner_2560x1440.png").crop((507, 508, 507 + 1546, 508 + 423)).save(OUT / "banner_safe_area_preview.png")
print("brand assets:", sorted(p.name for p in OUT.iterdir()))
