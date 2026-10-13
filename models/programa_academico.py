class ProgramaAcademico:

    def __init__(
        self,
        codigo,
        nombre,
        facultad,
        numero_semestres
    ):

        self.codigo = codigo
        self.nombre = nombre
        self.facultad = facultad

        self.set_numero_semestres(
            numero_semestres
        )

    def get_numero_semestres(self):
        return self.numero_semestres

    def set_numero_semestres(
        self,
        numero_semestres
    ):

        if numero_semestres > 0:
            self.numero_semestres = numero_semestres

        else:
            raise ValueError(
                "El número de semestres debe ser mayor que cero"
            )