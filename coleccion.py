from zope.interface import implementer
from interfaz import IColeccion
from docinv_SC_doc_inv import DocInv
from investigador_SC_personal import Investigador
from Nodo import Nodo

@implementer(IColeccion)
class Coleccion:
    __actual: None
    __comienzo: None
    __indice = 0
    __tope = 0
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getdato()
            self.__actual = self.__actual.getsiguiente()
            return dato
    
    def searchAnt(self, pos):
        ant = self.__comienzo
        while self.__indice < pos:
            ant = ant.getsiguiente()
            self.__indice += 1
        return ant

    def agregarElemento(self, elemento):    #ESTO NO AGREGA AL FINAL opcion 1
        nodo = Nodo(elemento)   #CREAR NODO
        if self.__comienzo == None:
            self.__comienzo = nodo
        else: 
            aux = self.__comienzo
            while aux.getsig() != None:
                aux = aux.getsig()
    
    def insertarElemento(self, elemento, posicion): #opcion 2
        if posicion < 0 or posicion > self.__tope:
            raise ValueError('Posicion invalida')
        if posicion == 0:
            self.agregarElemento(elemento)
        else:
            self.__indice = 0
            anterior = self.searchAnt(posicion)
            nuevo = Nodo(elemento)
            sig = anterior.getsiguiente()
            nuevo.setsiguiente(sig)
            anterior.setsiguiente(Nodo)
            self.__actual = nuevo
            self.__tope += 1
            self.__indice = 0
    
    def mostrarElemento(self, posicion):    #opcion 3
        if posicion < 0 or posicion > self.__tope:
            raise ValueError('Posicion invalida')
        if posicion == 0:
            print("Tipo de personal: {}".format(type(self.__comienzo)))
        else:
            for dato in self:
                if self.__indice == posicion:
                    print("Tipo de personal: {}".format(type(dato)))

    def listado_nombres(self, c):
        lista = []
        for dato in self:
            if isinstance (dato, DocInv) and dato.getcarrera() == c:
                lista.append(dato)
        
        if len(lista) > 0:
            lista.sort(key=lambda x: x.getnombre())
        else:
            raise ValueError("No hay docentes en la carrera {}".format(c))
        return lista
    
    def cant_docinv(self, area, l):
        cdi = 0 #contador de docentes investigadores
        ct = 0  #contador total
        for dato in self:
            if isinstance (dato, DocInv) and dato.getarea() == area:
                cdi += 1
            if isinstance (dato, Investigador) and dato.getarea() == area:
                ct += 1
        l[0] = cdi
        l[1] = ct