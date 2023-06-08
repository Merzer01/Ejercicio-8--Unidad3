class Menu(object):
    def showmenu(self):
        print('''
--------MENU DE OPCIONES--------
1 - Insertar personal (en una posicion determinada)
2 - Agregar personal (al final de todos)
3 - Mostrar tipo de personal
4 - Docentes investigadores por carreras
5 - Cantidad de docentes investigadores en un area
6 - Listado de personal (Ordenado por apellido)
7 - Listado de personal (dada una categoria)
0 - Salir
        ''')
        cond = False
        while not cond:
            op = int(input("Ingrese opcion: "))
            if op in [1,2,3,4,5,6,7,0]:
                cond = True
        return op