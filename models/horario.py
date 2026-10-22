class Horario:

    def __init__(
        self,
        dia,
        hora_inicio,
        hora_fin,
        salon
    ):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.salon = salon

    def mostrar_horario(self):
        return (
            f"Día: {self.dia}\n"
            f"Hora: {self.hora_inicio} - {self.hora_fin}\n"
            f"Salón: {self.salon}"
        )