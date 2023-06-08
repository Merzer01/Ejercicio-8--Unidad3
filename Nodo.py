class Nodo:
    __dato: None
    __siguiente: None
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    def setsiguiente(self, siguiente):
        self.__siguiente = siguiente
    def getsiguiente(self):
        return self.__siguiente
    def getdato(self):
        return self.__dato