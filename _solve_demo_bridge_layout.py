# -*- coding: utf-8 -*-
"""
Solver for demo_bridge layout (round 2).

Round 1 failed: the arrow search allowed huge lateral offsets, so i0 landed
INSIDE the diamond and i1/i2/i4 were flung 0.83 units away from their branch,
while i5 had no legal slot at all.  Round 2 pins the design intent first:

  * a current arrow runs PARALLEL to its branch, on the OUTWARD side, at a small
    fixed lateral offset (~0.28 unit) so it obviously belongs to that branch;
  * nothing may sit inside the dashed "this crossing is not a node" box;
  * annotation boxes are only the ink footprint, so neighbouring labels may sit
    close to each other (they are separated by white halos anyway).

Output: demo_bridge_geo.json  -> consumed by the generator.
"""
import importlib.util
import json
import math
import numpy as np

GEN = r'D:\obsidian_repository\电路原理\_gen_demo_bridge_avd.py'
OUTJSON = r'D:\obsidian_repository\电路原理\circuitry\assets\demo_bridge_geo.json'

import matplotlib
matplotlib.use('Agg')
spec = importlib.util.spec_from_file_location('gen', GEN)
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)

A, B, C, D = gen.A, gen.B, gen.C, gen.D
RES, SUB = gen.RES, gen.SUB
CLEAR = 0.16                       # min copper clearance for a non-polarity label
GAP = 0.05
XLIM, YLIM = (-0.45, 4.45), (-1.05, 4.50)
CROSSBOX = (1.50, 1.50, 2.50, 2.50)     # x0,y0,x1,y1 - keep clear of it


def zigzag_pts(p, q, n=8, amp=0.25):
    dx, dy = q[0] - p[0], q[1] - p[1]
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    pts = [p]
    for k in range(n):
        t = (k + 0.5) / n
        s = amp if k % 2 == 0 else -amp
        pts.append((p[0] + ux * L * t + nx * s, p[1] + uy * L * t + ny * s))
    pts.append(q)
    return pts


POLY = {nm: zigzag_pts(p, q) for nm, (p, q) in RES.items()}
POLY['V0_lead_top'] = [(2.0, 4.0), (2.0, 2.60)]
POLY['V0_lead_bot'] = [(2.0, 1.40), (2.0, 0.0)]
POLY['V0_plate_m'] = [(2 - 0.28, 1.40), (2 + 0.28, 1.40)]
POLY['V0_plate_p'] = [(2 - 0.46, 2.60), (2 + 0.46, 2.60)]
for i, p in enumerate((A, B, C, D)):
    POLY[f'dot{i}'] = [p, p]

SEGS = [(nm, np.array(pts[k], float), np.array(pts[k + 1], float))
        for nm, pts in POLY.items() for k in range(len(pts) - 1)]
BOXSEGS = [('cross_left', np.array([1.5, 1.5]), np.array([1.5, 2.5])),
           ('cross_right', np.array([2.5, 1.5]), np.array([2.5, 2.5])),
           ('cross_bot', np.array([1.5, 1.5]), np.array([2.5, 1.5])),
           ('cross_top', np.array([1.5, 2.5]), np.array([2.5, 2.5]))]


def seg_clear(p0, p1, g0, g1):
    ts = np.linspace(0, 1, 80)
    a = p0[None, :] + (p1 - p0)[None, :] * ts[:, None]
    b = g0[None, :] + (g1 - g0)[None, :] * ts[:, None]
    return float(np.linalg.norm(a[:, None, :] - b[None, :, :], axis=2).min())


def rect_gap(b1, b2):
    dx = max(b1[0] - b2[2], b2[0] - b1[2], 0.0)
    dy = max(b1[1] - b2[3], b2[1] - b1[3], 0.0)
    return math.hypot(dx, dy)


def rect_rect_overlap(b1, b2):
    ox = min(b1[2], b2[2]) - max(b1[0], b2[0])
    oy = min(b1[3], b2[3]) - max(b1[1], b2[1])
    if ox <= 0 or oy <= 0:
        return 0.0
    return ox * oy


def rect_box_overlap(b, box):
    ox = min(b[2], box[2]) - max(b[0], box[0])
    oy = min(b[3], box[3]) - max(b[1], box[1])
    if ox <= 0 or oy <= 0:
        return 0.0
    return ox * oy


def rect_seg_gap(b, p0, p1):
    cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
    hx, hy = (b[2] - b[0]) / 2, (b[3] - b[1]) / 2
    best = 1e9
    for t in np.linspace(0, 1, 110):
        pt = p0 + (p1 - p0) * t
        dx = max(abs(pt[0] - cx) - hx, 0.0)
        dy = max(abs(pt[1] - cy) - hy, 0.0)
        best = min(best, math.hypot(dx, dy))
    return best


BOXW = {'pol': 0.22, 'name': 0.46, 'ilab': 0.28, 'node': 0.26}
BOXH = {'pol': 0.30, 'name': 0.32, 'ilab': 0.28, 'node': 0.32}


def box_of(kind, xy, ha, va):
    w, h = BOXW[kind], BOXH[kind]
    x, y = xy
    x0 = x if ha == 'l' else (x - w if ha == 'r' else x - w / 2)
    y0 = y - h / 2 if va == 'c' else (y if va == 'b' else y - h)
    return (x0, y0, x0 + w, y0 + h)


def in_view(b):
    return (b[0] >= XLIM[0] + 0.02 and b[2] <= XLIM[1] - 0.02
            and b[1] >= YLIM[0] + 0.02 and b[3] <= YLIM[1] - 0.02)


