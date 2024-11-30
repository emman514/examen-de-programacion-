print("")
print("castruita soto emmanuel 3w 1176")
print("")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        """Inicializa los tres lados del triángulo"""
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        """Devuelve el valor del lado mayor"""
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        """Determina el tipo de triángulo"""
        if self.lado1 == self.lado2 == self.lado3:
            return "Equilátero"
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            return "Isósceles"
        else:
            return "Escaleno"

    def imprimir_info(self):
        """Imprime el lado mayor y el tipo de triángulo"""
        print(f"Lado mayor: {self.lado_mayor()}")
        print(f"Tipo de triángulo: {self.tipo_triangulo()}")

# Definir los valores de los lados del triángulo aquí
lado1 = int(input("ingresa lado 1:"))
lado2 = int(input("ingresa lado 2:"))
lado3 =  int(input("ingresa lado 3:"))

# Crear el objeto Triangulo con los valores predefinidos
triangulo = Triangulo(lado1, lado2, lado3)
triangulo.imprimir_info()
