"""
Pipeline de transformaciones.
"""


class Pipeline:

    def __init__(self, pasos):

        self.pasos = pasos

    def ejecutar(self, df):

        resultado = df.copy()

        for paso in self.pasos:

            paso.ajustar(resultado)

            resultado = paso.transformar(resultado)

        return resultado
