import pandas as pd
import kagglehub
from pathlib import Path


def load_cub_dataset() -> pd.DataFrame:
    """
    Loads CUB-200-2011 dataset into dataframe
    :return: Dataframe with image paths and class labels for each species
    """
    dataset_path = Path(kagglehub.dataset_download('wenewone/cub2002011')) / 'CUB_200_2011'
    df_img = pd.read_csv(dataset_path / 'images.txt', sep=' ', names=['ID', 'Image'])
    df_label = pd.read_csv(dataset_path / 'image_class_labels.txt', sep=' ', names=['ID', 'Label'])
    df = pd.merge(df_img, df_label, on='ID')
    df['Path'] = df['Image'].apply(lambda x: dataset_path / 'images' / x)
    return df
