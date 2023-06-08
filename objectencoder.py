from pathlib import Path
from personal_CP import Personal
from apoyo_SC_personal import Apoyo
from docente_SC_personal import Docente
from investigador_SC_personal import Investigador
from docinv_SC_doc_inv import DocInv
import json

class ObjectEncoder(object):
    def decodificarDiccionario(self, d, lista):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_=eval(class_name)
            if class_name == 'Coleccion':
                personal = d['personal']
                coleccion = class_()
                for i in range(len(personal)):
                    xPersonal = personal[i]
                    class_name = xPersonal.pop('__class__')
                    class_ = eval(class_name)
                    atributos = xPersonal['__atributos__']
                    p = class_(**atributos)
                    lista.agregarElementos(p)
            return lista


    def guardarJSONfile(self, diccionario, archivo):
        with Path(archivo).open('w', encoding='UTF-8') as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
    
    def leerJSONfile(self, archivo):
        with Path(archivo).open(encoding='UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario
    
    def convertirTextoaDiccionario(self, texto):
        return json.loads(texto)