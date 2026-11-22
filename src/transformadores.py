class ImputadorTeamSize(Transformador):

    def __init__(self):

        self.mediana = None

    def ajustar(self, df):

        self.mediana = (
            df["team_size"]
            .median()
        )

    def transformar(self, df):

        resultado = df.copy()

        resultado["team_size"] = (
            resultado["team_size"]
            .fillna(self.mediana)
        )

        return resultado
class ImputadorTeamSize(Transformador):

    def aprender(self, df):

        return {
            "mediana": float(
                df[self.columna].median()
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
