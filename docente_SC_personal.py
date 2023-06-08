from personal_CP import Personal

#CLASE HIJA DE PERSONAL
class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str
    def __init__(self, cu, ap, nomb, sb, ant, carr, carg, cat):
        super().__init__(cu, ap, nomb, sb, ant)
        self.__carrera = carr
        self.__cargo = carg
        self.__catedra = cat

    def getcarrera(self):
        return self.__carrera
    def getcargo(self):
        return self.__cargo
    def getcatedra(self):
        return self.__catedra