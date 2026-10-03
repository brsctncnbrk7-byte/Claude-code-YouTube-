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
    const p = sc.params, rows = E.data[p.data], b = chartBox(p), keys = p.series, colors = p.colors || SERIES;
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
    const p = sc.params, rows = E.data[p.data], b = chartBox(p), keys = p.series, colors = p.colors || SERIES;
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
    const rows = data || E.data[p.data];
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
