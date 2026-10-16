class Persona:

    def __init__(self, identificacion, nombre, correo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.set_correo(correo)

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):

        if correo != "":
            self.correo = correo
        else:
            raise ValueError(
                "El correo no puede estar vacío"
            )
    def mostrar_informacion(self):

        return (
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}"
        )
    def realizar_actividad_principal(self):
        return "Realizando actividad general."