class Obj:
    # Separador de los vértices
    SEPARATOR = " "
    # Comienzo de un vértice
    START_VERTEX = "v"
    # Comienzo de una normal
    START_NORMAL = "vn"
    # Comienzo de un color
    START_TEXT = "vt"
    # Comienzo de una cara
    START_FACE = "f"
    # Separador de cara
    SEPARATOR_FACES = "/"

    def __init__(self):
        self.__vertexs = []
        self.__normals = []
        self.__text = []

        self.aVerts = []
        self.aNormals = []
        self.aTexts = []

    def get_vertices(self):
        return self.aVerts

    def get_normales(self):
        return self.aNormals

    def get_texturas(self):
        return self.aTexts

    def load(self, archivo):
        for line in open(archivo):
            clean_line = line.strip()

            if clean_line == "":
                continue

            tipo = clean_line.split(" ")[0]

            if tipo == self.START_VERTEX:
                self.load_vertex(clean_line)
            if tipo == self.START_NORMAL:
                self.load_normal(clean_line)
            if tipo == self.START_TEXT:
                self.load_text(clean_line)
            if tipo == self.START_FACE:
                self.load_face(clean_line)

    def load_vertex(self, line):
        splitted_line = line.split(self.SEPARATOR)
        vertex = []
        for elem in splitted_line[1:]:
            if elem != "":
                vertex.append(float(elem))

        self.__vertexs.append(tuple(vertex))

    def load_normal(self, line):
        splitted_line = line.split(self.SEPARATOR)
        normal = []
        for elem in splitted_line[1:]:
            if elem != "":
                normal.append(float(elem))

        self.__normals.append(tuple(normal))

    def load_text(self, line):
        splitted_line = line.split(self.SEPARATOR)
        text = []
        for elem in splitted_line[1:]:
            if elem != "":
                text.append(float(elem))

        self.__text.append(tuple(text))

    def load_face(self, line):
        splitted_line = line.split(self.SEPARATOR)

        for trio in splitted_line[1:]:
            if trio == "":
                continue

            elems = trio.split(self.SEPARATOR_FACES)

            v = self.__vertexs[(int(elems[0]) - 1)]
            self.aVerts.append(v)
            vn = self.__normals[(int(elems[1]) - 1)]
            self.aNormals.append(vn)
            vt = self.__text[(int(elems[2]) - 1)]
            self.aTexts.append(vt)


class Parser:
    objs = {}

    def __init__(self):
        self.objs = {}

    def agregar_obj(self, source):
        new_obj = Obj()
        new_obj.cargar(source)
        self.objs.update({source: new_obj})

    def quitar_obj(self, source):
        self.objs.pop(source)

    def get_obj(self, name):
        return self.objs[name]
