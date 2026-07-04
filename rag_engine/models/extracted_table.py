from dataclasses import dataclass
import pandas as pd


@dataclass(slots=True)
class ExtractedTable:
    """
    Représente un tableau extrait d'un PDF.
    """

    dataframe: pd.DataFrame
    page: int