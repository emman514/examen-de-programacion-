print("")
print("castruita soto emmanuel 3w 1176")
print("")
class Persona:
    def __init__(self, nombre="", edad=0,):
        self.nombre = nombre
        self.edad = edad
    def nombre(self):
        return self._nombre
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value
    def edad(self):
        return self._edad
    def edad(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("La edad debe ser un entero positivo.")
        self._edad = value
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad},"
    def esMayorDeEdad(self):
        return self.edad >= 18
try:
    persona = Persona(nombre="Juan", edad=25, )
    print(persona.mostrar())
    print("Es mayor de edad:", persona.esMayorDeEdad())
except ValueError as e:
    print(e)