"""
Environment variables and functions for the project.
"""

import pandas as pd
import random

# Map of German literary movements
MOVEMENT_MAP = {
    (1050, 1350): "Middle High German",
    (1351, 1600): "Late Medieval/Early Modern",
    (1601, 1720): "Baroque",
    (1721, 1780): "Enlightenment",
    (1765, 1785): "Sturm und Drang",
    (1786, 1805): "Weimar Classicism",
    (1795, 1840): "Romanticism",
    (1841, 1900): "Realism/Naturalism",
    (1901, 1945): "Expressionism/Modernism",
}


def get_period(year: int) -> str:
    for (start, end), period in MOVEMENT_MAP.items():
        if start <= year <= end:
            return period
    return "Unknown"


def data_augment(
    x_train: pd.Series, y_train: pd.Series, words_per_line: int = 6, seed: int = None
) -> pd.DataFrame:
    """
    Shuffle poems within label groups and shuffle lines within each poem.
    Example: Poems from the same century will have their lined shuffled.

    WARNING: df must not be encoded (tfidf or word2vec)
    Apply this function on x_train and y_train, then encode the data.

    Parameters:
    - x_train: pd.Series of text data
    - y_train: pd.Series of corresponding labels
    - words_per_line: number of words per line
    - seed: random seed for reproducibility

    Returns:
    - Tuple[pd.Series, pd.Series]: shuffled text and labels
    """
    random.seed(seed)

    df = pd.DataFrame({"text": x_train, "label": y_train})

    def split_and_shuffle_lines(text):
        words = text.split()
        lines = [
            " ".join(words[i : i + words_per_line])
            for i in range(0, len(words), words_per_line)
        ]
        random.shuffle(lines)
        return " ".join(lines)

    x_new = []
    y_new = []

    for label, group in df.groupby("label"):
        group_shuffled = group.sample(frac=1, random_state=seed)
        for _, row in group_shuffled.iterrows():
            if label == "13" or label == "14" or label == "11" or label == "16":
                shuffled_text = split_and_shuffle_lines(row["text"])
                x_new.append(shuffled_text)
                y_new.append(row["label"])

    return pd.Series(x_new), pd.Series(y_new)
