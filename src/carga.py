from pathlib import Path
import pandas as pd


def cargar_dataset():

    ruta = (
        Path(__file__)
        .parent
        .parent
        / "data"
        / "y-combinator-companies.csv"
    )

    return pd.read_csv(ruta)
