import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *

import numpy

def drawMultipleTriangles(vertices, normales, texturas, textura):
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glEnableClientState(GL_NORMAL_ARRAY)
    glNormalPointer(GL_FLOAT, 0, normales)
    glEnableClientState(GL_TEXTURE_COORD_ARRAY)
    glTexCoordPointer(2, GL_FLOAT, 0, texturas)

    glBindTexture(GL_TEXTURE_2D, textura)
    glDrawArrays(GL_TRIANGLES, 0, int(len(vertices)))
    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_NORMAL_ARRAY)
    glDisableClientState(GL_TEXTURE_COORD_ARRAY)
    glBindTexture(GL_TEXTURE_2D, 0)

def setup(ancho, largo):
    glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, [1,1,1,1])
    glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, [1,1,1,1])
    glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [1,1,1,1])
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 16)

    glEnable(GL_LIGHT0)
    glLight(GL_LIGHT0, GL_DIFFUSE, [1,1,1,1])
    glLight(GL_LIGHT0, GL_AMBIENT, [0.1,0.1,0.1,1])
    glLight(GL_LIGHT0, GL_POSITION, [0,0,0,1])
    glLight(GL_LIGHT0, GL_SPECULAR, [1,1,1,1])

    glEnable(GL_LIGHTING)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, ancho, largo)

    glFrustum(-1, 1, -1, 1, 1, 1000)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glFrontFace(GL_CW)
    glEnable(GL_TEXTURE_2D)
    glActiveTexture(GL_TEXTURE0)
    glMatrixMode(GL_MODELVIEW)

def drawTriangle(v1, v2, v3):
    verts = [
        v1,v2,v3
    ]

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, verts)
    glDrawArrays(GL_TRIANGLES, 0, 9)
    glDisableClientState(GL_VERTEX_ARRAY)

def drawTrianglesOneByOne(vertices):
    for trio in vertices:
        print(trio)
        drawTriangle(trio[0], trio[1], trio[2])

def loadTexture(path):
    # Cargo la imagen a memoria. pygame se hace cargo de decodificarla correctamente
    surf = pygame.image.load(path)
    surf = pygame.transform.flip(surf, False, True)
    # Obtengo la matriz de colores de la imagen en forma de un array binario
    # Le indico el formato en que quiero almacenar los datos (RGBA) y que invierta la matriz, para poder usarla correctamente con OpenGL
    image = pygame.image.tostring(surf, "RGBA", 1)
    # Obentego las dimensiones de la imagen
    ix, iy = surf.get_rect().size
    # Creo una textura vacia en memoria de video, y me quedo con el identificador (texid) para poder referenciarla
    texid = glGenTextures(1)
    # Activo esta nueva textura para poder cargarle informacion
    glBindTexture(GL_TEXTURE_2D, texid)
    # Seteo los tipos de filtro a usar para agrandar y achivar la textura
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    # Cargo la matriz de colores dentro de la textura
    # Los parametros que le paso son:
    # - Tipo de textura, en este caso GL_TEXTURE_2D
    # - Nivel de mipmap, en este caso 0 porque no estoy usando mas niveles
    # - Formato en que quiero almacenar los datos en memoria de video, GL_RGB en este caso, porque no necesito canal Alfa
    # - Ancho de la textura
    # - Alto de la textura
    # - Grosor en pixels del borde, en este caso 0 porque no quiero agregar borde a al imagen
    # - Formato de los datos de la imagen, en este caso GL_RGBA que es como lo leimos con pygame.image
    # - Formato de los canales de color, GL_UNSIGNED_BYTE quiere decir que son 8bits para cada canal
    # - La imagen, en este caso la matriz de colores que creamos con pygame.image.tostring
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)
    # Una vez que tengo todo cargado, desactivo la textura para evitar que se dibuje por error mas adelante
    # Cada vez que quiera usarla, puedo hacer glBindTexture con el identificador (texid) que me guarde al crearla
    glBindTexture(GL_TEXTURE_2D, 0)
    # devuelvo el identificador de la textura para que pueda ser usada mas adelante
    return texid

def before_draw(camera_angle, fov):
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -fov)
    glRotatef(15, 1, 0, 0)
    glRotatef(camera_angle, 0, 1, 0)