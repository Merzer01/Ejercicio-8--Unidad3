from zope.interface import interface
from zope.interface import implementer

class Interfaz(interface):
    def insertarElemento(elemento, posicion):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass