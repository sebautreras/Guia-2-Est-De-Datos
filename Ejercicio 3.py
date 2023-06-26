# Implementar una lista enlazada simple para A. Agregar datos: Permite ingresar un nuevo dato a la lista


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            actual = self.cabeza
            while actual is not None:
                print(actual.dato, end=" ")
                actual = actual.siguiente
            print()

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)
lista.imprimir()





#codigo con los dos primeros pasos



class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            actual = self.cabeza
            while actual is not None:
                print(actual.dato, end=" ")
                actual = actual.siguiente
            print()

    def calcular_media(self):
        if self.cabeza is None:
            return None

        total = 0
        contador = 0
        actual = self.cabeza

        while actual is not None:
            total += actual.dato
            contador += 1
            actual = actual.siguiente

        media = total / contador
        return media

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)
lista.imprimir()

media = lista.calcular_media()
if media is not None:
    print("La media de los datos es:", media)
else:
    print("La lista está vacía, no se puede calcular la media.")



#Codigo con los 3 primeros datos que solicita


import math

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir(self):
        if self.cabeza is None:
            print("La lista está vacía.")
        else:
            actual = self.cabeza
            while actual is not None:
                print(actual.dato, end=" ")
                actual = actual.siguiente
            print()

    def calcular_media(self):
        if self.cabeza is None:
            return None

        total = 0
        contador = 0
        actual = self.cabeza

        while actual is not None:
            total += actual.dato
            contador += 1
            actual = actual.siguiente

        media = total / contador
        return media

    def calcular_desviacion_estandar(self):
        if self.cabeza is None:
            return None

        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        actual = self.cabeza

        while actual is not None:
            suma_cuadrados += (actual.dato - media) ** 2
            contador += 1
            actual = actual.siguiente

        varianza = suma_cuadrados / contador
        desviacion_estandar = math.sqrt(varianza)
        return desviacion_estandar

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)
lista.imprimir()

desviacion = lista.calcular_desviacion_estandar()
if desviacion is not None:
    print("La desviación estándar de los datos es:", desviacion)
else:
    print("La lista está vacía, no se puede calcular la desviación estándar.")
git