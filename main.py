import estudiante as e  # Importa la clase Estudiante desde el archivo estudiante.py

def solicitar_nombre():
    # Función para solicitar un nombre válido (solo letras y espacios)
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if all(caracter.isalpha() or caracter.isspace() for caracter in nombre):
            return nombre
        print("Error: El nombre solo puede contener letras y espacios. Intenta de nuevo.")

def solicitar_codigo():
    # Función para solicitar un código válido (8 dígitos que comienzan con DRZ0)
    while True:
        codigo = input("Ingrese el código del estudiante (DRZ0XXXX): ").strip().upper()
        if codigo.startswith("DRZ0") and len(codigo) == 8 and codigo[4:].isdigit():
            return codigo
        print("Error: El código debe comenzar con DRZ0 seguido de 4 dígitos. Intenta de nuevo.")

def solicitar_nota(materia):
    # Función para solicitar una nota válida (entre 1 y 5, con un decimal)
    while True:
        try:
            nota = float(input(f"Ingrese la nota de {materia} (1.0 a 5.0): "))
            if 1.0 <= nota <= 5.0:
                return round(nota, 1)  # Redondear a un decimal
            print("Error: La nota debe estar entre 1.0 y 5.0. Intenta de nuevo.")
        except ValueError:
            print("Error: Debes ingresar un número válido. Intenta de nuevo.")

def solicitar_datos_estudiante():
    # Función para solicitar los datos de un estudiante
    nombre = solicitar_nombre()
    codigo = solicitar_codigo()

    # Solicitar las notas del estudiante
    notas = {
        "Actividades": solicitar_nota("Actividades"),
        "Projecto": solicitar_nota("Projecto"),
        "Parcial": solicitar_nota("Parcial")
    }

    # Calcular la nota final como el promedio de las otras notas
    notas["Final"] = round(sum(notas.values()) / len(notas), 1)

    return nombre, codigo, notas  # Retorna los datos del estudiante

def main():
    # Solicitar datos de la institución, clase y docente
    institucion = input("Ingrese el nombre de la institución educativa: ").strip()
    clase = input("Ingrese el nombre de la clase: ").strip()
    docente = input("Ingrese el nombre del docente: ").strip()

    estudiantes = []  # Lista para almacenar los estudiantes

    while True:
        # Solicitar los datos de un estudiante
        print("\n=== Ingrese los datos de un nuevo estudiante ===")
        nombre, codigo, notas = solicitar_datos_estudiante()

        # Crear un objeto Estudiante y agregarlo a la lista
        estudiantes.append(e.Estudiante(nombre, codigo, notas))

        # Preguntar si desea agregar otro estudiante
        continuar = input("\n¿Desea agregar otro estudiante? (s/n): ").strip().lower()
        if continuar != "s":
            break  # Salir del bucle si el usuario no quiere agregar más estudiantes

    # Mostrar los datos de la institución, clase y docente
    print("\n" + "=" * 40)
    print(f"Institución: {institucion}")
    print(f"Clase: {clase}")
    print(f"Docente: {docente}")
    print("=" * 40)

    # Mostrar la lista de estudiantes y sus notas
    print("\n=== Lista de estudiantes ===")
    for estudiante in estudiantes:
        estudiante.mostrar_todo()

    # Calcular y mostrar el promedio de la clase
    if estudiantes:
        promedio_clase = sum(estudiante.calcular_promedio() for estudiante in estudiantes) / len(estudiantes)
        print(f"\nTotal de estudiantes: {len(estudiantes)}")
        print(f"Promedio de la clase: {promedio_clase:.2f}")
    else:
        print("\nNo hay estudiantes registrados.")

if __name__ == '__main__':
    main()