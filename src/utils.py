from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"


def set_plot_style():
    sns.set_theme(style="whitegrid")
    plt.rcParams["figure.figsize"] = (8, 5)
