from models.persona import Persona


class Estudiante(Persona):

    def __init__(
        self,
        identificacion,
        nombre,
        correo,
        codigo_estudiantil,
        programa_academico,
        semestre,
        promedio_acumulado
    ):

        super().__init__(
            identificacion,
            nombre,
            correo
        )

        self.codigo_estudiantil = codigo_estudiantil
        self.programa_academico = programa_academico
        self.semestre = semestre
        self.promedio_acumulado = promedio_acumulado
    def mostrar_informacion(self):

        return (
            "=== ESTUDIANTE ===\n\n"
            f"Identificación: {self.identificacion}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Código Estudiantil: {self.codigo_estudiantil}\n"
            f"Programa Académico: {self.programa_academico.nombre}\n"
            f"Semestre: {self.semestre}\n"
            f"Promedio Acumulado: {self.promedio_acumulado}"
        )   
    def realizar_actividad_principal(self):
        return (
            f"El estudiante cursa "
            f"{self.programa_academico.nombre} "
            f"y se encuentra en el semestre "
            f"{self.semestre}."
        )