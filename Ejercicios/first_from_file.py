import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from utils import *
from ObjectParser import *

def main():
    pygame.init()
    display = (800, 600)

    # Cargo Vertices
    obj_parser = Parser()

    obj_parser.agregar_obj("objs/dragon_10k.obj")

    # Prepara el canvas para openGL
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # Para que openGL sepa como convertir a pixeles
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, 800, 600)

    # Defino coordenadas para el plano de proyección
    glFrustum(-1, 1, -1, 1, 1, 10000)

    # Traslado para moverme del origen
    glTranslate(0,0,-1) # para knight
    glScalef(1,1,1)
    glRotatef(0.9, 1, 0, 0)
    ang = 0.0
   
    # Loop principal de pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Matriz mode
        glMatrixMode(GL_MODELVIEW)
        # Carga con matriz identidad, util para limpiar
        glLoadIdentity()

        # Roto (comentar para knight)
        # glRotatef(ang, 0, 1, 0)
        ang += 0.1
        ang += 4

        # Limpio canvas
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glRotatef(ang, 0, 1, 0)
        # glRotatef(ang, 0, 0, 1)
        glRotatef(-90, 1, 0, 0)

        # Leo vértices y dibujo triángulos
        drawMultipleTriangles(obj_parser.get_obj("objs/dragon_10k.obj").get_vertices(), obj_parser.get_obj("objs/dragon_10k.obj").get_normales(),obj_parser.get_obj("objs/dragon_10k.obj").get_colores() )
        
        #drawTrianglesOneByOne([obj_parser.get_obj("objs/box.obj").get_vertices()])

        # Flip buffers
        pygame.display.flip()

        # Small delay
        pygame.time.wait(10)

if __name__ == "__main__":
    main()