from personal_CP import Personal

#CLASE HIJA DE PERSONAL
class Apoyo(Personal): 
    __categoria: str
    def __init__(self, cu, ap, nomb, sb, ant, cat):
        super().__init__(cu, ap, nomb, sb, ant)
        self.__categoria = cat

    def getcat(self):
        return self.__categoria