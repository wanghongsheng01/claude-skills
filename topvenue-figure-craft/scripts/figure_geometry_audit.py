#!/usr/bin/env python3
"""figure_geometry_audit.py -- geometric collision audit for paper figures.

Catches the defects that make a schematic look like an engineering draft:
labels sitting on lines, text touching box borders, arrows running through
boxes or container title bands, overlapping text, text off the canvas.

Modes
-----
  run SCRIPT.py [--match SUBSTR ...] [--no-save | --out-dir DIR] [-- SCRIPT_ARGS...]
      Execute a matplotlib figure script with Figure.savefig hooked. Every figure
      is audited right before it is saved (all artists are laid out by then).
      Use --match to audit only files whose save path contains SUBSTR.
      SAFETY: figure scripts often hard-code absolute output paths. Run a COPY of
      the script, and pass --no-save or --out-dir so savefig() cannot overwrite
      the real figures. Writes made without savefig (json dumps, PIL previews)
      are not intercepted: grep the copy for absolute paths and rewrite them.
  pdf FIGURE.pdf [--page N]
      Audit a vector PDF (TikZ, matplotlib, Inkscape ...). Text comes from the
      PDF text layer, boxes/arrows from the vector drawing operators. Best for
      schematics; data plots with grid lines produce noise.
  selftest
      Build a deliberately broken figure and a clean one; verify detection.

Python API
----------
  from figure_geometry_audit import audit_matplotlib_figure
  findings = audit_matplotlib_figure(fig, name="fig1")

Checks (severity FAIL unless noted)
-----------------------------------
  TEXT_ON_LINE            text bbox (+clearance) intersects a line/arrow path
                          (WARN if the text has an opaque background box and
                          --strict is off: a masked label still reads as clutter)
  TEXT_ON_BORDER          text bbox (+clearance) intersects a box/container edge
  TEXT_OVERLAP            two text bboxes overlap
  TEXT_OUTSIDE_CANVAS     text extends beyond the figure canvas
                          (WARN when saved with bbox_inches="tight")
  LINE_THROUGH_CONTAINER  a connector enters the interior of a box that is
                          neither its source nor its target
  LINE_CROSSES_BORDER     a connector crosses the border of a container that
                          holds only one of its endpoints (route to the
                          container border instead, or keep both ends inside);
                          WARN with --allow-parent-entry
  LINE_THROUGH_TITLE      a connector passes through a container's title band
  ENDPOINT_INSIDE_BOX     (WARN) arrow continues into its endpoint box instead of
                          stopping on the border
  LINE_CROSSING           (WARN) two diagram connectors cross each other
  LEGEND_OVER_DATA        (WARN) legend box covers a data line or bar
  DANGLING_ARROW          (WARN) arrow tip touches no box, text or other line

Exit code: 0 = no FAIL, 1 = at least one FAIL, 2 = usage / runtime error.
Coordinates are reported in points from the bottom-left of the canvas, plus
data coordinates of the axes for matplotlib figures (to find the line in code).
"""
from __future__ import annotations

import argparse
import json
import math
import os
import runpy
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

Point = Tuple[float, float]
Rect = Tuple[float, float, float, float]  # x0, y0, x1, y1 (y up)


# ---------------------------------------------------------------- options
@dataclass
class Options:
    clearance: float = 2.0        # pt, min gap between text and lines/borders
    endpoint_tol: float = 3.0     # pt, how close an arrow end must be to a border
    junction_tol: float = 2.5     # pt, polyline pieces closer than this are chained
    strict: bool = False          # promote every WARN to FAIL
    allow_parent_entry: bool = False
    min_container: float = 6.0    # pt, smaller closed shapes are not containers
    min_connector: float = 12.0   # pt, shorter non-arrow strokes are decorations (cross marks, ticks)


# ---------------------------------------------------------------- geometry
def inflate(r: Rect, d: float) -> Rect:
    return (r[0] - d, r[1] - d, r[2] + d, r[3] + d)


def rect_w(r: Rect) -> float:
    return r[2] - r[0]


def rect_h(r: Rect) -> float:
    return r[3] - r[1]


def rect_area(r: Rect) -> float:
    return max(0.0, rect_w(r)) * max(0.0, rect_h(r))


def rects_intersect(a: Rect, b: Rect) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def overlap_rect(a: Rect, b: Rect) -> Optional[Rect]:
    r = (max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3]))
    return r if r[0] < r[2] and r[1] < r[3] else None


def rect_inside(a: Rect, b: Rect, slack: float = 0.0) -> bool:
    return a[0] >= b[0] - slack and a[1] >= b[1] - slack and a[2] <= b[2] + slack and a[3] <= b[3] + slack


def center(r: Rect) -> Point:
    return ((r[0] + r[2]) / 2, (r[1] + r[3]) / 2)


def point_strictly_inside(p: Point, r: Rect, margin: float) -> bool:
    return r[0] + margin < p[0] < r[2] - margin and r[1] + margin < p[1] < r[3] - margin


def dist_to_boundary(p: Point, r: Rect) -> float:
    x, y = p
    if r[0] <= x <= r[2] and r[1] <= y <= r[3]:
        return min(x - r[0], r[2] - x, y - r[1], r[3] - y)
    dx = max(r[0] - x, 0.0, x - r[2])
    dy = max(r[1] - y, 0.0, y - r[3])
    return math.hypot(dx, dy)


