# Sistema Estudiantil

Este proyecto es un sistema de gestión de estudiantes que permite registrar estudiantes, ingresar sus notas y calcular promedios. Está desarrollado en Python y utiliza un enfoque orientado a objetos para manejar la información de los estudiantes.

---

## Requisitos

- Python 3.8 o superior.
- Entorno virtual (recomendado).

---

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone git@github.com:driosoft-pro/sistema_estudiantil.git
    ```

2. Navega a la carpeta del proyecto:

    ```bash
    cd sistema_estudiantil
    ```

3. Crea y activa un entorno virtual:

    - **Linux/MacOS**:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

    - **Windows**:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

4. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

---

## Configuración

1. Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

    ```bash
    FLASK_ENV=development
    ```

    Este archivo se utiliza para configurar el entorno de desarrollo.

---

## Ejecución

1. Para ejecutar el proyecto sin necesidad de Docker, utiliza el siguiente comando:

    ```bash
    python run.py
    ```
---

## Estructura del Proyecto

- **`estudiante.py`**: Contiene la clase `Estudiante` que maneja la lógica de los estudiantes y sus notas.
- **`main.py`**: Es el archivo principal que ejecuta el sistema y maneja la interacción con el usuario.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar el proyecto.
- **`.env`**: Archivo de configuración para el entorno de desarrollo.
- **`README.md`**: Este archivo, que proporciona información sobre el proyecto.

---

## Uso del Sistema

1. **Registro de Estudiantes**:
   - El sistema solicita el nombre, código y notas de cada estudiante.
   - El código debe comenzar con `DRZ0` seguido de 4 dígitos (por ejemplo, `DRZ01234`).
   - Las notas deben estar en el rango de 1.0 a 5.0.

2. **Cálculo de Promedios**:
   - El sistema calcula automáticamente la nota final como el promedio de las notas de `Actividades`, `Projecto` y `Parcial`.
   - También se calcula el promedio de la clase al final.

3. **Visualización de Datos**:
   - Al final, el sistema muestra la lista de estudiantes con sus notas y promedios, junto con el promedio general de la clase.

---

## Ejemplo de Ejecución

```bash
=== Ingrese los datos de un nuevo estudiante ===
Ingrese el nombre del estudiante: Steven Gomez
Ingrese el código del estudiante (DRZ0XXXX): DRZ01234
Ingrese la nota de Actividades (1.0 a 5.0): 5.0
Ingrese la nota de Projecto (1.0 a 5.0): 4.4
Ingrese la nota de Parcial (1.0 a 5.0): 3.2

¿Desea agregar otro estudiante? (s/n): n

========================================
Institución: Universidad XYZ
Clase: Programación I
Docente: Dr. Juan Pérez
========================================

=== Lista de estudiantes ===
========================================
      Calificaciones       
========================================
Nombre: Steven Gomez
Código: DRZ01234
Las notas del estudiante son:
Actividades: 5.0
Projecto: 4.4
Parcial: 3.2
Final: 4.2
Promedio del estudiante: 4.20
========================================

Total de estudiantes: 1
Promedio de la clase: 4.20

## Autor
📌 **By:** Deyton Riascos Ortiz