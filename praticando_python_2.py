#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
#se deja ua linea enlanco para que se vea mas limpio
print("")
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    # Mostrar los datos
    def mostrar(self):
        print(f"Titular: {self.titular}, Saldo: {self.cantidad}€")

    # Ingresar dinero
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad debe ser positiva.")

    # Retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.cantidad:
            self.cantidad -= cantidad
        else:
            print("La cantidad debe ser positiva y no puede superar el saldo.")

# Ejemplo de uso
cuenta1 = Cuenta("Carlos", 1000)
cuenta1.mostrar()
cuenta1.ingresar(500)
cuenta1.retirar(200)
cuenta1.mostrar()
