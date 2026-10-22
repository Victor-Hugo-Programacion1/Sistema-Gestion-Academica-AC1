from models.exceptions import (
    EstudianteDuplicadoError,
    CapacidadMaximaError,
    EstudianteNoEncontradoError
)


class GrupoAcademico:

    def __init__(
        self,
        codigo,
        asignatura,
        docente,
        horario,
        capacidad
    ):
        self.codigo = codigo
        self.asignatura = asignatura
        self.docente = docente
        self.horario = horario
        self.capacidad = capacidad
        self.estudiantes = []

    def mostrar_informacion_grupo(self):

        return (
            f"Grupo: {self.codigo}\n"
            f"Asignatura: {self.asignatura.nombre}\n"
            f"Docente: {self.docente.nombre}\n"
            f"Capacidad: {self.capacidad}\n"
            f"Matriculados: {len(self.estudiantes)}"
        )

    def matricular_estudiante(
        self,
        estudiante
    ):

        for estudiante_existente in self.estudiantes:

            if (
                estudiante_existente.codigo_estudiantil
                == estudiante.codigo_estudiantil
            ):
                raise EstudianteDuplicadoError(
                    "El estudiante ya está matriculado."
                )

        if len(self.estudiantes) >= self.capacidad:

            raise CapacidadMaximaError(
                "El grupo alcanzó su capacidad máxima."
            )

        self.estudiantes.append(
            estudiante
        )

    def retirar_estudiante(
        self,
        codigo_estudiantil
    ):

        for estudiante in self.estudiantes:

            if (
                estudiante.codigo_estudiantil
                == codigo_estudiantil
            ):
                self.estudiantes.remove(
                    estudiante
                )
                return

        raise EstudianteNoEncontradoError(
            "El estudiante no está matriculado."
        )

    def mostrar_estudiantes(self):

        for estudiante in self.estudiantes:

            print(
                estudiante.nombre
            )