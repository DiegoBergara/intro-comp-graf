class Obj:
    # Separador de los vértices
    SEPARADOR = " "
    # Comienzo de un vértice
    COMIENZO_VERTICE = "v"
    # Comienzo de una normal
    COMIENZO_NORMAL = "vn"
    # Comienzo de un color
    COMIENZO_COLOR = "vt"
    # Comienzo de una posición
    COMIENZO_POSICION = "f"
    # Separación del caracter inicial y los datos
    OFFSET = 2

    def __init__(self):
        self.__vertices = []
        self.__normales = []
        self.__colores = []

    def get_vertices(self):
        return self.__vertices

    def get_normales(self):
        return self.__normales

    def get_colores(self):
        return self.__colores

    # De un archivo extrae los vértices, normales y colores
    def cargar(self, archivo):
        vertices_ind = []
        normales_ind = []
        colores_ind = []

        for line in open(archivo):
            cl = line.strip()
            if cl == "":
                continue

            tipo_l = cl.split(" ")[0]
            if tipo_l == Obj.COMIENZO_VERTICE:
                vertices = []
                for vertice in cl[Obj.OFFSET :].split(Obj.SEPARADOR):
                    if vertice == "":
                        continue

                    vertices.append(float(vertice))

                vertices_ind.append(vertices)

            if tipo_l == Obj.COMIENZO_NORMAL:
                normales = []
                for normal in cl[Obj.OFFSET :].split(Obj.SEPARADOR):
                    if normal == "":
                        continue

                    normales.append(float(normal))

                normales_ind.append(normales)

            if tipo_l == Obj.COMIENZO_COLOR:
                colores = []
                for color in cl[Obj.OFFSET :].split(Obj.SEPARADOR):
                    if color == "":
                        continue

                    colores.append(float(color))

                colores_ind.append(colores)

            # Vértices sucesivos según posición
            elif tipo_l == Obj.COMIENZO_POSICION:
                for pos in cl[Obj.OFFSET :].split(Obj.SEPARADOR):
                    vert = pos
                    if ("/") in pos:
                        pair = pos.split("/")
                        vert = pair[0]
                        normal = pair[1]
                        if len(pair) > 2:
                            color = pair[2]

                        if len(normales_ind) > 0:
                            for n in normales_ind[int(normal) - 1]:
                                self.__normales.append(n)
                        # TODO: Ver esto bien, debería ser v/n/c, no v/[n/c]
                        if len(colores_ind) > 0:
                            for c in colores_ind[int(normal) - 1]:
                                self.__colores.append(c)
                    for v in vertices_ind[int(vert) - 1]:
                        self.__vertices.append(v)

            else:
                pass
