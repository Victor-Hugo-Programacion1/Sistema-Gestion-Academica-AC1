from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura

from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

from models.horario import Horario
from models.grupo_academico import GrupoAcademico

from models.exceptions import (
    EstudianteDuplicadoError,
    CapacidadMaximaError,
    EstudianteNoEncontradoError,
    AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError
)


def main():

    # Prueba clase abstracta Persona

    try:

        persona = Persona(
            "12345678",
            "Victor Hugo Zapata Florez",
            "victor@correo.com"
        )

    except TypeError as e:

        print(
            "No es posible crear objetos de la clase Persona."
        )

        print(e)

        print()

    # Objetos principales

    programa = ProgramaAcademico(
        "SIS001",
        "Ingenieria de Sistemas",
        "Ingenieria",
        10
    )

    asignatura = Asignatura(
        "POO001",
        "Programacion Orientada a Objetos",
        3,
        programa
    )

    programas = [
        programa
    ]

    asignaturas = [
        asignatura
    ]

    estudiante = Estudiante(
        "123456",
        "Juan Perez",
        "juan@correo.com",
        "E001",
        programa,
        4,
        4.2
    )

    estudiante2 = Estudiante(
        "222222",
        "Ana Lopez",
        "ana@correo.com",
        "E002",
        programa,
        3,
        4.0
    )

    estudiante3 = Estudiante(
        "333333",
        "Carlos Torres",
        "carlos@correo.com",
        "E003",
        programa,
        2,
        3.8
    )

    docente = Docente(
        "987654",
        "Maria Gomez",
        "maria@correo.com",
        "D001",
        "Ingenieria",
        "Tiempo Completo",
        40
    )

    administrativo = Administrativo(
        "555555",
        "Carlos Ruiz",
        "carlos@correo.com",
        "A001",
        "Registro Academico",
        "Coordinador",
        "Diurna"
    )

    horario1 = Horario(
        "Lunes",
        "18:00",
        "20:00",
        "B201"
    )

    horario2 = Horario(
        "Martes",
        "18:00",
        "20:00",
        "B202"
    )

    grupo1 = GrupoAcademico(
        "G001",
        asignatura,
        docente,
        horario1,
        30
    )

    grupo2 = GrupoAcademico(
        "G002",
        asignatura,
        docente,
        horario2,
        2
    )

    # Matrícula correcta

    grupo1.matricular_estudiante(
        estudiante
    )

    # PRUEBA ESTUDIANTE DUPLICADO

    try:

        grupo1.matricular_estudiante(
            estudiante
        )

    except EstudianteDuplicadoError as e:

        print(
            "\nPRUEBA ESTUDIANTE DUPLICADO"
        )

        print(e)

        print()

    # PRUEBA ESTUDIANTE NO ENCONTRADO

    try:

        grupo1.retirar_estudiante(
            "E999"
        )

    except EstudianteNoEncontradoError as e:

        print(
            "\nPRUEBA ESTUDIANTE NO ENCONTRADO"
        )

        print(e)

        print()

    # PRUEBA CAPACIDAD MÁXIMA

    try:

        grupo2.matricular_estudiante(
            estudiante
        )

        grupo2.matricular_estudiante(
            estudiante2
        )

        grupo2.matricular_estudiante(
            estudiante3
        )

    except CapacidadMaximaError as e:

        print(
            "\nPRUEBA CAPACIDAD MAXIMA"
        )

        print(e)

        print()

    # PRUEBA ASIGNATURA NO ENCONTRADA

    try:

        codigo_asignatura = "MAT999"

        asignatura_encontrada = None

        for asignatura_actual in asignaturas:

            if (
                asignatura_actual.codigo
                == codigo_asignatura
            ):
                asignatura_encontrada = asignatura_actual

        if asignatura_encontrada is None:

            raise AsignaturaNoEncontradaError(
                "La asignatura buscada no existe."
            )

    except AsignaturaNoEncontradaError as e:

        print(
            "\nPRUEBA ASIGNATURA NO ENCONTRADA"
        )

        print(e)

        print()

    # PRUEBA PROGRAMA NO ENCONTRADO

    try:

        codigo_programa = "ADM999"

        programa_encontrado = None

        for programa_actual in programas:

            if (
                programa_actual.codigo
                == codigo_programa
            ):
                programa_encontrado = programa_actual

        if programa_encontrado is None:

            raise ProgramaNoEncontradoError(
                "El programa académico buscado no existe."
            )

    except ProgramaNoEncontradoError as e:

        print(
            "\nPRUEBA PROGRAMA NO ENCONTRADO"
        )

        print(e)

        print()

    # Información del grupo

    print(
        grupo1.mostrar_informacion_grupo()
    )

    print()

    print(
        horario1.mostrar_horario()
    )

    print()

    grupo1.mostrar_estudiantes()

    print()

    # Información de las personas

    personas = [
        estudiante,
        docente,
        administrativo
    ]

    for persona in personas:

        print(
            persona.mostrar_informacion()
        )

        print()

    # Polimorfismo

    for persona in personas:

        print(
            persona.realizar_actividad_principal()
        )

        print()


if __name__ == "__main__":
    main()