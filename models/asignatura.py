class Asignatura:

    def __init__(
        self,
        codigo,
        nombre,
        creditos,
        programa_academico
    ):

        self.codigo = codigo
        self.nombre = nombre

        self.set_creditos(
            creditos
        )

        self.programa_academico = programa_academico

    def get_creditos(self):
        return self.creditos

    def set_creditos(
        self,
        creditos
    ):

        if creditos > 0:
            self.creditos = creditos

        else:
            raise ValueError(
                "Los créditos deben ser mayores que cero"
            )