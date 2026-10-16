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

    def mostrar_informacion(self):

        return (
            "=== DOCENTE ===\n\n"
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Número Empleado: {self.numero_empleado}\n"
            f"Facultad: {self.facultad}\n"
            f"Tipo Contratación: {self.tipo_contratacion}\n"
            f"Horas Semanales: {self.horas_semanales}"
        )
    def realizar_actividad_principal(self):
        return (
            f"El docente orienta clases "
            f"en la facultad de "
            f"{self.facultad}."
        )