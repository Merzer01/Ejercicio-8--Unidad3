from docente_SC_personal import Docente
from investigador_SC_personal import Investigador

#CLASE HIJA DE DOCENTE E INVESTIGADOR
class DocInv(Docente,Investigador):
    __cat_incentivos: str
    __extra: int
    def __init__(self, cu, ap, nomb, sb, ant, carr, carg, cat, area, tipo, inc, extra):
        super().__init__(cu, ap, nomb, sb, ant, carr, carg, cat, area, tipo)
        self.__cat_incentivos = inc
        self.__extra = extra

    def getincentivo(self):
        return self.__cat_incentivos
    def getextra(self):
        return self.__extra