def clip_segment(p: Point, q: Point, r: Rect) -> Optional[Tuple[float, float]]:
    """Liang-Barsky: parameter interval [t0, t1] of segment p->q inside rect r."""
    x0, y0 = p
    dx, dy = q[0] - x0, q[1] - y0
    t0, t1 = 0.0, 1.0
    for pk, qk in ((-dx, x0 - r[0]), (dx, r[2] - x0), (-dy, y0 - r[1]), (dy, r[3] - y0)):
        if abs(pk) < 1e-12:
            if qk < 0:
                return None
        else:
            t = qk / pk
            if pk < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
            if t0 > t1:
                return None
    return (t0, t1)


def polyline_in_rect(pts: Sequence[Point], r: Rect) -> Tuple[float, Optional[Point]]:
    """Total length of polyline inside rect and midpoint of the longest piece."""
    total, best, best_pt = 0.0, 0.0, None
    for p, q in zip(pts[:-1], pts[1:]):
        c = clip_segment(p, q, r)
        if not c:
            continue
        seg_len = math.hypot(q[0] - p[0], q[1] - p[1]) * (c[1] - c[0])
        if seg_len <= 0:
            continue
        total += seg_len
        if seg_len > best:
            tm = (c[0] + c[1]) / 2
            best, best_pt = seg_len, (p[0] + (q[0] - p[0]) * tm, p[1] + (q[1] - p[1]) * tm)
    return total, best_pt


def polyline_length(pts: Sequence[Point]) -> float:
    return sum(math.hypot(q[0] - p[0], q[1] - p[1]) for p, q in zip(pts[:-1], pts[1:]))


def trim_polyline(pts: Sequence[Point], d: float) -> List[Point]:
    """Remove length d from both ends of a polyline."""
    def trim_start(ps: List[Point], d: float) -> List[Point]:
        out = list(ps)
        while len(out) >= 2 and d > 0:
            p, q = out[0], out[1]
            L = math.hypot(q[0] - p[0], q[1] - p[1])
            if L <= d:
                d -= L
                out.pop(0)
            else:
                t = d / L
                out[0] = (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
                d = 0
        return out
    if polyline_length(pts) <= 2 * d:
        return []
    out = trim_start(list(pts), d)
    out = trim_start(out[::-1], d)[::-1]
    return out if len(out) >= 2 else []


def segments_cross(p1: Point, p2: Point, q1: Point, q2: Point) -> Optional[Point]:
    """Proper intersection point of two segments, or None."""
    d = (p2[0] - p1[0]) * (q2[1] - q1[1]) - (p2[1] - p1[1]) * (q2[0] - q1[0])
    if abs(d) < 1e-9:
        return None
    t = ((q1[0] - p1[0]) * (q2[1] - q1[1]) - (q1[1] - p1[1]) * (q2[0] - q1[0])) / d
    u = ((q1[0] - p1[0]) * (p2[1] - p1[1]) - (q1[1] - p1[1]) * (p2[0] - p1[0])) / d
    if 0.0 < t < 1.0 and 0.0 < u < 1.0:
        return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]))
    return None


def boundary_crossings(pts: Sequence[Point], r: Rect) -> List[Point]:
    """Points where a polyline crosses the outline of rect r."""
    corners = [(r[0], r[1]), (r[2], r[1]), (r[2], r[3]), (r[0], r[3])]
    edges = list(zip(corners, corners[1:] + corners[:1]))
    out = []
    for p, q in zip(pts[:-1], pts[1:]):
        for a, b in edges:
            x = segments_cross(p, q, a, b)
            if x:
                out.append(x)
    return out


def rect_edges_hit(text: Rect, box: Rect) -> bool:
    """True if rect `text` touches the outline of `box` (not merely inside/outside)."""
    if not rects_intersect(text, box):
        return False
    if rect_inside(text, box):
        return False
    if rect_inside(box, text):
        return False
    return True


# ---------------------------------------------------------------- model
@dataclass
class TextItem:
    id: int
    text: str
    rect: Rect
    kind: str = "label"            # label | title | axis | tick | legend
    masked: bool = False           # has an opaque background box
    own_connectors: set = field(default_factory=set)
    axes: object = None


@dataclass
class Container:
    id: int
    rect: Rect
    label: str = ""
    title_band: Optional[Rect] = None
    axes: object = None
    data_axes: bool = False        # bar in a data plot (not a diagram box)


@dataclass
class Connector:
    id: int
    pts: List[Point]
    arrow: bool = False
    diagram: bool = True           # lives in a schematic (axis-off) axes / PDF
    axes: object = None
    desc: str = ""
    seqno: int = 0                 # drawing order (pdf mode)


@dataclass
class Finding:
    severity: str
    code: str
    figure: str
    message: str
    at_pt: Optional[Point] = None
    at_data: Optional[Point] = None

    def line(self) -> str:
        loc = ""
        if self.at_pt:
            loc += f" @pt({self.at_pt[0]:.1f},{self.at_pt[1]:.1f})"
        if self.at_data:
            loc += f" data({self.at_data[0]:.3g},{self.at_data[1]:.3g})"
        return f"[{self.severity}] {self.code:<22} {self.figure}: {self.message}{loc}"


def short(s: str, n: int = 38) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "\u2026"


# ---------------------------------------------------------------- core checks
def assign_titles(texts: List[TextItem], containers: List[Container], opts: Options) -> None:
    for c in containers:
        if c.data_axes:
            continue
        inside = [t for t in texts if t.kind in ("label", "title") and t.axes is c.axes
                  and rect_inside(t.rect, c.rect, slack=1.0)]
        children = [o for o in containers if o is not c and o.axes is c.axes and not o.data_axes
                    and rect_inside(o.rect, c.rect, slack=0.5) and rect_area(o.rect) < rect_area(c.rect) * 0.95]
        direct = [t for t in inside if not any(rect_inside(t.rect, ch.rect, slack=0.5) for ch in children)]
        if not c.label:
            pool = inside or direct
            if pool:
                c.label = short(max(pool, key=lambda t: t.rect[3]).text, 30)
        if not direct:
            continue
        top = max(direct, key=lambda t: t.rect[3])
        others_below = [t for t in inside if t is not top and t.rect[3] <= top.rect[1] + 1.0]
        gap = c.rect[3] - top.rect[3]
        if (others_below or children) and gap <= max(12.0, 0.35 * rect_h(c.rect)):
            c.title_band = (c.rect[0], top.rect[1] - opts.clearance, c.rect[2], c.rect[3])
            c.label = short(top.text, 30)


