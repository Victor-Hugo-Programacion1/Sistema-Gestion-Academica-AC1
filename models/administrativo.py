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
        
    def mostrar_informacion(self):

        return (
            "=== ADMINISTRATIVO ===\n\n"
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Número Empleado: {self.numero_empleado}\n"
            f"Dependencia: {self.dependencia}\n"
            f"Cargo: {self.cargo}\n"
            f"Jornada: {self.jornada}"
        )
    def realizar_actividad_principal(self):
        return (
            f"El administrativo desempeña "
            f"el cargo de {self.cargo} "
            f"en la dependencia "
            f"{self.dependencia}."
        )