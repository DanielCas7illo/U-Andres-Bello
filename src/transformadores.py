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
