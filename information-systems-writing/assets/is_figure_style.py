"""matplotlib defaults for Information Systems figures (plots and schematics).

Usage:
    import matplotlib as mpl
    from is_figure_style import IS_STYLE, COLORS, box
    mpl.rcParams.update(IS_STYLE)

Design at final size: in elsarticle preprint layout \\linewidth is about 5.4 in,
a full page width in the final 3p/5p layout about 7.5 in, a column about 3.5 in.
"""

IS_STYLE = {
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "font.size": 8,
    "axes.titlesize": 8.5,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "legend.frameon": False,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.6,
    "lines.linewidth": 1.2,
    "grid.linewidth": 0.4,
    "grid.color": "#DDDDDD",
    "pdf.fonttype": 42,      # embed TrueType fonts
    "ps.fonttype": 42,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
    "figure.dpi": 150,
    "savefig.dpi": 300,
}

# Colour-blind-safe (Okabe-Ito based), distinguishable in grayscale by lightness.
COLORS = {
    "ink": "#222222",        # text and outlines
    "line": "#555555",       # arrows and connectors
    "fill": "#F2F2F2",       # neutral box fill
    "accent": "#0072B2",     # the element the figure is about
    "accent_fill": "#DCEAF5",
    "warn": "#D55E00",       # failure or discrepancy
    "warn_fill": "#FBE3D6",
    "ok": "#009E73",
    "ok_fill": "#D9F0E8",
    "series": ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#E69F00", "#56B4E9", "#555555"],
}


def box(ax, x, y, w, h, text, fill=None, edge=None, weight="normal", size=None):
    """Flat rectangle with centred text (axes data coordinates)."""
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.02",
                                linewidth=0.7, edgecolor=edge or COLORS["line"],
                                facecolor=fill or COLORS["fill"]))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=size or 7.5,
            color=COLORS["ink"], fontweight=weight, linespacing=1.25)


def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", lw=0.7, color=COLORS["line"], shrinkA=0, shrinkB=0))
