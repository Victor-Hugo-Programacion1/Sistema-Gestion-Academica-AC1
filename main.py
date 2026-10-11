from models.persona import Persona
from models.programa_academico import ProgramaAcademico
from models.asignatura import Asignatura


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

    print("=== PERSONA ===")
    print(persona.nombre)

    print("\n=== PROGRAMA ACADEMICO ===")
    print(programa.nombre)

    print("\n=== ASIGNATURA ===")
    print(asignatura.nombre)


if __name__ == "__main__":
    main()