def chain_connectors(conns: List[Connector], tol: float) -> List[Connector]:
    """Merge polyline pieces that meet end-to-end at degree-2 junctions."""
    pool = [c for c in conns if c.diagram]
    rest = [c for c in conns if not c.diagram]

    def close(a: Point, b: Point) -> bool:
        return math.hypot(a[0] - b[0], a[1] - b[1]) <= tol

    changed = True
    while changed:
        changed = False
        ends = []
        for i, c in enumerate(pool):
            ends.append((i, 0, c.pts[0]))
            ends.append((i, 1, c.pts[-1]))
        for a_i, a_side, a_pt in ends:
            matches = [(b_i, b_side) for b_i, b_side, b_pt in ends if b_i != a_i and pool[b_i].axes is pool[a_i].axes and close(a_pt, b_pt)]
            if len(matches) != 1:
                continue
            b_i, b_side = matches[0]
            # junction degree must be exactly 2 (no other end nearby)
            a, b = pool[a_i], pool[b_i]
            if a.arrow and b.arrow:
                continue  # two arrowheads meeting: keep separate
            pa = a.pts if a_side == 1 else a.pts[::-1]
            pb = b.pts if b_side == 0 else b.pts[::-1]
            # the arrowhead must stay at the far end of the merged polyline
            merged = Connector(id=a.id, pts=pa + pb[1:], arrow=a.arrow or b.arrow, diagram=True,
                               axes=a.axes, desc="", seqno=min(a.seqno, b.seqno))
            # keep the arrowhead (original last point of the arrow piece) at the merged end
            tip = a.pts[-1] if a.arrow else (b.pts[-1] if b.arrow else None)
            if tip is not None and close(merged.pts[0], tip) and not close(merged.pts[-1], tip):
                merged.pts = merged.pts[::-1]
            pool = [c for k, c in enumerate(pool) if k not in (a_i, b_i)] + [merged]
            changed = True
            break
    return pool + rest


