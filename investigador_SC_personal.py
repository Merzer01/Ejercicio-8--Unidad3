from personal_CP import Personal

#CLASE HIJA DE PERSONAL
class Investigador(Personal):
    __area: str
    __tipo: str
    def __init__(self, cu, ap, nomb, sb, ant, area, tipo):
        super().__init__(cu, ap, nomb, sb, ant)
        self.__area = area
        self.__tipo = tipo

    def getarea(self):
        return self.__area
    def gettipo(self):
        return self.__tipo