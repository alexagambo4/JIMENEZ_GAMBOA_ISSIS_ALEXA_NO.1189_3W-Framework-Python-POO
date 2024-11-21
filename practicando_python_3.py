#imprime los datos de la autora 
print("Jimenez Gamboa Issis Alexa ")
print("no.1189")
print("3W")
#imprime linea en banco para qu se vea mas limpio
print("")
#imprime el titulo del prgrama 
print("Ejercicio no.1 ")
#se deja una linea en blanco para que se vea mas limpio
print("")
class CuentaJoven:
    def __init__(self, titular, edad, cantidad=0.0, bonificacion=0.0):
        self.titular = titular
        self.edad = edad
        self.cantidad = cantidad
        self.bonificacion = bonificacion

    # Mostrar los datos
    def mostrar(self):
        print(f"Cuenta Joven - Titular: {self.titular}, Edad: {self.edad}, Saldo: {self.cantidad}€, Bonificación: {self.bonificacion}%")

    # Verificar si el titular es mayor de 18 y menor de 25 años
    def es_titular_valido(self):
        return 18 <= self.edad < 25

    # Método para retirar dinero
    def retirar(self, cantidad):
        if self.es_titular_valido():
            if cantidad <= self.cantidad:
                self.cantidad -= cantidad
                print(f"Has retirado {cantidad}€. Saldo actual: {self.cantidad}€.")
            else:
                print("No tienes suficiente saldo.")
        else:
            print("El titular no es válido para una Cuenta Joven.")

# Ejemplo de uso
cuenta_joven = CuentaJoven("Ana", 22, 1500, 5)
cuenta_joven.mostrar()

# Intentar retirar dinero (titular válido)
cuenta_joven.retirar(300)

# Intentar retirar dinero (titular no válido)
cuenta_joven.edad = 26  # Cambiar la edad a un valor no válido
cuenta_joven.retirar(300)