def run_checks(name: str, texts: List[TextItem], containers: List[Container], connectors: List[Connector],
               canvas: Rect, opts: Options, tight: bool = False, legends: Sequence[Tuple[Rect, object]] = (),
               to_data=None, describe=None) -> List[Finding]:
    F: List[Finding] = []
    seen = set()

    def add(sev: str, code: str, msg: str, at: Optional[Point], ax=None, key=None):
        if opts.strict and sev == "WARN":
            sev = "FAIL"
        k = key or (code, msg)
        if k in seen:
            return
        seen.add(k)
        dat = to_data(ax, at) if (to_data and ax is not None and at is not None) else None
        F.append(Finding(sev, code, name, msg, at, dat))

    assign_titles(texts, containers, opts)
    connectors = chain_connectors(connectors, opts.junction_tol)
    for i, c in enumerate(connectors):
        if not c.desc:
            c.desc = describe(c) if describe else (
                f"{'arrow' if c.arrow else 'line'}({c.pts[0][0]:.0f},{c.pts[0][1]:.0f})->({c.pts[-1][0]:.0f},{c.pts[-1][1]:.0f})pt")

    # ---- C1 text vs connector
    for t in texts:
        if t.kind in ("tick", "legend"):
            continue
        box = inflate(t.rect, opts.clearance)
        for c in connectors:
            if c.id in t.own_connectors or len(c.pts) < 2:
                continue
            if c.axes is not None and t.axes is not None and c.axes is not t.axes and not c.diagram:
                continue
            L, at = polyline_in_rect(c.pts, box)
            if L <= 0.05:
                continue
            hard, _ = polyline_in_rect(c.pts, t.rect)
            how = "overlaps" if hard > 0.05 else f"within {opts.clearance:g}pt of"
            sev = "WARN" if (t.masked and hard > 0.05) else "FAIL"
            add(sev, "TEXT_ON_LINE", f'text "{short(t.text)}" {how} {"arrow" if c.arrow else "line"} {c.desc}',
                at, t.axes, key=("C1", t.id, c.id))

    # ---- C2 text vs container border
    for t in texts:
        if t.kind not in ("label", "title"):
            continue
        box = inflate(t.rect, opts.clearance)
        for c in containers:
            if c.axes is not None and t.axes is not None and c.axes is not t.axes:
                continue
            if not rect_edges_hit(box, c.rect):
                continue
            # badge: a small shape wrapped tightly around a single text
            if point_strictly_inside(center(t.rect), c.rect, 0) and rect_area(c.rect) <= 4.0 * rect_area(t.rect):
                continue
            ov = overlap_rect(box, c.rect)
            hard = rect_edges_hit(t.rect, c.rect)
            how = "crosses" if hard else f"is within {opts.clearance:g}pt of"
            what = "bar" if c.data_axes else "box"
            add("FAIL", "TEXT_ON_BORDER", f'text "{short(t.text)}" {how} border of {what} "{c.label or "?"}"',
                center(ov) if ov else center(t.rect), t.axes, key=("C2", t.id, c.id))

    # ---- C3 text vs text
    for i, a in enumerate(texts):
        for b in texts[i + 1:]:
            ov = overlap_rect(a.rect, b.rect)
            if ov and rect_area(ov) > 0.5:
                add("FAIL", "TEXT_OVERLAP", f'"{short(a.text, 24)}" overlaps "{short(b.text, 24)}"', center(ov),
                    a.axes, key=("C3", a.id, b.id))

    # ---- C4 canvas
    for t in texts:
        if not rect_inside(t.rect, canvas, slack=0.5):
            sev = "WARN" if tight else "FAIL"
            add(sev, "TEXT_OUTSIDE_CANVAS", f'text "{short(t.text)}" extends beyond the canvas', center(t.rect), t.axes,
                key=("C4", t.id))

    # ---- C5 connector routing (diagram connectors only)
    tol = opts.endpoint_tol
    # very short strokes (cross marks, ticks, tiny glyph-like decorations) are not connectors
    diag = [c for c in connectors if c.diagram and len(c.pts) >= 2 and polyline_length(c.pts) > 2 * tol
            and (c.arrow or polyline_length(c.pts) > opts.min_connector)]
    diag_boxes = [b for b in containers if not b.data_axes]
    for c in diag:
        s, e = c.pts[0], c.pts[-1]
        core = trim_polyline(c.pts, tol)
        for b in diag_boxes:
            if b.axes is not None and c.axes is not None and b.axes is not c.axes:
                continue
            ds, de = dist_to_boundary(s, b.rect), dist_to_boundary(e, b.rect)
            s_in = point_strictly_inside(s, b.rect, tol)
            e_in = point_strictly_inside(e, b.rect, tol)
            is_endpoint = ds <= tol or de <= tol
            shrunk = inflate(b.rect, -tol)
            inner_len, at = (polyline_in_rect(core, shrunk) if core and rect_w(shrunk) > 0 and rect_h(shrunk) > 0
                             else (0.0, None))
            if b.title_band and core:
                bl, bat = polyline_in_rect(core, b.title_band)
                if bl > 0.5:
                    add("FAIL", "LINE_THROUGH_TITLE", f'{c.desc} passes through the title band of "{b.label}"', bat,
                        c.axes, key=("C5t", c.id, b.id))
            if s_in and e_in:
                continue  # container holds both ends: internal edge
            if is_endpoint and not (s_in or e_in):
                if inner_len > tol and c.arrow:
                    add("WARN", "ENDPOINT_INSIDE_BOX", f'{c.desc} runs {inner_len:.1f}pt into endpoint box "{b.label}"',
                        at, c.axes, key=("C5e", c.id, b.id))
                continue
            if s_in or e_in:
                xs = [x for x in boundary_crossings(c.pts, b.rect)
                      if math.hypot(x[0] - s[0], x[1] - s[1]) > tol and math.hypot(x[0] - e[0], x[1] - e[1]) > tol]
                if xs:
                    sev = "WARN" if opts.allow_parent_entry else "FAIL"
                    add(sev, "LINE_CROSSES_BORDER",
                        f'{c.desc} crosses the border of container "{b.label}" (only one endpoint inside)',
                        xs[0], c.axes, key=("C5b", c.id, b.id))
                continue
            if inner_len > 0.5:
                add("FAIL", "LINE_THROUGH_CONTAINER", f'{c.desc} passes through non-endpoint box "{b.label}"', at,
                    c.axes, key=("C5c", c.id, b.id))

    # ---- C5b connector crossings
    for i, a in enumerate(diag):
        for b in diag[i + 1:]:
            if a.axes is not b.axes:
                continue
            hit = None
            for p1, p2 in zip(a.pts[:-1], a.pts[1:]):
                for q1, q2 in zip(b.pts[:-1], b.pts[1:]):
                    x = segments_cross(p1, p2, q1, q2)
                    if x and min(math.hypot(x[0] - p[0], x[1] - p[1]) for p in (a.pts[0], a.pts[-1], b.pts[0], b.pts[-1])) > tol:
                        hit = x
                        break
                if hit:
                    break
            if hit:
                add("WARN", "LINE_CROSSING", f"{a.desc} crosses {b.desc}", hit, a.axes, key=("C5x", a.id, b.id))

    # ---- dangling arrow tips
    for c in diag:
        if not c.arrow:
            continue
        tip = c.pts[-1]
        near_box = any(dist_to_boundary(tip, b.rect) <= tol for b in diag_boxes)
        near_text = any(dist_to_boundary(tip, inflate(t.rect, tol)) <= tol or point_strictly_inside(tip, inflate(t.rect, tol), 0)
                        for t in texts)
        near_line = any(o is not c and any(dist_to_boundary(tip, (min(p[0], q[0]), min(p[1], q[1]), max(p[0], q[0]), max(p[1], q[1]))) <= tol
                                           for p, q in zip(o.pts[:-1], o.pts[1:])) for o in diag)
        if not (near_box or near_text or near_line):
            add("WARN", "DANGLING_ARROW", f"arrow tip of {c.desc} touches nothing", tip, c.axes, key=("C7", c.id))

    # ---- legends
    for lrect, ax in legends:
        for c in connectors:
            if c.diagram or c.axes is not ax:
                continue
            L, at = polyline_in_rect(c.pts, lrect)
            if L > 1.0:
                add("WARN", "LEGEND_OVER_DATA", f"legend box covers {c.desc}", at, ax, key=("C8", id(lrect), c.id))
        for b in containers:
            if b.data_axes and b.axes is ax and rects_intersect(lrect, b.rect):
                ov = overlap_rect(lrect, b.rect)
                add("WARN", "LEGEND_OVER_DATA", "legend box covers a bar/patch", center(ov), ax,
                    key=("C8b", id(lrect), b.id))
    return F


