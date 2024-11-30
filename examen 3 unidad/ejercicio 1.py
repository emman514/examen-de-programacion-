print("")
print("castruita soto emmanuel 3w 1176")
print("")
class Alumno:
    def __init__(self, nombre, calificacion):
        """Inicializa el nombre y la calificación del alumno"""
        self.nombre = nombre
        self.calificacion = calificacion

    def imprimir_info(self):
        """Imprime el nombre y la calificación del alumno"""
        print(f"Nombre del alumno: {self.nombre}")
        print(f"Calificación: {self.calificacion}")

    def resultado(self):
        """Muestra el resultado de la calificación y si ha aprobado o no"""
        if self.calificacion >= 6:
            print(f"¡Felicidades {self.nombre}! Has aprobado.")
        else:
            print(f"Lo siento {self.nombre}, no has aprobado.")

# Función principal que pide datos al usuario
def main():
    nombre = input("Ingrese el nombre del alumno: ")
    calificacion = float(input("Ingrese la calificación del alumno: "))
    
    # Crear objeto Alumno con los datos ingresados
    alumno = Alumno(nombre, calificacion)
    
    # Mostrar la información y el resultado
    alumno.imprimir_info()
    alumno.resultado()

if __name__ == "__main__":
    main()
