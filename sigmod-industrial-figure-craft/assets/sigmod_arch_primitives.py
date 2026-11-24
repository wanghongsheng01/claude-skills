"""Reusable vector drawing primitives for SIGMOD Industrial Track architecture diagrams.

Design principles (grounded in sigmod-industrial-figure-craft):
- Restrained palette: 80% neutral slate/gray infrastructure, 1 primary hero navy, 1 warm control tint,
  and semantic-only status accents (teal = certified/pass, vermilion = blocked/diagnostic).
- Distinct vector ontologies: database cylinders, header-band zones, decision diamonds,
  compact chips, dual-track step badges (circled offline vs. filled-square/circle online).
- Clean sans-serif inside schematics (7.0-8.5pt printed at 7.0 in full width), generous padding.
"""
from __future__ import annotations
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Ellipse, Circle, Rectangle

PALETTE = {
    # Hero contribution (Primary Navy)
    'hero_dark':   '#0B4F8C',
    'hero_mid':    '#1D6FA5',
    'hero_bg':     '#EDF5FC',
    'hero_chip':   '#DBEAFE',
    # Offline / Control plane (Warm Sand/Amber)
    'ctrl_dark':   '#92400E',
    'ctrl_edge':   '#D97706',
    'ctrl_bg':     '#FFFBF2',
    # Commodity Infrastructure (Muted Slate/Gray)
    'infra_dark':  '#334155',
    'infra_edge':  '#94A3B8',
    'infra_bg':    '#F8FAFC',
    'infra_card':  '#FFFFFF',
    # Semantic status accents (strictly for pass/refusal outcomes)
    'ok_dark':     '#0F766E',
    'ok_edge':     '#0D9488',
    'ok_bg':       '#ECFDF5',
    'warn_dark':   '#9A3412',
    'warn_edge':   '#C2410C',
    'warn_bg':     '#FFF7ED',
    # Text
    'text':        '#0F172A',
    'muted':       '#475569',
}


def draw_zone(ax, x, y, w, h, title, bg, edge, header_bg=None, header_fg='#FFFFFF',
              header_h=3.4, lw=1.0, title_fs=7.6, ls='-', r=0.8):
    """Draw a clean architectural zone with an optional crisp header strip (FinSQL / Palimpzest style)."""
    outer = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0.1,rounding_size={r}',
                           facecolor=bg, edgecolor=edge, linewidth=lw, linestyle=ls, zorder=1)
    ax.add_patch(outer)
    if header_bg:
        hdr = FancyBboxPatch((x, y + h - header_h), w, header_h,
                             boxstyle=f'round,pad=0.1,rounding_size={r}',
                             facecolor=header_bg, edgecolor=edge, linewidth=lw, zorder=2)
        ax.add_patch(hdr)
        ax.text(x + w / 2, y + h - header_h / 2, title, ha='center', va='center',
                fontsize=title_fs, fontweight='bold', color=header_fg, zorder=3)
    elif title:
        ax.text(x + 1.2, y + h - 1.1, title, ha='left', va='top',
                fontsize=title_fs, fontweight='bold', color=edge, zorder=3)


def draw_card(ax, x, y, w, h, title, body='', fc='#FFFFFF', ec='#94A3B8', lw=0.85,
              title_c='#0F172A', body_c='#334155', title_fs=7.2, body_fs=6.3, r=0.6, z=3):
    """Draw a clean component box with balanced top/bottom breathing room."""
    p = FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0.08,rounding_size={r}',
                       facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z)
    ax.add_patch(p)
    if body:
        ax.text(x + w / 2, y + h - 1.25, title, ha='center', va='top',
                fontsize=title_fs, fontweight='bold', color=title_c, zorder=z + 1)
        ax.text(x + w / 2, y + (h - 2.3) / 2, body, ha='center', va='center',
                fontsize=body_fs, color=body_c, linespacing=1.24, zorder=z + 1)
    else:
        ax.text(x + w / 2, y + h / 2, title, ha='center', va='center',
                fontsize=title_fs, fontweight='bold', color=title_c, zorder=z + 1)


