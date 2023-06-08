from personal_CP import Personal
from apoyo_SC_personal import Apoyo
from docente_SC_personal import Docente
from investigador_SC_personal import Investigador
from docinv_SC_doc_inv import DocInv
from coleccion import Coleccion
from objectencoder import ObjectEncoder
from menu import Menu
import os

def cargarPersonal():
    print('''
Tipo de Personal
1 - Docente
2 - Personal de Apoyo
3 - Investigador
4 - Docente investigador
    ''')
    op = int(input("Ingrese el tipo de personal: "))
    cu = str(input("Ingrese numero de cuil (incluyendo los guiones): "))
    ap = str(input("Ingrese apellido: "))
    nomb = str(input("Ingrese nombre: "))
    sb = int(input("Ingrese sueldo basico: "))
    ant = int(input("Ingrese antiguedad: "))
    if op == 1:
        carrera = str(input("Ingrese carrera en la que dicta clase: "))
        cargo = str(input("Ingrese cargo que ocupa: "))
        catedra = str(input("Ingrese catedra a la que pertenece: "))
        xp = Docente(cu, ap, nomb, sb, ant, carrera, cargo, catedra)
    elif op == 1:
        categoria = str(input("Ingrese la categoria a la que corresponde: "))
        xp = Apoyo(cu, ap, nomb, sb, ant, categoria)
    elif op == 1:
        area = str(input("Ingrese area en la que investiga: "))
        tipo = str(input("Ingrese tipo de investigacion: "))
        xp = Investigador(cu, ap, nomb, sb, ant, area, tipo)
    elif op == 1:
        area = str(input("Ingrese area en la que investiga: "))
        tipo = str(input("Ingrese tipo de investigacion: "))
        incentivo = str(input("Ingrese categoria del programa de incentivos: "))
        extra = int(input("Ingrese monto extra por docencia e investigacion: "))
        xp = DocInv(cu, ap, nomb, sb, ant, carrera, cargo, categoria, area, tipo, incentivo, extra)
    return xp


if __name__ == '__main__':
    os.system('cls')
    lista = Coleccion()
    jsonF = ObjectEncoder()
    dic = jsonF.leerJSONfile('Personal.json')
    lista = jsonF.decodificarDiccionario(dic, lista)
    band = False
    while not band:
        menu = Menu()
        opcion = menu.showmenu()
        if opcion == 1:
            xp = cargarPersonal()
            pos = int(input("Ingrese la posicion en la que añadir el elemento: "))
            lista.insertarElemento(xp, pos)
        elif opcion == 2:
            xp = cargarPersonal()
            lista.agregarElemento(xp)
        elif opcion == 3:
            pos = int(input("Ingrese la posicion en la que añadir el elemento: "))
            lista.mostrarElemento(pos)
        elif opcion == 4:
            carrera = str(input("Ingrese nombre de la carrera: "))
            lo = lista.listado_nombres(carrera)
            for docente in lo:
                print(docente)
        elif opcion == 5:
            l = []
            area = str(input("Ingrese area a consultar: "))
            cont = lista.cant_docinv(area, l)
            print('''
            Area: {}
Cantidad de docentes investigadores: {}
Cantidad total de investigadores: {}
            '''.format(area, l[0], l[1]))
        elif opcion == 6:
            ''
        elif opcion == 7:
            ''
        elif opcion == 0:
            print("Saliendo...")
            band = True
        else: print("Opcion Incorrecta!!!")
    os.system('pause')
    os.system('cls')