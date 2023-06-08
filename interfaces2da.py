from zope.interfaces import interface

class ITesorero(interface):
    def gastosSueldoPorEmpleado(dni):
        pass

class IDirector(interface):
    def modificarBasico(dni, nuevoBasico):
        pass
    def modificarPorcentajeporcargo(dni, nuevoPorcentaje):
        pass
    def modificarPorcentajeporcategoria(dni, nuevoPorcentaje):
        pass
    def modificarImporteExtra(dni, nuevoImporteExtra):
        pass