# ---------------------------------------------------------------- matplotlib backend
def _visible_color(c) -> bool:
    if c is None:
        return False
    if isinstance(c, str):
        return c.lower() not in ("none", "")
    try:
        return len(c) < 4 or c[3] > 0.05
    except TypeError:
        return True


def audit_matplotlib_figure(fig, name: str = "figure", opts: Optional[Options] = None, tight: bool = False) -> List[Finding]:
    import numpy as np
    from matplotlib.patches import FancyArrowPatch, FancyArrow, Patch, Shadow
    from matplotlib.text import Annotation, Text
    from matplotlib.collections import LineCollection

    opts = opts or Options()
    fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    k = 72.0 / fig.dpi  # px -> pt

    def bb_rect(bb) -> Rect:
        return (bb.x0 * k, bb.y0 * k, bb.x1 * k, bb.y1 * k)

    texts: List[TextItem] = []
    containers: List[Container] = []
    connectors: List[Connector] = []
    legends: List[Tuple[Rect, object]] = []
    counter = [0]

    def nid() -> int:
        counter[0] += 1
        return counter[0]

    def add_conn_from_path(path_px, ax, diagram, arrow, desc_hint="") -> List[int]:
        ids = []
        polys = path_px.to_polygons(closed_only=False)
        if not polys:
            return ids
        polys = [np.asarray(p) * k for p in polys if len(p) >= 2]
        if not polys:
            return ids
        shaft = polys[0]
        pts = [tuple(map(float, p)) for p in shaft if np.all(np.isfinite(p))]
        # collapse duplicate consecutive points
        clean = [pts[0]] if pts else []
        for p in pts[1:]:
            if math.hypot(p[0] - clean[-1][0], p[1] - clean[-1][1]) > 1e-6:
                clean.append(p)
        if len(clean) < 2:
            return ids
        if arrow and len(polys) > 1:
            allv = np.vstack(polys)
            p_end, p_prev = np.array(clean[-1]), np.array(clean[-2])
            d = p_end - p_prev
            n = np.linalg.norm(d)
            if n > 0:
                d = d / n
                proj = (allv - p_end) @ d
                j = int(np.argmax(proj))
                if proj[j] > 0.2:
                    clean.append(tuple(map(float, allv[j])))
            p_st, p_nx = np.array(clean[0]), np.array(clean[1])
            d0 = p_st - p_nx
            n0 = np.linalg.norm(d0)
            if n0 > 0:
                d0 = d0 / n0
                proj0 = (allv - p_st) @ d0
                j0 = int(np.argmax(proj0))
                if proj0[j0] > 0.2:
                    clean.insert(0, tuple(map(float, allv[j0])))
        cid = nid()
        connectors.append(Connector(cid, clean, arrow=arrow, diagram=diagram, axes=ax, desc=desc_hint))
        ids.append(cid)
        return ids

    def describe(ax, pts_pt, arrow) -> str:
        kind = "arrow" if arrow else "line"
        if ax is None:
            return kind
        inv = ax.transData.inverted()
        a = inv.transform((pts_pt[0][0] / k, pts_pt[0][1] / k))
        b = inv.transform((pts_pt[-1][0] / k, pts_pt[-1][1] / k))
        return f"{kind}({a[0]:.3g},{a[1]:.3g})->({b[0]:.3g},{b[1]:.3g})"

    def add_text(t, kind, ax):
        if not t.get_visible():
            return None
        s = t.get_text()
        if not s or not s.strip():
            return None
        try:
            bb = t.get_window_extent(renderer)
        except Exception:
            return None
        r = bb_rect(bb)
        masked = False
        bp = t.get_bbox_patch()
        if bp is not None:
            try:
                r2 = bb_rect(bp.get_window_extent(renderer))
                r = (min(r[0], r2[0]), min(r[1], r2[1]), max(r[2], r2[2]), max(r[3], r2[3]))
                masked = _visible_color(bp.get_facecolor())
            except Exception:
                pass
        item = TextItem(nid(), s, r, kind=kind, masked=masked, axes=ax)
        texts.append(item)
        return item

    axes_list = list(fig.axes)
    for ax in axes_list:
        diagram = not ax.axison
        # texts
        for t in ax.texts:
            item = add_text(t, "label", ax)
            if isinstance(t, Annotation) and t.arrow_patch is not None and t.arrow_patch.get_visible():
                ap = t.arrow_patch
                path = ap.get_transform().transform_path(ap.get_path())
                ids = add_conn_from_path(path, ax, True if diagram else False, True)
                if item is not None:
                    item.own_connectors.update(ids)
        if not diagram:
            for t in (ax.title, ax._left_title, ax._right_title):
                add_text(t, "title", ax)
            add_text(ax.xaxis.label, "axis", ax)
            add_text(ax.yaxis.label, "axis", ax)
            for axis in (ax.xaxis, ax.yaxis):
                try:
                    ticks = axis._update_ticks()  # only ticks inside the view interval are drawn
                except Exception:
                    ticks = axis.get_major_ticks()
                for tk in ticks:
                    for tl in (tk.label1, tk.label2):
                        add_text(tl, "tick", ax)
            off = ax.yaxis.get_offset_text()
            add_text(off, "tick", ax)
        else:
            for t in (ax.title, ax._left_title, ax._right_title):
                add_text(t, "title", ax)
        leg = ax.get_legend()
        if leg is not None and leg.get_visible():
            legends.append((bb_rect(leg.get_window_extent(renderer)), ax))
            for t in leg.get_texts():
                add_text(t, "legend", ax)
            if leg.get_title() is not None:
                add_text(leg.get_title(), "legend", ax)
        # patches
        for p in ax.patches:
            if not p.get_visible() or isinstance(p, Shadow):
                continue
            if isinstance(p, FancyArrowPatch):
                path = p.get_transform().transform_path(p.get_path())
                add_conn_from_path(path, ax, diagram or True, True)
                continue
            if isinstance(p, FancyArrow):
                x, y, dx, dy = (getattr(p, a, None) for a in ("_x", "_y", "_dx", "_dy"))
                if None not in (x, y, dx, dy):
                    tr = p.get_transform()
                    a = tr.transform((x, y)) * k
                    b = tr.transform((x + dx, y + dy)) * k
                    cid = nid()
                    connectors.append(Connector(cid, [tuple(a), tuple(b)], arrow=True, diagram=True, axes=ax))
                continue
            edge = _visible_color(p.get_edgecolor()) and p.get_linewidth() > 0
            face = p.get_fill() and _visible_color(p.get_facecolor())
            if not (edge or face):
                continue
            try:
                r = bb_rect(p.get_window_extent(renderer))
            except Exception:
                continue
            if min(rect_w(r), rect_h(r)) < (opts.min_container if diagram else 0.3):
                continue
            containers.append(Container(nid(), r, axes=ax, data_axes=not diagram))
        # lines
        for ln in ax.lines:
            if not ln.get_visible() or ln.get_linestyle() in ("None", "none", "", " "):
                continue
            xy = ln.get_xydata()
            if xy is None or len(xy) < 2:
                continue
            disp = ln.get_transform().transform(np.asarray(xy, dtype=float)) * k
            run: List[Point] = []
            pieces = []
            for v in disp:
                if np.all(np.isfinite(v)):
                    run.append((float(v[0]), float(v[1])))
                else:
                    if len(run) >= 2:
                        pieces.append(run)
                    run = []
            if len(run) >= 2:
                pieces.append(run)
            for pc in pieces:
                connectors.append(Connector(nid(), pc, arrow=False, diagram=diagram, axes=ax))
        for coll in ax.collections:
            if isinstance(coll, LineCollection) and coll.get_visible():
                tr = coll.get_transform()
                for seg in coll.get_segments():
                    if len(seg) >= 2:
                        d = tr.transform(np.asarray(seg, dtype=float)) * k
                        connectors.append(Connector(nid(), [tuple(map(float, v)) for v in d], diagram=diagram, axes=ax))
    # figure-level artists
    for t in fig.texts:
        add_text(t, "label", None)
    if getattr(fig, "_suptitle", None) is not None:
        add_text(fig._suptitle, "title", None)
    for leg in fig.legends:
        legends.append((bb_rect(leg.get_window_extent(renderer)), None))
        for t in leg.get_texts():
            add_text(t, "legend", None)
    for c in connectors:
        if not c.desc:
            c.desc = describe(c.axes, c.pts, c.arrow)

    canvas = (0.0, 0.0, fig.bbox.width * k, fig.bbox.height * k)

    def to_data(ax, at):
        try:
            v = ax.transData.inverted().transform((at[0] / k, at[1] / k))
            return (float(v[0]), float(v[1]))
        except Exception:
            return None

    return run_checks(name, texts, containers, connectors, canvas, opts, tight=tight, legends=legends, to_data=to_data,
                      describe=lambda c: describe(c.axes, c.pts, c.arrow))


