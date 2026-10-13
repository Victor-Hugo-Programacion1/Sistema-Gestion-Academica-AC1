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