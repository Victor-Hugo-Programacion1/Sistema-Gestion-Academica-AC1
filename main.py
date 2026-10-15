from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura

from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo


def main():

    persona = Persona(
        "12345678",
        "Victor Hugo Zapata Florez",
        "victor@correo.com"
    )

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

    administrativo = Administrativo(
        "555555",
        "Carlos Ruiz",
        "carlos@correo.com",
        "A001",
        "Registro Academico",
        "Coordinador",
        "Diurna"
    )

    print(estudiante.mostrar_informacion())

    print()
    print(docente.mostrar_informacion())

    print()
    print(administrativo.mostrar_informacion())


if __name__ == "__main__":
    main()