# ---------------------------------------------------------------- PDF backend
def audit_pdf(path: str, page_no: int = 0, opts: Optional[Options] = None) -> List[Finding]:
    import fitz  # PyMuPDF

    opts = opts or Options()
    doc = fitz.open(path)
    page = doc[page_no]
    H = page.rect.height
    W = page.rect.width

    def flip_rect(x0, y0, x1, y1) -> Rect:
        return (x0, H - y1, x1, H - y0)

    texts: List[TextItem] = []
    containers: List[Container] = []
    connectors: List[Connector] = []
    masks: List[Tuple[Rect, int]] = []
    heads: List[Tuple[Rect, List[Point]]] = []
    counter = [0]

    def nid():
        counter[0] += 1
        return counter[0]

    d = page.get_text("rawdict")
    for block in d.get("blocks", []):
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue
            xs0, ys0, xs1, ys1, s = [], [], [], [], ""
            for sp in spans:
                chars = sp.get("chars", [])
                txt = "".join(ch.get("c", "") for ch in chars)
                if not txt.strip():
                    continue
                size = sp.get("size", 8.0)
                ox, oy = sp.get("origin", (sp["bbox"][0], sp["bbox"][3]))
                x0, x1 = sp["bbox"][0], sp["bbox"][2]
                # tighten vertical extent to ink-ish box around the baseline
                xs0.append(x0); xs1.append(x1)
                ys0.append(oy - 0.72 * size); ys1.append(oy + 0.22 * size)
                s += txt
            if s.strip():
                texts.append(TextItem(nid(), s, flip_rect(min(xs0), min(ys0), max(xs1), max(ys1))))

    def bezier(p0, p1, p2, p3, n=8):
        out = []
        for i in range(n + 1):
            t = i / n
            mt = 1 - t
            out.append((mt ** 3 * p0.x + 3 * mt * mt * t * p1.x + 3 * mt * t * t * p2.x + t ** 3 * p3.x,
                        mt ** 3 * p0.y + 3 * mt * mt * t * p1.y + 3 * mt * t * t * p2.y + t ** 3 * p3.y))
        return out

    for dr in page.get_drawings():
        r = dr.get("rect")
        if r is None:
            continue
        rect = flip_rect(r.x0, r.y0, r.x1, r.y1)
        typ = dr.get("type", "")
        stroke = "s" in typ and dr.get("color") is not None
        fill = dr.get("fill")
        seq = dr.get("seqno", 0)
        if rect_w(rect) >= 0.9 * W and rect_h(rect) >= 0.9 * H:
            continue  # page background
        # flatten into subpaths
        subpaths: List[List[Point]] = []
        cur: List[Point] = []
        closed_shape = bool(dr.get("closePath"))
        for it in dr["items"]:
            op = it[0]
            if op == "l":
                a, b = it[1], it[2]
                pa, pb = (a.x, H - a.y), (b.x, H - b.y)
                if cur and math.hypot(cur[-1][0] - pa[0], cur[-1][1] - pa[1]) < 0.01:
                    cur.append(pb)
                else:
                    if len(cur) >= 2:
                        subpaths.append(cur)
                    cur = [pa, pb]
            elif op == "c":
                pts = [(x, H - y) for x, y in bezier(it[1], it[2], it[3], it[4])]
                if cur and math.hypot(cur[-1][0] - pts[0][0], cur[-1][1] - pts[0][1]) < 0.01:
                    cur.extend(pts[1:])
                else:
                    if len(cur) >= 2:
                        subpaths.append(cur)
                    cur = pts
            elif op in ("re", "qu"):
                closed_shape = True
        if len(cur) >= 2:
            subpaths.append(cur)
        if subpaths and not closed_shape:
            # closed if every subpath returns to its start
            closed_shape = all(math.hypot(sp[0][0] - sp[-1][0], sp[0][1] - sp[-1][1]) < 0.5 for sp in subpaths)
        is_white = fill is not None and min(fill) > 0.97
        small = max(rect_w(rect), rect_h(rect)) < 8.0
        has_curve = any(it[0] == "c" for it in dr["items"])
        if closed_shape:
            if small and fill is not None and not is_white and not has_curve:
                heads.append((rect, [p for sp in subpaths for p in sp]))
                continue
            if small:
                continue  # dots, markers, badges: decoration, not containers
            if fill is not None and is_white and not stroke:
                masks.append((rect, seq))
                continue
            if min(rect_w(rect), rect_h(rect)) >= opts.min_container and (stroke or (fill is not None and not is_white)):
                containers.append(Container(nid(), rect))
            continue
        if stroke:
            for sp in subpaths:
                connectors.append(Connector(nid(), sp, arrow=False, diagram=True, seqno=seq))

    # attach arrowheads to the nearest connector end
    for hrect, hpts in heads:
        best = None
        for c in connectors:
            for end in (0, -1):
                dd = dist_to_boundary(c.pts[end], inflate(hrect, 0.5))
                if dd <= 1.5 and (best is None or dd < best[0]):
                    best = (dd, c, end)
        if best:
            _, c, end = best
            c.arrow = True
            ref = c.pts[end]
            other = c.pts[1] if end == 0 else c.pts[-2]
            dx, dy = ref[0] - other[0], ref[1] - other[1]
            n = math.hypot(dx, dy) or 1.0
            tip = max(hpts, key=lambda p: (p[0] - ref[0]) * dx / n + (p[1] - ref[1]) * dy / n)
            if end == 0:
                c.pts.insert(0, tip)
                c.pts.reverse()  # keep the head at the end
            else:
                c.pts.append(tip)
    # masked labels
    for t in texts:
        for mrect, mseq in masks:
            if rect_inside(t.rect, inflate(mrect, 0.5)):
                t.masked = True
    canvas = (0.0, 0.0, W, H)
    return run_checks(os.path.basename(path) + (f"#p{page_no + 1}" if page_no else ""), texts, containers,
                      connectors, canvas, opts, tight=True)


