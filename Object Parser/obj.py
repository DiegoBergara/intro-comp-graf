class Obj:
    '''
    Clase que representa un objeto (.obj)
    Contiene sus vértices, normales y colores
    '''

    # Separador de los vértices en archivos obj
    SEPARADOR = " "

    # Caracter que indica el comienzo de un vértice
    COMIENZO_VERTICE = "v"

    # Caracter que indica el comienzo de una normal
    COMIENZO_NORMAL = "vn"

    # Caracter que indica el comienzo de un color
    COMIENZO_COLOR = "vt"

    # Caracter que indica el comienzo de una posición
    COMIENZO_POSICION = "f"

    # Separación del caracter inicial y los datos
    OFFSET = 2

    def __init__(self):
        '''
        Constructor por defecto de la clase
        '''
        self.__vertices = []
        self.__normales = []
        self.__colores = []

    def get_vertices(self):
        '''
        Retorna lista con los vértices del objeto
        '''
        return self.__vertices

    def get_normales(self):
        '''
        Retorna lista con las normales del objeto
        '''
        return self.__normales

    def get_colores(self): 
        '''
        Retorna lista con los colores del objeto
        '''
        return self.__colores

    def cargar(self, archivo):
        '''
        "Parsea" un archivo .obj definiéndole
        sus vértices, normales y colores
        '''
        # Almacena los vértices intermedios (mapeados con "v")
        # Luego se agregan sucesivamente a la lista de vértices del objeto
        vertices_ind = []

        # Almacena las normales intermediass (mapeadas con "vn")
        # Luego se agregan sucesivamente a la lista de vértices del objeto
        normales_ind = []

        # Almacena los colores intermedios (mapeadas con "vt")
        # Luego se agregan sucesivamente a la lista de colores del objeto
        colores_ind = []

        for line in open(archivo):
            cl = line.strip()
            if (cl == ""):
                continue
            # tipo_l = cl[0:2]
            tipo_l = cl.split(" ")[0]

            # Vértices intermedios
            if (tipo_l == Obj.COMIENZO_VERTICE):
                # Lista para almacenar el trío de vértices
                vertices = []
                for vertice in cl[Obj.OFFSET:].split(Obj.SEPARADOR):
                    if (vertice == ""):
                        continue
                    # Agrego cada vértice
                    vertices.append(float(vertice))
                # Agrego el trío a la lista de vértices intermedios
                vertices_ind.append(vertices)

            # Normales intermadias
            if (tipo_l == Obj.COMIENZO_NORMAL):
                # Lista para almacenar el trío de normales
                normales = []
                for normal in cl[Obj.OFFSET:].split(Obj.SEPARADOR):
                    if (normal == ""):
                        continue
                    # Agrego cada normal
                    normales.append(float(normal))
                # Agrego el trío a la lista de normales intermedias
                normales_ind.append(normales)

            # Colores intermadios
            if (tipo_l == Obj.COMIENZO_COLOR):
                # Lista para almacenar el trío de colores
                colores = []
                for color in cl[Obj.OFFSET:].split(Obj.SEPARADOR):
                    if (color == ""):
                        continue
                    # Agrego cada color
                    colores.append(float(color))
                # Agrego el trío a la lista de colores intermedios
                colores_ind.append(colores)

            # Vértices sucesivos según posición
            elif (tipo_l == Obj.COMIENZO_POSICION):
                for pos in cl[Obj.OFFSET:].split(Obj.SEPARADOR):
                    # Separo vértices de normales
                    vert = pos
                    if ("/") in pos:
                        pair = pos.split("/")
                        vert = pair[0]
                        normal = pair[1]
                        if (len(pair) > 2):
                            color = pair[2]
                        # Agrego sucesivamente cada normal
                        if (len(normales_ind) > 0):
                            for n in normales_ind[int(normal)-1]:
                                self.__normales.append(n)
                        # Agrego sucesivamente cada color
                        # TODO: Ver esto bien, debería ser v/n/c, no v/[n/c]
                        if (len(colores_ind) > 0):
                            for c in colores_ind[int(normal)-1]:
                                self.__colores.append(c)
                    # IMPORTANTE: Sólo se utilizan con glDrawArrays()
                    # Agrego sucesivamente cada vértice
                    for v in vertices_ind[int(vert)-1]:
                        self.__vertices.append(v)

            # Otros
            else:
                pass # ignorar lo demás (por ahora)