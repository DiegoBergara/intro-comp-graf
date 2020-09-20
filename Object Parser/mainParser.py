from obj import Obj

class Parser:
    # Guardo todos los objetos con su respectiva lista de Vertices, Normales y Colores
    objs = {}

    def __init__(self):
        self.objs = {}
    
    def agregar_obj(self, source):
        new_obj = Obj()
        new_obj.cargar(source)
        self.objs.update({[source] : new_obj})
    
    def quitar_obj(self, source):
        self.objs.pop(source)