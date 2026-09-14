# -*- coding: utf-8 -*-
"""
Regenerate demo_bridge.svg / .png for
    circuitry/Basic Circuit Analysis Method.md  §3.1 Demo Circuit

WHY: the old figure was topologically correct but carried NO polarity marks and
NO current arrows, while §3.1 claims "均按 AVD 方向（源/电阻上正下负 -> 电流向下）".
In a diamond layout that claim is not readable from the drawing at all.

HOW: pure matplotlib (no schemdraw).  Rationale:
  * schemdraw 0.23 here exports through the matplotlib backend (text -> vector
    paths, elm.Arrow arrowheads do NOT render).  Drawing directly in matplotlib
    gives reliable arrowheads via FancyArrowPatch.
  * every annotation lives in ONE table (ANN below, text included) in the SAME
    data coordinates as the schematic, so the companion checker can verify
    numerically that nothing overlaps and nothing sits on a conductor.

Circuit (same geometry as the old figure, so nothing else in the vault shifts):
      a = (2,4) top   b = (0,2) left   c = (2,0) bottom   d = (4,2) right
      V0 between a(+) and c(-)   [left vertical branch]
      R1(a-b) R2(b-c) R3(b-d) R4(a-d) R5(d-c)
      R3 and R4 cross geometrically at (2,2) but are NOT connected there.

Reference directions (AVD: current enters the '+' terminal):
      i0: c->a   i1: a->b   i2: b->c   i3: b->d   i4: a->d   i5: d->c
"""
import os
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

OUT = r'D:\obsidian_repository\电路原理\circuitry\assets'
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- geometry ---
A, B, C, D = (2.0, 4.0), (0.0, 2.0), (2.0, 0.0), (4.0, 2.0)
CR = (2.0, 2.0)                       # crossing of R3 and R4 - NOT a node
SRC_P, SRC_N = A, C
RES = {'R1': (A, B), 'R2': (B, C), 'R3': (B, D), 'R4': (A, D), 'R5': (D, C)}
SUB = '\u2080\u2081\u2082\u2083\u2084\u2085'

INK, ACC, RED, FADE = 'black', '#0b5fa5', '#a01010', '0.68'
ARR_D = 0.62                          # current-arrow length, data units
POL_D = 0.55                          # polarity symbol distance from its node


def unit(p, q):
    L = math.hypot(q[0] - p[0], q[1] - p[1])
    return ((q[0] - p[0]) / L, (q[1] - p[1]) / L)


def toward(src, dst, d):
    ux, uy = unit(src, dst)
    return (src[0] + ux * d, src[1] + uy * d)


# ------------------------------------------------- annotation coord table ----
# (kind, text, anchor, ha, va)   kind in pol | name | ilab | node
ANN = [('pol', 'v' + SUB[0], toward(SRC_P, SRC_N, POL_D), 'c', 'c'),   # on the wire
       ('pol', '\u2212', (2.0, 0.30), 'c', 'c')]                       # on the wire
for k, (pp, nn) in enumerate(RES.values(), start=1):
    ANN.append(('pol', 'v' + SUB[k], toward(pp, nn, POL_D), 'c', 'c'))
    ANN.append(('pol', '\u2212', toward(nn, pp, POL_D), 'c', 'c'))

for txt, xy in [('V' + SUB[0], (2.42, -0.78)), ('R1', (0.34, 3.42)), ('R2', (0.62, 0.58)),
                ('R3', (3.36, 1.78)), ('R4', (2.72, 3.60)), ('R5', (3.34, 0.94))]:
    ANN.append(('name', txt, xy, 'l', 'c'))

for txt, xy in [('i0', (3.24, -0.66)), ('i1', (0.52, 3.32)), ('i2', (0.94, 1.36)),
                ('i3', (2.74, 1.58)), ('i4', (3.32, 2.94)), ('i5', (2.66, 0.82))]:
    ANN.append(('ilab', txt, xy, 'l', 'c'))

