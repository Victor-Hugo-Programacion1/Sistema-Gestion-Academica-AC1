from models.persona import Persona


class Docente(Persona):

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        numero_empleado,
        facultad,
        tipo_contratacion,
        horas_semanales
    ):

        super().__init__(
            identificacion,
            nombre,
            correo
        )

        self.numero_empleado = numero_empleado
        self.facultad = facultad
        self.tipo_contratacion = tipo_contratacion
        self.horas_semanales = horas_semanales
