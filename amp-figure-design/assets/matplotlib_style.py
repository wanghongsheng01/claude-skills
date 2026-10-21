"""
matplotlib style template for AMP / protein-generative-model paper figures.

Usage:
    import matplotlib as mpl
    from matplotlib.pyplot import cycler
    from amp_style import amp_style, ZONE_COLORS, add_panel_label
    mpl.rcParams.update(amp_style)
"""

from matplotlib.pyplot import cycler

amp_style = {
    # --- Font: sans-serif, matching Nature / Briefings in Bioinformatics ---
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 9,
    'axes.titlesize': 10,
    'axes.labelsize': 9,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,

    # --- Panel labels: bold uppercase A/B/C at upper-left (Briefings style) ---
    # Add manually with: ax.text(-0.12, 1.05, 'A', transform=ax.transAxes,
    #                          fontweight='bold', fontsize=12)

    # --- Colors: low-saturation semantic palette ---
    'axes.prop_cycle': cycler('color', [
        '#D2691E',   # ochre-terracotta (main method)
        '#4682B4',   # medium blue (comparison)
        '#808080',   # neutral gray (baseline)
        '#B2182B',   # brick red (highlight)
        '#2C7A7B',   # deep teal
        '#90BE6D',   # light green
    ]),

    # --- Figure size: double-column ~170 mm wide = 6.7 inches ---
    'figure.figsize': (6.7, 4.5),
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.05,

    # --- Axes ---
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': False,
    'axes.edgecolor': '#333333',
    'axes.labelcolor': '#222222',

    # --- Ticks ---
    'xtick.color': '#333333',
    'ytick.color': '#333333',
    'xtick.direction': 'out',
    'ytick.direction': 'out',

    # --- Legend ---
    'legend.frameon': False,
    'legend.loc': 'best',

    # --- Heatmap default colormap: blue-white-red diverging ---
    # Use with sns.heatmap(cmap='RdBu_r', center=0)
    # For sequential orange-brown: cmap='YlOrBr'
}

# --- Heatmap color scales (manual, for seaborn / matplotlib) ---
# Diverging blue-white-red (Wan 2024 Fig. 4a style):
#   sns.heatmap(data, cmap='RdBu_r', center=0, annot=True, fmt='g')
#
# Sequential orange-brown (Cell 2024 Fig. 6B/C style):
#   sns.heatmap(data, cmap='YlOrBr', annot=True, fmt='g')

# --- Schematic zone colors (for workflow diagrams) ---
ZONE_COLORS = {
    'data':    '#B8D4E8',  # light blue
    'model':   '#E8B8B8',  # light red
    'eval':    '#B8D8B8',  # light green
    'highlight': '#F5EED8',  # beige (for formula boxes)
    'extra':   '#9B7FB8',  # light purple
}

# --- Panel label helper ---
def add_panel_label(ax, label, position='upper-left'):
    """Add a bold panel label (A, B, C...) at the corner.

    For Briefings in Bioinformatics: use uppercase bold.
    For Nature family: use lowercase bold.
    """
    ax.text(-0.12, 1.05, label, transform=ax.transAxes,
            fontweight='bold', fontsize=12, va='bottom', ha='right')
