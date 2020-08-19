## Vamos a hacer una baraja de cartas españolas orientado a objetos.

## Una carta tiene un número entre 1 y 12 (el 8 y el 9 no los incluimos) y un palo (espadas, bastos, oros y copas)

## La baraja estará compuesta por un conjunto de cartas, 40 exactamente.

## Las operaciones que podrá realizar la baraja son:

## barajar: cambia de posición todas las cartas aleatoriamente

## siguienteCarta: devuelve la siguiente carta que está en la baraja, cuando no haya más o se haya llegado al final, se indica al usuario que no hay más cartas.

## cartasDisponibles: indica el número de cartas que aún puede repartir

## darCartas: dado un número de cartas que nos pidan, le devolveremos ese número de cartas (piensa que puedes devolver). En caso de que haya menos cartas que las pedidas, no devolveremos nada pero debemos indicárselo al usuario.

## cartasMonton: mostramos aquellas cartas que ya han salido, si no ha salido ninguna indicárselo al usuario

## mostrarBaraja: muestra todas las cartas hasta el final. Es decir, si se saca una carta y luego se llama al método, este no mostrara esa primera carta.

class Carta:
    def __init__(self, figura, valor):
        self.figura = figura
        self.valor = valor

    def __repr__(self):
        return "{} de {}".format(self.valor, self.figura)

from random import shuffle

class Baraja:
    def __init__(self):
        figuras = ['Copas', 'Bastos', 'Oros', 'Espadas']
        valores = ['1','2','3','4','5','6','7','Sota','Caballo','Rey']
        self.cartas = [Carta(figura ,valor) for figura in figuras for valor in valores]
        self.descarte =list()
    
    def barajar(self):
        return shuffle(self.cartas)

    def siguienteCarta(self):
        if (len(self.cartas) == 0):
            raise ValueError("Todas las cartas se repartieron")
        cartaRepartida = self.cartas.pop()
        self.descarte.append(cartaRepartida)
        return cartaRepartida

    def cartasDisponibles(self):
        return len(self.cartas)
    
    def darCartas(self, cantidad):
        if (self.cartasDisponibles() < cantidad):
            raise ValueError("No dispongo de cartas suficientes")
        print("Estas son sus ", cantidad, "cartas:")
        for _ in range(cantidad):
            cartaRepartida = self.siguienteCarta()
            print(cartaRepartida)
    
    def cartasMonton(self):
        if (len(self.descarte) == 0):
            print("Todavia no se repartio ninguna carta")
        return self.descarte

    def mostrarBaraja(self):
        print(self.cartas)

    def __repr__(self):
        return "Cartas: {}".format(self.cartas)

##Pruebas

## Codigo principal

print("*"*8, "BIENVENIDO AL BARAJADOR DE CARTAS","*"*8)
carta = Carta("Copas", 6)
print(carta)

baraja = Baraja()
print(baraja)
print("*"*20)
baraja.barajar()
print(baraja)
print(baraja.siguienteCarta())
print(baraja.cartasDisponibles())
print(baraja.siguienteCarta())
baraja.darCartas(3)
print(baraja.cartasDisponibles())
print(baraja.cartasMonton())
baraja.mostrarBaraja()