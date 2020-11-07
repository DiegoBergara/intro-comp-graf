import pygame
import time
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from utils import *
from ObjectParser import Obj
from Model import Animated_Model


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    text = loadTexture("./textures/knight.png")

    text_sword = loadTexture("./textures/weapon_k.png")

    anim2 = Animated_Model(10,40,"knight_stand",text)

    anim = Animated_Model(10,40,"weapon_k_stand",text_sword)

    floor = Obj()
    floor.load("./objs/floor.obj")
    floorText = loadTexture("./textures/floor_texture.jpg")

    glClearColor(1, 1, 1, 1)

    setup(800, 600)

    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True

       
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Camera position
        glTranslatef(0.0, 0.0, -50)
        glRotatef(15, 1, 0, 0)
        
       
        drawMultipleTriangles(floor.get_vertices(),floor.get_normales(),floor.get_texturas(), floorText)
        
        glRotatef(-90, 1, 0, 0)
        glRotatef(-90, 0, 0, 1)
        

        anim.draw()
        anim2.draw()




        pygame.display.flip()


    glDeleteTextures([text])
    pygame.quit()
    quit()


main()
