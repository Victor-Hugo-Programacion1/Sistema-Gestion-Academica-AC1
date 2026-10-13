from models.persona import Persona


class Administrativo(Persona):

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        numero_empleado,
        dependencia,
        cargo,
        jornada
    ):

        super().__init__(
            identificacion,
            nombre,
            correo
        )

        self.numero_empleado = numero_empleado
        self.dependencia = dependencia
        self.cargo = cargo
        self.jornada = jornada