# Sistema Avanzado de Gestión de Proyectos y Tareas

Este proyecto fue desarrollado como parte de una prueba parcial realizada en junio de 2024 para la Universidad José Antonio Páez.

## Descripción

El sistema está diseñado para gestionar de manera efectiva los proyectos y tareas de una empresa. Cuenta con los siguientes módulos:

1. **Módulo de Gestión de Proyectos**:
   - Permite crear, modificar, consultar, eliminar y listar los proyectos.
   - Los usuarios pueden agregar nuevos proyectos.
   - Búsqueda de proyectos por nombre u otros criterios.

2. **Módulo de Gestión de Tareas y Prioridades**:
   - Cada proyecto contiene una lista enlazada de tareas.
   - Los usuarios pueden agregar nuevas tareas al final de la lista o en posiciones específicas.
   - Implementación de una pila para almacenar las tareas prioritarias.
   - Utilización de una cola para almacenar las tareas próximas a su fecha de vencimiento.

3. **Módulo de Reportes**:
   - Consulta de tareas por estado (pendientes, en progreso, completadas).
   - Filtrado de tareas y proyectos por fechas relevantes.
   - Listado jerárquico de sub tareas de un proyecto.

4. **Módulo de importación y exportación de datos**:
   - Carga automática de datos al inicio del programa.
   - Carga de sub tareas desde un archivo JSON.
   - Respaldo automático de los datos del programa.

## Tecnologías utilizadas

- Lenguaje de programación: Python
- Estructuras de datos: Listas enlazadas, pilas y colas

## Cómo ejecutar el proyecto

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el archivo principal del proyecto.

## Contribución

Este proyecto fue desarrollado individualmente como parte de una prueba parcial. Sin embargo, si deseas contribuir con mejoras o sugerencias, puedes crear un fork del repositorio y enviar tus pull requests.

## Licencia

Este proyecto se encuentra bajo la Licencia MIT. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles.