# ------------------------------------------------ fixed boxes (from ANN) -----
reserved = []
names = []
for kind, txt, xy, ha, va in gen.ANN:
    b = box_of(kind, xy, ha, va)
    reserved.append(b)
    names.append((kind, txt, xy))

# ---------------------------------------------- solve the free label slots ---
ANNEXT = [('V0_plate_minus', 'pol', '\u2212', 'c', 'c', (2.0, 1.15), ['V0_plate_m']),
          ('R3_minus',       'pol', '\u2212', 'c', 'c', (3.70, 1.95), []),
          ('R5_name',        'name', 'R5',    'l', 'c', (3.42, 1.02), []),
          ('R5_i5',          'ilab', 'i5',    'l', 'c', (2.64, 0.68), []),
          ('V0_name',        'name', 'V' + SUB[0], 'l', 'c', (2.45, -0.62), []),
          ('V0_i0',          'ilab', 'i0',    'l', 'c', (3.18, -0.60), [])]

solved = {}
print('=== solved label slots ===')
for key, kind, txt, ha, va, nom, forbid in ANNEXT:
    cands = []
    for dx in np.arange(-0.9, 0.91, 0.06):
        for dy in np.arange(-0.9, 0.91, 0.06):
            xy = (nom[0] + dx, nom[1] + dy)
            b = box_of(kind, xy, ha, va)
            if not in_view(b):
                continue
            if rect_box_overlap(b, CROSSBOX) > 0:
                continue
            if any(rect_rect_overlap(b, r) > 0 for r in reserved):
                continue
            worst = 1e9
            for nm, g0, g1 in SEGS:
                if nm in forbid:
                    continue
                worst = min(worst, rect_seg_gap(b, g0, g1))
            if worst >= CLEAR:
                cands.append((abs(dx) + abs(dy), xy, b, worst))
    if not cands:
        print(f'  !! NO LEGAL SLOT for {key}')
        solved[key] = None
        continue
    cands.sort(key=lambda c: c[0])
    _, xy, b, worst = cands[0]
    solved[key] = {'xy': xy, 'box': b, 'clear': worst}
    reserved.append(b)
    print(f'  {key:16s} xy=({xy[0]:6.2f},{xy[1]:6.2f})  clearance={worst:.3f}  '
          f'(moved {abs(xy[0]-nom[0]):.2f},{abs(xy[1]-nom[1]):.2f} from nominal)')

# --------------------------------------------------- solve current arrows ----
BRANCH = {'i0': (A, C), 'i1': (A, B), 'i2': (B, C), 'i3': (B, D), 'i4': (A, D), 'i5': (D, C)}
CENT = np.array([2.0, 2.0])
IDX = list(BRANCH)
arrows = {}
print()
print('=== solved current arrows (parallel, outward) ===')
for key, (p, m) in BRANCH.items():
    P, M = np.array(p, float), np.array(m, float)
    u = (M - P) / np.linalg.norm(M - P)
    n = np.array([-u[1], u[0]])
    if float((((P + M) / 2) - CENT) @ n) < 0:
        n = -n
    cands = []
    for off in (0.30, 0.34, 0.26, 0.38, 0.42, 0.22):
        for f in np.arange(0.30, 0.71, 0.02):
            c = P + (M - P) * f + n * off
            t = c - u * (gen.ARR_D / 2)
            h = c + u * (gen.ARR_D / 2)
            if not (XLIM[0] + 0.03 < min(t[0], h[0]) and max(t[0], h[0]) < XLIM[1] - 0.03
                    and YLIM[0] + 0.03 < min(t[1], h[1]) and max(t[1], h[1]) < YLIM[1] - 0.03):
                continue
            ab = (min(t[0], h[0]) - 0.03, min(t[1], h[1]) - 0.03,
                  max(t[0], h[0]) + 0.03, max(t[1], h[1]) + 0.03)
            if rect_box_overlap(ab, CROSSBOX) > 0:
                continue
            if any(rect_rect_overlap(ab, r) > 0 for r in reserved):
                continue
            worst = 1e9
            for nm, g0, g1 in SEGS:
                if nm.startswith('dot') or nm.startswith('V0_plate'):
                    continue
                worst = min(worst, seg_clear(t.astype(float), h.astype(float), g0, g1))
            for nm, g0, g1 in BOXSEGS:            # stay out of the dashed box lines
                worst = min(worst, seg_clear(t.astype(float), h.astype(float), g0, g1))
            if worst >= CLEAR:
                cands.append((abs(off - 0.30) + abs(f - 0.5), off, f, tuple(np.round(t, 2)),
                              tuple(np.round(h, 2)), worst))
    if not cands:
        print(f'  !! NO LEGAL SLOT for arrow {key}')
        arrows[key] = None
        continue
    cands.sort(key=lambda c: c[0])
    _, off, f, t, h, worst = cands[0]
    arrows[key] = {'tail': list(t), 'head': list(h), 'clearance': round(worst, 3),
                   'offset': off, 'f': round(float(f), 2)}
    print(f'  {key}: tail=({t[0]:5.2f},{t[1]:5.2f}) -> head=({h[0]:5.2f},{h[1]:5.2f})  '
          f'offset={off:.2f} f={f:.2f} clearance={worst:.3f}')

json.dump({'slots': {k: (None if v is None else {'xy': list(v['xy']), 'clear': round(v['clear'], 3)})
                     for k, v in solved.items()},
           'arrows': arrows}, open(OUTJSON, 'w'), indent=1)
print()
print('wrote', OUTJSON)
