from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura

from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo

from models.horario import Horario
from models.grupo_academico import GrupoAcademico


def main():

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

    estudiante = Estudiante(
        "123456",
        "Juan Perez",
        "juan@correo.com",
        "E001",
        programa,
        4,
        4.2
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
        25
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

    grupo1.matricular_estudiante(
        estudiante
    )

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

    personas = [
        estudiante,
        docente,
        administrativo
    ]

    for persona in personas:

        print(persona.mostrar_informacion())
        print()

    for persona in personas:

        print(persona.realizar_actividad_principal())
        print()


if __name__ == "__main__":
    main()

