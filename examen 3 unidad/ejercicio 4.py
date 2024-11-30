print("")
print("castruita soto emmanuel 3w 1176")
print("")
class Calculadora:
    def __init__(self, num1, num2):
        """Inicializa los dos valores numéricos"""
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        """Realiza la suma de los dos números"""
        return self.num1 + self.num2

    def restar(self):
        """Realiza la resta de los dos números"""
        return self.num1 - self.num2

    def multiplicar(self):
        """Realiza la multiplicación de los dos números"""
        return self.num1 * self.num2

    def dividir(self):
        """Realiza la división de los dos números"""
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

    def imprimir_resultados(self):
        """Imprime los resultados de todas las operaciones"""
        print(f"Suma: {self.sumar()}")
        print(f"Resta: {self.restar()}")
        print(f"Multiplicación: {self.multiplicar()}")
        print(f"División: {self.dividir()}")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
calculadora = Calculadora(num1, num2)
calculadora.imprimir_resultados()
