<img width="1971" height="2268" alt="image" src="https://github.com/user-attachments/assets/af161861-d995-40f5-896b-29d5c0bf4a41" />

Estado actual
- Fase 1 - Clases base y constructores (Completada)

- Fase 2 - Encapsulamiento y validaciones (Completada)

- Fase 3 - Herencia (Completada)

- Fase 4 - Sobrescritura (Completada)

- Fase 5 - Polimorfismo (Completada)

Participación del equipo
- VICTOR HUGO ZAPATA FLOREZ

Arquitectura, integración y desarrollo principal.
- YOAN MANUEL POVEDA SOTELO

Validación de créditos.
Pruebas de Asignatura.
Validación de la clase Estudiante durante la Fase 4 (Sobrescritura).

- SAMUEL HERNANDO SILVA NAVARRO

Pruebas y validación de Programa Académico.
Validación de la clase Docente durante la Fase 4 (Sobrescritura).
Validacion de la fase 5 (poliformismo).
Documentacion de la validacion poliformismo.


Uso de herramientas de inteligencia artificial

Durante el desarrollo del proyecto se utilizaron herramientas de inteligencia artificial como apoyo para comprender conceptos, revisar errores, interpretar mensajes de Git y GitHub, validar decisiones de diseño y orientar la resolución de problemas durante el desarrollo.
La mayor utilidad estuvo en el análisis y corrección de errores, permitiendo comprender qué ocurría en cada situación antes de aplicar una solución.
Todas las decisiones de diseño, pruebas, validaciones, integración y documentación fueron revisadas y verificadas por los integrantes del equipo antes de incorporarlas al proyecto.

Pruebas finales realizadas

Se verificó el funcionamiento del Sistema de Gestión Académica mediante pruebas de creación y validación de programas académicos, asignaturas, estudiantes, docentes y administrativos.

También se comprobó el correcto funcionamiento de los conceptos de encapsulamiento, herencia, sobrescritura y polimorfismo implementados durante el desarrollo del proyecto.

Todas las pruebas ejecutadas fueron satisfactorias

Validación final del proyecto

Se realizó una revisión final de los requisitos establecidos en la actividad colaborativa.

Se verificó el cumplimiento de:

Clases y objetos.
Constructores.
Encapsulamiento.
Herencia.
Sobrescritura.
Polimorfismo.
Organización del proyecto.
Documentación del repositorio.
El sistema cumple con los criterios técnicos definidos para la entrega.

Cierre del proyecto

Con la implementación y validación de las cinco fases propuestas, se da por finalizado el desarrollo del Sistema de Gestión Académica correspondiente a la Actividad Colaborativa N.° 1.
El proyecto fue desarrollado de manera colaborativa utilizando GitHub para el control de versiones y el seguimiento de las contribuciones de los integrantes del equipo.

## Relación de composición
El sistema implementa una relación de composición entre GrupoAcademico y Horario.
 
Cada grupo académico contiene un objeto Horario que almacena el día, hora de inicio, hora de finalización y salón donde se desarrolla la actividad académica.
 
La relación corresponde a composición porque un GrupoAcademico tiene un Horario como parte de su estructura, mientras que no existe una relación de herencia entre ambas clases.
 
Además, GrupoAcademico se relaciona con objetos de las clases Asignatura, Docente y Estudiante para representar la organización de la oferta académica.

## Implementación de la clase abstracta Persona
La clase Persona fue implementada como clase abstracta para impedir la creación directa de objetos genéricos dentro del sistema.
Las clases Estudiante, Docente y Administrativo implementan el método realizar_actividad_principal(), permitiendo definir comportamientos específicos para cada tipo de persona.
Esta implementación fortalece la abstracción y mantiene la estructura orientada a objetos del sistema.

## Uso de herramientas de inteligencia artificial

Durante el desarrollo del proyecto se utilizaron herramientas de inteligencia artificial como apoyo para comprender conceptos, revisar errores, analizar mensajes del sistema, validar decisiones de diseño y orientar la resolución de problemas presentados durante el desarrollo.

Todas las decisiones de implementación, pruebas, integración y documentación fueron revisadas, comprendidas y validadas por los integrantes del equipo antes de incorporarlas al proyecto.