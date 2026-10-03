/* Plotted Past — deterministic scene renderer. renderFrame(sceneIndex, tSeconds[, thumb]) draws the state at time t. */
(function () {
  const E = window.EPISODE;
  const W = E.format.w, H = E.format.h, V = H > W;
  const stage = document.getElementById('stage');
  const fade = document.getElementById('fade');
  const thumb = document.getElementById('thumb');
  if (V) document.body.classList.add('vertical');
  const C = { bg: '#0B1020', paper: '#F4F1EA', amber: '#F2A93B', sky: '#5CC8FF', coral: '#FF6B6B', muted: '#8A93A6', grid: '#243049' };
  const SERIES = [C.sky, C.coral, C.amber, '#9BE564', '#C77DFF'];

  const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
  const ease = (x) => { x = clamp(x, 0, 1); return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
  const easeOut = (x) => { x = clamp(x, 0, 1); return 1 - Math.pow(1 - x, 3); };
  const prog = (t, s, d) => clamp((t - s) / Math.max(d, 1e-6), 0, 1);
  const fmt = (n, d = 0) => Number(n).toLocaleString('en-US', { maximumFractionDigits: d, minimumFractionDigits: d });
  const esc = (s) => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const rich = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<span class="hl">$1</span>');
  const rowsOf = (p) => { let rows = E.data[p.data] || []; if (p.filter) rows = rows.filter(r => eval(p.filter)); return rows; }; // filter is a trusted literal from episode.yaml

  function chartBox(p) {
    // chart drawing area in px
    const top = V ? H * 0.24 : H * 0.20, bottom = V ? H * 0.70 : H * 0.84;
    const left = W * (p && p.left_pad || 0.09), right = W * 0.95;
    return { x: left, y: top, w: right - left, h: bottom - top };
  }
  function linScale(d0, d1, r0, r1) { return (v) => r0 + (v - d0) / ((d1 - d0) || 1) * (r1 - r0); }
  function niceTicks(d0, d1, n = 5) {
    const span = d1 - d0 || 1, step0 = span / n, mag = Math.pow(10, Math.floor(Math.log10(step0)));
    const cands = [1, 2, 2.5, 5, 10].map(m => m * mag);
    const step = cands.find(s => span / s <= n) || cands[cands.length - 1];
    const out = []; for (let v = Math.ceil(d0 / step) * step; v <= d1 + 1e-9; v += step) out.push(+v.toFixed(10)); return out;
  }
  function axes(b, xs, ys, xt, yt, xlabel, ylabel, xfmt, yfmt) {
    let s = `<g class="axis">`;
    s += `<path d="M${b.x},${b.y + b.h}H${b.x + b.w}"/><path d="M${b.x},${b.y}V${b.y + b.h}"/>`;
    for (const v of yt) { const y = ys(v); s += `<line x1="${b.x}" x2="${b.x + b.w}" y1="${y}" y2="${y}" stroke-dasharray="4 8" opacity=".55"/><text x="${b.x - 14}" y="${y + 8}" text-anchor="end">${(yfmt || fmt)(v)}</text>`; }
    for (const v of xt) { const x = xs(v); s += `<text x="${x}" y="${b.y + b.h + 36}" text-anchor="middle">${(xfmt || fmt)(v)}</text>`; }
    if (xlabel) s += `<text x="${b.x + b.w / 2}" y="${b.y + b.h + 78}" text-anchor="middle" font-size="26" fill="${C.paper}">${esc(xlabel)}</text>`;
    if (ylabel) s += `<text transform="translate(${b.x - 96},${b.y + b.h / 2}) rotate(-90)" text-anchor="middle" font-size="26" fill="${C.paper}">${esc(ylabel)}</text>`;
    return s + `</g>`;
  }
  function header(sc, p) {
    let h = '';
    if (p.title) h += `<div class="chart-title">${rich(p.title)}</div>`;
    if (p.subtitle) h += `<div class="chart-sub">${rich(p.subtitle)}</div>`;
    return h;
  }
  function footer(sc, t, dur) {
    let h = '';
    if (sc.caption) h += `<div class="caption" style="opacity:${easeOut(prog(t, .4, .5))}">${rich(sc.caption)}</div>`;
    if (sc.source) h += `<div class="source">${esc(sc.source)}</div>`;
    return h;
  }
  const badge = () => `<div class="badge">${esc(E.brand.name)}</div>`;

  const K = {};
  K.title = (sc, t, d) => {
    const p = sc.params;
    return `<div class="title" style="opacity:${easeOut(prog(t, .2, .9))};transform:translateY(${(1 - easeOut(prog(t, .2, .9))) * 30}px)">${rich(p.title || E.title)}</div>
            <div class="subtitle" style="opacity:${easeOut(prog(t, 1.0, .9))}">${rich(p.subtitle || '')}</div>${badge()}`;
  };
  K.text = (sc, t, d) => {
    const p = sc.params; let big = '';
    if (p.number !== undefined) { const v = p.number * easeOut(prog(t, .3, 1.6)); big = `<div class="big num" style="color:${p.color || C.amber}">${p.prefix || ''}${fmt(v, p.decimals || 0)}${p.suffix || ''}</div>`; }
    return `<div class="card" style="opacity:${easeOut(prog(t, .1, .6))}">${big}<div class="head">${rich(p.headline || '')}</div><div class="sub">${rich(p.sub || '')}</div></div>${footer(sc, t, d)}`;
  };
  K.outro = (sc, t, d) => {
    const p = sc.params;
    return `<div class="card" style="opacity:${easeOut(prog(t, .1, .8))}"><div class="head">${rich(p.headline || E.brand.name)}</div><div class="sub">${rich(p.sub || 'Sources and data in the description.')}</div></div>${badge()}`;
  };

  // ---- bars (stacked, monthly) ----
  K.bars = (sc, t, d) => {
    const p = sc.params, rows = rowsOf(p), b = chartBox(p), keys = p.series, colors = p.colors || SERIES;
    const n = rows.length, reveal = p.reveal_seconds || Math.max(2, d - 2.5);
    const maxv = p.ymax || Math.max(...rows.map(r => keys.reduce((a, k) => a + (+r[k] || 0), 0)));
    const ys = linScale(0, maxv, b.y + b.h, b.y), bw = b.w / n;
    let s = `<svg width="${W}" height="${H}">` + axes(b, v => v, ys, [], niceTicks(0, maxv), '', p.ylabel);
    rows.forEach((r, i) => {
      const k = easeOut(prog(t, 0.3 + (i / n) * reveal, 0.6)); let y0 = b.y + b.h;
      keys.forEach((key, j) => { const v = (+r[key] || 0) * k, y1 = ys(v) - (b.y + b.h - y0); const hgt = (b.y + b.h) - ys(v); s += `<rect x="${b.x + i * bw + bw * .12}" y="${y0 - hgt}" width="${bw * .76}" height="${hgt}" fill="${colors[j]}" rx="3"/>`; y0 -= hgt; });
      if (p.xkey && (i % (p.xevery || 1) === 0)) s += `<text x="${b.x + i * bw + bw / 2}" y="${b.y + b.h + 34}" text-anchor="middle" fill="${C.muted}" font-size="20">${esc(r[p.xkey])}</text>`;
    });
    s += `</svg>` + legend(keys, colors, p.labels);
    return header(sc, p) + s + footer(sc, t, d);
  };
  function legend(keys, colors, labels) {
    return `<div class="legend">` + keys.map((k, j) => `<div>${esc((labels && labels[j]) || k)}<span class="sw" style="background:${colors[j]}"></span></div>`).join('') + `</div>`;
  }

  // ---- rose (Nightingale polar area) ----
  K.rose = (sc, t, d) => {
    const p = sc.params, rows = E.data[p.data].filter(r => !p.filter || eval(p.filter)); // filter is a trusted literal from episode.yaml
    const keys = p.series, colors = p.colors || [C.sky, C.coral, C.paper];
    const cx = W * (p.cx || (V ? .5 : .58)), cy = H * (p.cy || (V ? .47 : .54)), R = Math.min(W, H) * (p.radius || .36);
    const maxv = p.vmax || Math.max(...rows.map(r => Math.max(...keys.map(k => +r[k] || 0))));
    const n = rows.length, step = 2 * Math.PI / n, reveal = p.reveal_seconds || Math.max(2, d - 3);
    let s = `<svg width="${W}" height="${H}">`;
    for (let g = 1; g <= 4; g++) s += `<circle cx="${cx}" cy="${cy}" r="${R * g / 4}" fill="none" stroke="${C.grid}" stroke-width="1.5" stroke-dasharray="3 7"/>`;
    rows.forEach((r, i) => {
      const k = easeOut(prog(t, 0.3 + (i / n) * reveal, 0.7));
      const a0 = -Math.PI / 2 + i * step, a1 = a0 + step;
      const vals = keys.map((key, j) => ({ v: (+r[key] || 0) * k, c: colors[j] })).sort((a, b) => b.v - a.v);
      for (const { v, c } of vals) {
        if (v <= 0) continue; const rr = R * Math.sqrt(v / maxv);
        const x0 = cx + rr * Math.cos(a0), y0 = cy + rr * Math.sin(a0), x1 = cx + rr * Math.cos(a1), y1 = cy + rr * Math.sin(a1);
        s += `<path d="M${cx},${cy}L${x0},${y0}A${rr},${rr},0,0,1,${x1},${y1}Z" fill="${c}" fill-opacity=".92" stroke="${C.bg}" stroke-width="2"/>`;
      }
      const am = (a0 + a1) / 2, lr = R * 1.1; if (p.xkey) s += `<text x="${cx + lr * Math.cos(am)}" y="${cy + lr * Math.sin(am) + 8}" text-anchor="middle" fill="${C.muted}" font-size="22" opacity="${k}">${esc(r[p.xkey])}</text>`;
    });
    s += `</svg>` + legend(keys, colors, p.labels);
    return header(sc, p) + s + footer(sc, t, d);
  };

  // ---- line chart ----
  K.line = (sc, t, d) => {
    const p = sc.params, rows = rowsOf(p), b = chartBox(p), keys = p.series, colors = p.colors || SERIES;
    const xs0 = rows.map((r, i) => p.xkey_numeric ? +r[p.xkey_numeric] : i);
    const xmin = Math.min(...xs0), xmax = Math.max(...xs0);
    const ymax = p.ymax || Math.max(...rows.flatMap(r => keys.map(k => +r[k] || 0))) * 1.05;
    const xs = linScale(xmin, xmax, b.x, b.x + b.w), ys = linScale(p.ymin || 0, ymax, b.y + b.h, b.y);
    const reveal = p.reveal_seconds || Math.max(2, d - 2.5), k = easeOut(prog(t, 0.3, reveal));
    let s = `<svg width="${W}" height="${H}">` + axes(b, xs, ys, p.xkey_numeric ? niceTicks(xmin, xmax, 6) : [], niceTicks(p.ymin || 0, ymax), p.xlabel, p.ylabel);
    if (!p.xkey_numeric && p.xkey) rows.forEach((r, i) => { if (i % (p.xevery || 1) === 0) s += `<text x="${xs(i)}" y="${b.y + b.h + 34}" text-anchor="middle" fill="${C.muted}" font-size="20">${esc(r[p.xkey])}</text>`; });
    const clipW = b.w * k;
    s += `<defs><clipPath id="clipL"><rect x="${b.x}" y="${b.y - 10}" width="${clipW}" height="${b.h + 20}"/></clipPath></defs><g clip-path="url(#clipL)">`;
    keys.forEach((key, j) => { const pts = rows.map((r, i) => `${xs(xs0[i])},${ys(+r[key] || 0)}`).join(' '); s += `<polyline points="${pts}" fill="none" stroke="${colors[j]}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>`; });
    s += `</g>`;
    (p.markers || []).forEach(m => { const x = xs(m.x); const mk = easeOut(prog(t, m.at || 0, .5)); s += `<line x1="${x}" x2="${x}" y1="${b.y}" y2="${b.y + b.h}" stroke="${C.amber}" stroke-width="3" stroke-dasharray="10 8" opacity="${mk}"/><text x="${x + 12}" y="${b.y + 30}" fill="${C.amber}" font-size="26" opacity="${mk}">${esc(m.label)}</text>`; });
    s += `</svg>` + legend(keys, colors, p.labels);
    return header(sc, p) + s + footer(sc, t, d);
  };

  // ---- scatter ----
  function scatterSVG(p, t, d, b, data) {
    const rows = data || rowsOf(p);
    const xk = p.x, yk = p.y;
    const show = rows.filter(r => !p.hide_if || !eval(p.hide_if));
    const xd = p.xdomain || [Math.min(...rows.map(r => +r[xk])), Math.max(...rows.map(r => +r[xk]))];
    const yd = p.ydomain || [0, Math.max(...rows.map(r => +r[yk])) * 1.15];
    const xs = linScale(xd[0], xd[1], b.x, b.x + b.w), ys = linScale(yd[0], yd[1], b.y + b.h, b.y);
    let s = axes(b, xs, ys, niceTicks(xd[0], xd[1], 6), niceTicks(yd[0], yd[1], 5), p.xlabel, p.ylabel);
    const n = show.length, reveal = p.reveal_seconds || 2.0;
    show.forEach((r, i) => {
      const k = easeOut(prog(t, 0.3 + (i / n) * reveal, .4));
      const hl = p.highlight && eval(p.highlight);
      const jitter = p.jitter ? ((i * 37) % 7 - 3) * 1.5 : 0;
      s += `<circle cx="${xs(+r[xk]) + jitter}" cy="${ys(+r[yk])}" r="${11 * k}" fill="${hl ? C.amber : (p.color || C.sky)}" fill-opacity=".9" stroke="${C.bg}" stroke-width="2"/>`;
    });
    if (p.curve && t > (p.curve.at || 0)) {
      const k = easeOut(prog(t, p.curve.at || 0, p.curve.dur || 1.5));
      const pts = p.curve.points, m = Math.max(2, Math.round(pts.length * k));
      s += `<polyline points="${pts.slice(0, m).map(q => `${xs(q[0])},${ys(q[1])}`).join(' ')}" fill="none" stroke="${p.curve.color || C.coral}" stroke-width="5" stroke-linecap="round"/>`;
    }
    (p.markers || []).forEach(m => { const x = xs(m.x); const mk = easeOut(prog(t, m.at || 0, .5)); s += `<line x1="${x}" x2="${x}" y1="${b.y}" y2="${b.y + b.h}" stroke="${C.amber}" stroke-width="3" stroke-dasharray="10 8" opacity="${mk}"/><text x="${x + 12}" y="${b.y + 30}" fill="${C.amber}" font-size="26" opacity="${mk}">${esc(m.label)}</text>`; });
    return s;
  }
  K.scatter = (sc, t, d) => {
    const p = sc.params, b = chartBox(p);
    return header(sc, p) + `<svg width="${W}" height="${H}">${scatterSVG(p, t, d, b)}</svg>` + footer(sc, t, d);
  };
  K.compare = (sc, t, d) => {
    const p = sc.params; const gap = W * 0.04;
    const b0 = chartBox(p); const half = (b0.w - gap) / 2;
    let s = `<svg width="${W}" height="${H}">`;
    [p.left, p.right].forEach((q, i) => {
      const b = V ? { x: b0.x, y: b0.y + i * (b0.h / 2 + 30), w: b0.w, h: b0.h / 2 - 30 } : { x: b0.x + i * (half + gap), y: b0.y, w: half, h: b0.h };
      const show = i === 0 || t >= (p.right_at || 0);
      if (!show) return;
      s += `<text x="${b.x}" y="${b.y - 18}" fill="${C.paper}" font-size="28" font-weight="700">${esc(q.title || '')}</text>`;
      s += scatterSVG(Object.assign({}, q, { reveal_seconds: q.reveal_seconds || 1.5 }), t - (i === 0 ? 0 : (p.right_at || 0)), d, b);
    });
    return header(sc, p) + s + `</svg>` + footer(sc, t, d);
  };


  // ---- dots: N units appear over time in a grid, optionally grouped/colored by a data column ----
  K.dots = (sc, t, d) => {
    const p = sc.params; const rows = p.data ? rowsOf(p) : null;
    let groups = [];
    if (rows) rows.forEach((r, i) => { const n = +r[p.count_key] || 0; for (let k = 0; k < n; k++) groups.push({ g: i, label: r[p.label_key] }); });
    else for (let k = 0; k < (p.total || 100); k++) groups.push({ g: 0 });
    const N = groups.length, b = chartBox(p);
    const cols = p.cols || Math.ceil(Math.sqrt(N * b.w / b.h)), rowsN = Math.ceil(N / cols);
    const cell = Math.min(b.w / cols, b.h / rowsN), r = cell * 0.36;
    const reveal = p.reveal_seconds || Math.max(2, d - 2.5), k = prog(t, 0.3, reveal);
    const shown = Math.floor(N * easeOut(k));
    let s = `<svg width="${W}" height="${H}">`;
    for (let i = 0; i < shown; i++) {
      const x = b.x + (i % cols) * cell + cell / 2, y = b.y + Math.floor(i / cols) * cell + cell / 2;
      const hl = p.highlight_from !== undefined && groups[i].g >= p.highlight_from;
      s += `<circle cx="${x}" cy="${y}" r="${r}" fill="${hl ? C.amber : (p.color || C.coral)}" fill-opacity=".95"/>`;
    }
    s += `</svg><div class="legend"><div class="num" style="font-size:64px;font-weight:800;color:${C.paper}">${fmt(shown)}</div><div>${esc(p.unit || '')}</div></div>`;
    return header(sc, p) + s + footer(sc, t, d);
  };


  // ---- flow: Minard-style band whose width ∝ a count, drawn along (x,y) points in data order; optional temperature strip ----
  K.flow = (sc, t, d) => {
    const p = sc.params, rows = E.data[p.data], b = chartBox(p);
    const temp = p.temp_data ? E.data[p.temp_data] : null;
    const bh = temp ? b.h * 0.68 : b.h, tb = { x: b.x, y: b.y + bh + 50, w: b.w, h: b.h - bh - 50 };
    const xs0 = rows.map(r => +r[p.x]), ys0 = rows.map(r => +r[p.y]);
    const xmin = Math.min(...xs0) - .4, xmax = Math.max(...xs0) + .4, ymin = Math.min(...ys0) - .3, ymax = Math.max(...ys0) + .3;
    const xs = linScale(xmin, xmax, b.x, b.x + b.w), ys = linScale(ymin, ymax, b.y + bh, b.y);
    const maxv = p.vmax || Math.max(...rows.map(r => +r[p.size]));
    const wmax = (bh / 5.5), reveal = p.reveal_seconds || Math.max(3, d - 3), k = easeOut(prog(t, 0.4, reveal));
    // segments ordered: advance groups then retreat
    const groups = {};
    rows.forEach(r => { const g = `${r[p.group]}|${r[p.direction]}`; (groups[g] = groups[g] || []).push(r); });
    const order = Object.keys(groups).sort((a, b2) => (a.endsWith('A') ? 0 : 1) - (b2.endsWith('A') ? 0 : 1) || a.localeCompare(b2));
    let segs = [];
    for (const g of order) { const rs = groups[g]; for (let i = 0; i + 1 < rs.length; i++) segs.push({ a: rs[i], b: rs[i + 1], adv: g.endsWith('A') }); }
    const nShow = Math.floor(segs.length * k);
    let s = `<svg width="${W}" height="${H}">`;
    (p.cities_data ? E.data[p.cities_data] : []).forEach(c => { s += `<circle cx="${xs(+c[p.cx || 'long'])}" cy="${ys(+c[p.cy || 'lat'])}" r="5" fill="${C.muted}"/><text x="${xs(+c[p.cx || 'long']) + 10}" y="${ys(+c[p.cy || 'lat']) - 10}" fill="${C.muted}" font-size="20">${esc(c[p.city || 'city'])}</text>`; });
    segs.slice(0, nShow).forEach(sg => {
      const w = Math.max(2, wmax * (+sg.a[p.size]) / maxv);
      s += `<line x1="${xs(+sg.a[p.x])}" y1="${ys(+sg.a[p.y])}" x2="${xs(+sg.b[p.x])}" y2="${ys(+sg.b[p.y])}" stroke="${sg.adv ? C.amber : C.paper}" stroke-width="${w}" stroke-linecap="butt" stroke-opacity=".9"/>`;
    });
    if (nShow > 0) { const sg = segs[Math.max(0, nShow - 1)]; s += `<text x="${b.x + b.w - 10}" y="${b.y + bh - 10}" fill="${C.paper}" font-size="40" font-weight="800" text-anchor="end" class="num">${fmt(+sg.b[p.size])} <tspan font-size="22" font-weight="400" fill="${C.muted}">men (${sg.adv ? 'advance' : 'retreat'})</tspan></text>`; }
    if (temp) {
      const txs = xs, tmin = Math.min(...temp.map(r => +r[p.temp_y])) - 2, tys = linScale(tmin, 0, tb.y + tb.h, tb.y);
      s += `<path d="M${tb.x},${tys(0)}H${tb.x + tb.w}" stroke="${C.grid}" stroke-width="2"/>`;
      const pts = temp.map(r => `${txs(+r[p.temp_x])},${tys(+r[p.temp_y])}`).join(' ');
      const kt = easeOut(prog(t, reveal * 0.55, reveal * 0.45));
      s += `<defs><clipPath id="clipT"><rect x="${tb.x + tb.w * (1 - kt)}" y="${tb.y - 20}" width="${tb.w * kt + 2}" height="${tb.h + 40}"/></clipPath></defs>`;
      s += `<g clip-path="url(#clipT)"><polyline points="${pts}" fill="none" stroke="${C.sky}" stroke-width="4"/>`;
      temp.forEach((r, i) => { s += `<circle cx="${txs(+r[p.temp_x])}" cy="${tys(+r[p.temp_y])}" r="6" fill="${C.sky}"/><text x="${txs(+r[p.temp_x])}" y="${tys(+r[p.temp_y]) + (i % 2 ? 34 : -16)}" fill="${C.muted}" font-size="20" text-anchor="middle">${esc(r[p.temp_y])}°R ${esc(r[p.temp_label] || '')}</text>`; });
      s += `</g><text x="${tb.x}" y="${tb.y - 8}" fill="${C.muted}" font-size="22">${esc(p.temp_title || 'temperature during the retreat')}</text>`;
    }
    s += `</svg>` + legend(['advance', 'retreat'], [C.amber, C.paper], p.labels);
    return header(sc, p) + s + footer(sc, t, d);
  };

  window.renderFrame = function (idx, t, thumbSpec) {
    const sc = E.scenes[idx], d = sc.duration;
    const fn = K[sc.kind] || K.text;
    stage.innerHTML = fn(sc, t, d);
    const fin = Math.min(prog(t, 0, .35), 1 - prog(t, d - .35, .35));
    fade.style.opacity = String(1 - fin);
    if (thumbSpec) { thumb.style.display = 'block'; thumb.querySelector('.headline').innerHTML = rich(thumbSpec.headline || ''); thumb.querySelector('.sub').innerHTML = rich(thumbSpec.sub || ''); fade.style.opacity = '0'; }
    else thumb.style.display = 'none';
    return true;
  };
  window.checkOverflow = function () {
    const out = [];
    for (const el of stage.querySelectorAll('.title,.subtitle,.caption,.card .head,.card .sub,.card .big,.chart-title,.chart-sub,.legend')) {
      const r = el.getBoundingClientRect();
      if (r.right > W + 1 || r.bottom > H + 1 || r.left < -1 || r.top < -1 || el.scrollWidth > el.clientWidth + 2) out.push({ cls: el.className, text: (el.textContent || '').slice(0, 60), rect: [r.left, r.top, r.right, r.bottom] });
    }
    return out;
  };
})();
