
class Contacto:
    def __init__(self, nombre, telefono, email):
        """Inicializa los atributos de un contacto"""
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        """Representación de un contacto"""
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
        """Inicializa la agenda vacía"""
        self.contactos = []

    def añadir_contacto(self):
        """Añadir un nuevo contacto a la agenda"""
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)
        print("Contacto añadido exitosamente.")

    def lista_contactos(self):
        """Muestra todos los contactos en la agenda"""
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto)

    def buscar_contacto(self):
        """Busca un contacto por nombre"""
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(contacto)
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")

    def editar_contacto(self):
        """Edita los datos de un contacto existente"""
        nombre = input("Ingrese el nombre del contacto a editar: ")
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print("Contacto encontrado. Ingrese los nuevos datos:")
                contacto.nombre = input("Nuevo nombre: ")
                contacto.telefono = input("Nuevo teléfono: ")
                contacto.email = input("Nuevo email: ")
                print("Contacto actualizado.")
                return
        print("Contacto no encontrado.")

    def cerrar_agenda(self):
        """Cierra la agenda"""
        print("Agenda cerrada.")
        exit()


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\nMenú de Agenda")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")


def ejecutar_agenda():
    """Ejecuta el programa de la agenda"""
    agenda = Agenda()
        if ione una opción (1-5): ")
        if opcion == '1':
            agenda.añadir_contacto()
        elif opcion == '2':
            agenda.lista_contactos()
        elif opcion == '3':
            agenda.buscar_contacto()
        elif opcion == '4':
            agenda.editar_contacto()
        elif opcion == '5':
            agenda.cerrar_agenda()
        else:
            print("Opción inválida. Por favor, seleccione una opción entre 1 y 5.")


ejecutar_agenda()
