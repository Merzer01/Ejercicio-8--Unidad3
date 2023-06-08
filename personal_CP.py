#CLASE PADRE
class Personal:
    __cuil: str #formato xx-dni-x
    __apellido: str
    __nombre: str
    __sueldo_basico: int
    __antiguedad: int
    def __init__(self, cu, ap, nomb, sb, ant):
        self.__cuil = cu
        self.__apellido = ap
        self.__nombre = nomb
        self.__sueldo_basico = sb
        self.__antiguedad = ant
    
    def getapellido(self):
        return self.__apellido
    def getnombre(self):
        return self.__nombre
    def getsueldo(self):
        return self.__sueldo_basico
    def getant(self):
        return self.__antiguedad