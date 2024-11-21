#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
#Se deja una linea en blanco para q se vea mas limpio
print("")
class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    # Setter y getter para nombre
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and len(nombre) > 0:
            self.nombre = nombre
        else:
            print("Nombre no válido.")

    def get_nombre(self):
        return self.nombre

    # Setter y getter para edad
    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("Edad no válida.")

    def get_edad(self):
        return self.edad

    # Método para mostrar los datos
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

    # Método para verificar si es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo de uso
persona = Persona("Alexa", 19)
persona.mostrar()
print(f"¿Es mayor de edad? {'Sí' if persona.es_mayor_de_edad() else 'No'}")
