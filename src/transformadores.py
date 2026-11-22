"""
Transformadores para el proyecto de startups de Y Combinator.

Cada transformador implementa dos etapas:

1. ajustar():
   Aprende lo necesario del conjunto de datos.

2. transformar():
   Aplica la transformación utilizando lo aprendido.
"""

from abc import ABC, abstractmethod


class Transformador(ABC):
    """
    Clase base para todos los pasos del pipeline.
    """

    def __init__(self, columna):

        self.columna = columna
        self._parametros = {}
        self._ajustado = False

    @property
    def nombre(self):

        return f"{type(self).__name__}({self.columna})"

    @property
    def parametros(self):

        return dict(self._parametros)

    def ajustar(self, df):

        if self.columna not in df.columns:
            raise KeyError(
                f"{self.nombre}: la columna no existe."
            )

        self._parametros = self.aprender(df)

        self._ajustado = True

        return self

    def transformar(self, df):

        if not self._ajustado:
            raise RuntimeError(
                f"{self.nombre}: debe ajustarse antes de transformar."
            )

        return self.aplicar(df.copy())

    def ajustar_transformar(self, df):

        return (
            self
            .ajustar(df)
            .transformar(df)
        )

    @abstractmethod
    def aprender(self, df):
        pass

    @abstractmethod
    def aplicar(self, df):
        pass
class EliminarYCombinator(Transformador):
    """
    Elimina el registro que corresponde a Y Combinator.
    """

    def aprender(self, df):

        return {
            "filas_antes": len(df)
        }

    def aplicar(self, df):

        return df[
            df["name"] != "Y Combinator"
        ].copy()
class ImputadorTeamSize(Transformador):
    """
    Imputa valores nulos usando la mediana.
    """

    def aprender(self, df):

        return {
            "mediana": float(
                df[self.columna].median()
            ),
            "nulos": int(
                df[self.columna]
                .isna()
                .sum()
            )
        }
    def aplicar(self, df):

        df[self.columna] = (
            df[self.columna]
            .fillna(
                self._parametros["mediana"]
            )
        )

        return df