# ---------------------------------------------------------------- CLI
def report(findings: List[Finding], quiet: bool = False) -> Tuple[int, int]:
    nf = sum(1 for f in findings if f.severity == "FAIL")
    nw = sum(1 for f in findings if f.severity == "WARN")
    for f in findings:
        if quiet and f.severity != "FAIL":
            continue
        print(f.line())
    return nf, nw


def cmd_run(args, opts: Options) -> int:
    import matplotlib
    matplotlib.use("Agg")
    from matplotlib.figure import Figure

    script = os.path.abspath(args.script)
    orig_savefig = Figure.savefig
    all_findings: Dict[str, List[Finding]] = {}
    audited = set()

    def hooked(self, fname, *a, **kw):
        label = os.path.basename(str(fname)) if not hasattr(fname, "write") else "<buffer>"
        if not args.match or any(m in str(fname) for m in args.match):
            key = (id(self), os.path.splitext(label)[0])
            if key not in audited:
                audited.add(key)
                tight = kw.get("bbox_inches") == "tight"
                all_findings[label] = audit_matplotlib_figure(self, name=label, opts=opts, tight=tight)
        if args.no_save:
            return None
        if args.out_dir and not hasattr(fname, "write"):
            os.makedirs(args.out_dir, exist_ok=True)
            fname = os.path.join(args.out_dir, os.path.basename(str(fname)))
        return orig_savefig(self, fname, *a, **kw)

    Figure.savefig = hooked
    old_argv = sys.argv
    sys.argv = [script] + list(args.script_args or [])
    sys.path.insert(0, os.path.dirname(script))
    try:
        runpy.run_path(script, run_name="__main__")
    finally:
        sys.argv = old_argv
        Figure.savefig = orig_savefig
    return summarize(all_findings, args)


def summarize(all_findings: Dict[str, List[Finding]], args) -> int:
    total_f = total_w = 0
    if not all_findings:
        print("no figure matched / audited", file=sys.stderr)
        return 2
    for name, fs in all_findings.items():
        print(f"== {name}")
        nf, nw = report(fs, quiet=args.quiet)
        print(f"   -> {nf} FAIL, {nw} WARN")
        total_f += nf
        total_w += nw
    print(f"TOTAL: {total_f} FAIL, {total_w} WARN over {len(all_findings)} figure(s)")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({k: [f.__dict__ for f in v] for k, v in all_findings.items()}, fh, indent=1)
    return 1 if total_f else 0


