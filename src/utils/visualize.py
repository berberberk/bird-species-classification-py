import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def plot_sample_images(df: pd.DataFrame, n: int = 9) -> None:
    """
    Plots sample images from dataframe
    :param df: Dataframe with bird species images (contains 'Path' and 'Species' columns)
    :param n: Number of images to be plotted
    :return:
    """
    random_index = np.random.randint(0, len(df), n)
    nrows = int(n ** 0.5)
    ncols = n // nrows
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10, 10),
                            subplot_kw={'xticks': [], 'yticks': []})
    for i, ax in enumerate(axes.flat):
        ax.imshow(plt.imread(df['Path'][random_index[i]]))
        ax.set_title(df['Species'][random_index[i]])
    plt.tight_layout()
    plt.show()
    plt.savefig(Path('..') / 'plots' / 'images_sample.png')