def draw_cylinder(ax, x, y, w, h, title, body='', fc='#FFFFFF', top_fc='#E2E8F0',
                  ec='#64748B', title_c='#0F172A', body_c='#475569',
                  title_fs=7.0, body_fs=6.0, lw=0.95, z=3):
    """Draw a crisp vector database / cache cylinder."""
    eh = min(2.0, h * 0.22)
    # Bottom ellipse
    bot = Ellipse((x + w / 2, y + eh / 2), w, eh, facecolor=fc, edgecolor=ec, lw=lw, zorder=z)
    ax.add_patch(bot)
    # Body rectangle
    rect = Rectangle((x, y + eh / 2), w, h - eh, facecolor=fc, edgecolor='none', zorder=z)
    ax.add_patch(rect)
    # Side walls
    ax.plot([x, x], [y + eh / 2, y + h - eh / 2], color=ec, lw=lw, zorder=z + 1)
    ax.plot([x + w, x + w], [y + eh / 2, y + h - eh / 2], color=ec, lw=lw, zorder=z + 1)
    # Top ellipse
    top = Ellipse((x + w / 2, y + h - eh / 2), w, eh, facecolor=top_fc, edgecolor=ec, lw=lw, zorder=z + 2)
    ax.add_patch(top)
    cy = y + (h - eh) / 2
    if body:
        ax.text(x + w / 2, cy + 1.15, title, ha='center', va='center',
                fontsize=title_fs, fontweight='bold', color=title_c, zorder=z + 3)
        ax.text(x + w / 2, cy - 1.25, body, ha='center', va='center',
                fontsize=body_fs, color=body_c, linespacing=1.18, zorder=z + 3)
    else:
        ax.text(x + w / 2, cy, title, ha='center', va='center',
                fontsize=title_fs, fontweight='bold', color=title_c, zorder=z + 3)


def draw_diamond(ax, cx, cy, rx, ry, text, fc='#EDF5FC', ec='#0B4F8C',
                 tc='#0B4F8C', fs=6.5, lw=1.0, z=4):
    """Draw a decision / certification gate diamond."""
    pts = [(cx, cy + ry), (cx + rx, cy), (cx, cy - ry), (cx - rx, cy)]
    poly = Polygon(pts, closed=True, facecolor=fc, edgecolor=ec, linewidth=lw, zorder=z)
    ax.add_patch(poly)
    ax.text(cx, cy, text, ha='center', va='center', fontsize=fs, fontweight='bold',
            color=tc, linespacing=1.12, zorder=z + 1)


def draw_badge(ax, cx, cy, label, kind='online', r=1.15, fs=6.4, z=6):
    """Draw dual-track step badge: 'online' = navy filled square/circle, 'offline' = amber outlined circle."""
    if kind == 'offline':
        c = Circle((cx, cy), r, facecolor='#FFFBEB', edgecolor='#B45309', lw=0.95, zorder=z)
        ax.add_patch(c)
        ax.text(cx, cy, str(label), ha='center', va='center', fontsize=fs,
                fontweight='bold', color='#92400E', zorder=z + 1)
    else:
        b = FancyBboxPatch((cx - r, cy - r), 2 * r, 2 * r,
                           boxstyle='round,pad=0.05,rounding_size=0.35',
                           facecolor='#0B4F8C', edgecolor='#0B4F8C', lw=0.8, zorder=z)
        ax.add_patch(b)
        ax.text(cx, cy, str(label), ha='center', va='center', fontsize=fs,
                fontweight='bold', color='#FFFFFF', zorder=z + 1)


def draw_ortho_arrow(ax, pts, color='#334155', lw=1.0, ls='-', z=4):
    """Draw a clean orthogonal polyline ending in a crisp arrowhead."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    if len(pts) > 2:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, linestyle=ls, solid_capstyle='butt', zorder=z)
    ax.annotate('', xy=pts[-1], xytext=pts[-2],
                arrowprops=dict(arrowstyle='-|>', color=color, lw=lw, linestyle=ls,
                                mutation_scale=8.5, shrinkA=0, shrinkB=0), zorder=z + 1)