def cmd_pdf(args, opts: Options) -> int:
    res = {}
    import fitz
    for p in args.pdfs:
        n = len(fitz.open(p))
        pages = [args.page - 1] if args.page else range(n)
        for i in pages:
            res[os.path.basename(p) + (f"#p{i + 1}" if n > 1 else "")] = audit_pdf(p, i, opts)
    return summarize(res, args)


def cmd_selftest(opts: Options) -> int:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch

    def box(ax, x, y, w, h, **kw):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.01", fc="white", ec="k", lw=0.8, **kw))

    # broken: arrow through a foreign box and a container title, label on line, label on border
    fig, ax = plt.subplots(figsize=(4, 2.4))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    box(ax, 0.05, 0.05, 0.9, 0.6)
    ax.text(0.07, 0.62, "Container title", va="top", fontsize=8, fontweight="bold")
    box(ax, 0.10, 0.15, 0.2, 0.25); ax.text(0.2, 0.275, "A", ha="center", va="center", fontsize=8)
    box(ax, 0.40, 0.15, 0.2, 0.25); ax.text(0.5, 0.275, "B", ha="center", va="center", fontsize=8)
    box(ax, 0.70, 0.15, 0.2, 0.25); ax.text(0.8, 0.275, "C", ha="center", va="center", fontsize=8)
    ax.annotate("", xy=(0.70, 0.30), xytext=(0.30, 0.30), arrowprops=dict(arrowstyle="-|>", shrinkA=0, shrinkB=0))  # through B
    ax.annotate("", xy=(0.2, 0.40), xytext=(0.2, 0.90), arrowprops=dict(arrowstyle="-|>", shrinkA=0, shrinkB=0))  # through title
    ax.text(0.5, 0.30, "on line", ha="center", va="center", fontsize=7)
    ax.text(0.95, 0.5, "on border", ha="center", va="center", fontsize=7)
    bad = audit_matplotlib_figure(fig, "selftest_broken", opts)
    plt.close(fig)
    codes = {f.code for f in bad if f.severity == "FAIL"}
    need = {"LINE_THROUGH_CONTAINER", "LINE_THROUGH_TITLE", "TEXT_ON_LINE", "TEXT_ON_BORDER", "LINE_CROSSES_BORDER"}
    print("broken figure findings:")
    report(bad)
    ok1 = need <= codes
    # clean
    fig, ax = plt.subplots(figsize=(4, 2.4))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    box(ax, 0.05, 0.25, 0.25, 0.3); ax.text(0.175, 0.4, "Source", ha="center", va="center", fontsize=8)
    box(ax, 0.70, 0.25, 0.25, 0.3); ax.text(0.825, 0.4, "Target", ha="center", va="center", fontsize=8)
    ax.annotate("", xy=(0.70, 0.40), xytext=(0.30, 0.40), arrowprops=dict(arrowstyle="-|>", shrinkA=0, shrinkB=0))
    ax.text(0.5, 0.45, "request", ha="center", va="bottom", fontsize=7)
    good = audit_matplotlib_figure(fig, "selftest_clean", opts)
    plt.close(fig)
    print("clean figure findings:")
    report(good)
    ok2 = not any(f.severity == "FAIL" for f in good)
    print(f"selftest: broken-detected={ok1} (missing: {sorted(need - codes)}), clean-passes={ok2}")
    return 0 if (ok1 and ok2) else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--clearance", type=float, default=2.0, help="min text clearance in pt (default 2)")
    ap.add_argument("--endpoint-tol", type=float, default=3.0, help="arrow endpoint tolerance in pt (default 3)")
    ap.add_argument("--junction-tol", type=float, default=2.5, help="chain polyline pieces closer than this (pt)")
    ap.add_argument("--strict", action="store_true", help="treat every WARN as FAIL")
    ap.add_argument("--allow-parent-entry", action="store_true",
                    help="arrows may cross into a container to reach a child box (WARN instead of FAIL)")
    ap.add_argument("--quiet", action="store_true", help="print FAIL lines only")
    ap.add_argument("--json", help="write findings to this JSON file")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run", help="run a matplotlib script with savefig hooked")
    r.add_argument("script")
    r.add_argument("--match", action="append", help="only audit save paths containing this substring")
    r.add_argument("--no-save", action="store_true", help="audit only, do not write figure files")
    r.add_argument("--out-dir", help="redirect every savefig() to this directory (protects hard-coded output paths)")
    p = sub.add_parser("pdf", help="audit vector PDF figure(s)")
    p.add_argument("pdfs", nargs="+")
    p.add_argument("--page", type=int, default=0, help="1-based page (default: all pages)")
    sub.add_parser("selftest", help="verify the detector on synthetic figures")
    argv = list(sys.argv[1:] if argv is None else argv)
    script_args: List[str] = []
    if "--" in argv:  # everything after a bare -- is passed to the audited script
        i = argv.index("--")
        argv, script_args = argv[:i], argv[i + 1:]
    args = ap.parse_args(argv)
    args.script_args = script_args
    opts = Options(clearance=args.clearance, endpoint_tol=args.endpoint_tol, junction_tol=args.junction_tol,
                   strict=args.strict, allow_parent_entry=args.allow_parent_entry)
    try:
        if args.cmd == "run":
            return cmd_run(args, opts)
        if args.cmd == "pdf":
            return cmd_pdf(args, opts)
        return cmd_selftest(opts)
    except SystemExit as e:  # script called sys.exit
        raise
    except Exception as e:  # pragma: no cover
        import traceback
        traceback.print_exc()
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
