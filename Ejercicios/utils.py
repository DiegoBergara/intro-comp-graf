import pygame
from pygame.locals import *

from OpenGL.GL import *
import numpy

def drawMultipleTriangles(vertices, normals, colors):

    if len(vertices) > 0:
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)

    if len(normals) > 0:
        glEnableClientState(GL_NORMAL_ARRAY)
        glNormalPointer(GL_FLOAT, 0, normals)

    if len(colors) > 0:
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(3, GL_FLOAT, 0, colors)

    glDrawArrays(GL_TRIANGLES, 0, int(len(vertices) / 3))

    if len(vertices) > 0:
        glDisableClientState(GL_VERTEX_ARRAY)

    if len(normals) > 0:
        glDisableClientState(GL_NORMAL_ARRAY)

    if len(colors) > 0:
        glDisableClientState(GL_COLOR_ARRAY)

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

