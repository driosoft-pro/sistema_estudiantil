class Estudiante:
    def __init__(self, nombre, codigo, notas):
        self.__nombre = nombre  # Atributo privado para el nombre
        self.__codigo = codigo  # Atributo privado para el código
        self.__notas = notas    # Atributo privado para las notas

    def get_nombre(self):
        return self.__nombre  # Método para obtener el nombre

    def get_codigo(self):
        return self.__codigo  # Método para obtener el código

    def get_notas(self):
        return self.__notas  # Método para obtener las notas

    def calcular_promedio(self):
        # Método para calcular el promedio de las notas del estudiante
        return sum(self.__notas.values()) / len(self.__notas)

    def mostrar_todo(self):
        # Método para mostrar toda la información del estudiante
        print("=" * 40)  # Línea divisoria
        print(" " * 5, "Calificaciones", " " * 5)  # Título
        print("=" * 40)  # Línea divisoria
        print(f"Nombre: {self.__nombre}")
        print(f"Código: {self.__codigo}")
        print("Las notas del estudiante son:")
        for key, nota in self.__notas.items():
            print(f"{key}: {nota}")
        print(f"Promedio del estudiante: {self.calcular_promedio():.2f}")
        print("=" * 40)  # Línea divisoria