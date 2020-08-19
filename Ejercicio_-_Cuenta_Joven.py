class Cuenta:
    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad
    
    def __str__(self):
        return "titular: {} cantidad: {}".format(self.titular, self.cantidad)
    
    def mostrar(self): 
        print(self.__str__())
    
    def ingresar(self,cantidad):
        if cantidad < 0:
            return
        else:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        self.cantidad -= cantidad

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion, edad):
        Cuenta.__init__(self, titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad
    
    def esTitularValido(self):
        if self.edad >=18 and self.edad <= 25:
            print("Es titular valido")
            return True
        else:
            print("No es titular valido")
            return False
    
    def retirar(self, cantidad):
        if self.esTitularValido() == True:
            self.cantidad -= cantidad 

    def __str__(self):
        return "titular: {} bonificacion: {} %".format(self.titular, self.bonificacion)
    
    def mostrar(self): 
        print(self.__str__())

'''cuentaGeronimo = Cuenta("Geronimo Franco")
print(cuentaGeronimo)
cuentaGeronimo.mostrar()
cuentaGeronimo.ingresar(100)
cuentaGeronimo.mostrar()
cuentaGeronimo.retirar(30)
cuentaGeronimo.mostrar()'''

prueba1 = CuentaJoven("maxi", 15350, 10, 22)
print(prueba1)
prueba1.retirar(1475)
prueba1.mostrar()