for txt, xy, ha, va in [('a', (2.13, 4.16), 'l', 'b'), ('b', (-0.18, 2.14), 'r', 'b'),
                        ('c', (2.13, -0.16), 'l', 't'), ('d', (4.18, 2.14), 'l', 'b')]:
    ANN.append(('node', txt, xy, ha, va))

# current arrows: (label, tail, plus-node, minus-node) - head = tail + ARR_D*unit(+ -> -)
IARR = [('i0', (1.62, -0.52), SRC_P, SRC_N), ('i1', (0.44, 3.30), A, B),
        ('i2', (1.20, 1.40), B, C), ('i3', (2.62, 1.74), B, D),
        ('i4', (3.34, 3.19), A, D), ('i5', (2.62, 0.72), D, C)]


# ------------------------------------------------------------------ helpers ---
def zigzag(ax, p, q, n=8, amp=0.25):
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
    ax.plot([t[0] for t in pts], [t[1] for t in pts], color=INK, lw=1.6,
            solid_joinstyle='miter', solid_capstyle='butt')


def wire(ax, p, q):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=INK, lw=1.6, solid_capstyle='round')


def put(ax, txt, xy, ha, va, size, color):
    ax.text(xy[0], xy[1], txt, fontsize=size, color=color, ha=ha, va=va, zorder=6,
            bbox=dict(fc='white', ec='none', pad=0.5))


# -------------------------------------------------------------------- draw ---
def build():
    fig = plt.figure(figsize=(2.637, 4.168), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(-0.45, 4.45)
    ax.set_ylim(-1.05, 4.50)
    ax.set_aspect('equal')
    ax.axis('off')

    for pp, nn in RES.values():                        # resistors first
        zigzag(ax, pp, nn)

    wire(ax, A, (2.0, 2.60))                           # V0 leads
    wire(ax, (2.0, 1.40), C)
    ax.plot([2 - 0.28, 2 + 0.28], [1.40, 1.40], color=INK, lw=3.4, solid_capstyle='butt')
    ax.plot([2 - 0.46, 2 + 0.46], [2.60, 2.60], color=INK, lw=1.6, solid_capstyle='butt')

    for p in (A, B, C, D):                             # junction dots
        ax.add_patch(plt.Circle(p, 0.075, color=INK, zorder=4))

    ax.add_patch(Rectangle((CR[0] - 0.50, CR[1] - 0.50), 1.00, 1.00, fill=False,
                           ec=FADE, ls=(0, (2.2, 1.6)), lw=0.9, zorder=3))

    for kind, txt, xy, ha, va in ANN:                  # annotations off the table
        size, color = {'pol': (12.5, None), 'name': (13, INK),
                       'ilab': (12, ACC), 'node': (15, INK)}[kind]
        if kind == 'pol':
            color = RED if txt.startswith('v') else INK
            if not txt.startswith('v'):
                size = 14
        put(ax, txt, xy, ha, va, size, color)

    for key, tail, plus, minus in IARR:                # current arrows
        ux, uy = unit(plus, minus)
        head = (tail[0] + ux * ARR_D, tail[1] + uy * ARR_D)
        ax.add_patch(FancyArrowPatch(tail, head, arrowstyle='-|>', mutation_scale=11,
                                     lw=1.7, color=ACC, shrinkA=0, shrinkB=0, zorder=5))
    return fig


if __name__ == '__main__':
    fig = build()
    fig.savefig(os.path.join(OUT, 'demo_bridge.svg'), format='svg',
                facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(OUT, 'demo_bridge.png'), format='png', dpi=200,
                facecolor='white', edgecolor='none')
    print('written demo_bridge.svg / .png to', OUT)
    print('annotations:', sum(1 for a in ANN if a[0] == 'pol'), 'polarity,',
          sum(1 for a in ANN if a[0] == 'name'), 'names,',
          sum(1 for a in ANN if a[0] == 'ilab'), 'current labels,',
          sum(1 for a in ANN if a[0] == 'node'), 'node labels;',
          len(IARR), 'arrows')
