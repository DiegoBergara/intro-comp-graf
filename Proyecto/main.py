import pygame, time, json
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from utils import *
from ObjectParser import Obj
from Model import Model, Static


def main():
    ARCHIVO_CONFIG = "./config/config.json"
    # Load Config
    with open(ARCHIVO_CONFIG, "r") as c:
        cf = c.read()
        config = json.loads(cf)

    display = tuple(config["display"])
    fov = config["fov"]
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    #Load textures
    texture_directory = config["directory"]["textures"]
    texture_knight = loadTexture(f'{texture_directory}/{config["models"]["knight"]["text"]}')
    texture_weapon = loadTexture(f'{texture_directory}/{config["models"]["weapon"]["text"]}')
    texture_floor = loadTexture(f'{texture_directory}/{config["map"]["floor"]["text"]}')

    # Load Models
    obj_directory = config["directory"]["objs"]
    weapon = Model(config["models"]["weapon"]["animations"],texture_weapon,obj_directory)
    knight = Model(config["models"]["knight"]["animations"],texture_knight,obj_directory)

    #Load Map
    floor = Static(config["map"]["floor"]["name"], texture_floor, obj_directory)

    glClearColor(1, 1, 1, 1)

    setup(display[0], display[1])
    
    # loop control
    end = False
    # camera angle
    camera_angle = 0
    # animation index
    animation_index = 0
    # walking
    walking = False 
    # facing direction
    direction = 0
    # show weapon
    show_weapon = True

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                animation_index = 0
                walking = False
                show_weapon = True
            if event.type == pygame.KEYDOWN:
                # Finaliza el programa
                if event.key == pygame.K_ESCAPE:
                    end = True
                if event.key == pygame.K_SPACE:
                    walking = False
                    animation_index = 2
                    show_weapon = False
                if event.key == pygame.K_w:
                    animation_index=1
                    walking = True
                    direction = 1
                if event.key == pygame.K_a:
                    animation_index=1
                    walking = True
                    direction = 3
                if event.key == pygame.K_s:
                    animation_index=1
                    walking = True
                    direction = 0
                if event.key == pygame.K_d:
                    animation_index=1
                    walking = True
                    direction = 2
                if event.key == pygame.K_1:
                    animation_index=5
                    show_weapon = False
                if event.key == pygame.K_2:
                    animation_index=6
                    show_weapon = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    animation_index = 3
                if event.button == 3:
                    animation_index = 4
                if event.button == 4:
                    if fov + 5 < 160:
                        fov += 5.0
                if event.button == 5:
                    if fov - 5 > 30:
                        fov -= 5.0
                
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        mouse_position = pygame.mouse.get_rel()
        camera_angle += mouse_position[0]
        
        # Draw Floor
        floor.draw(camera_angle, fov, walking, direction)

        # Draw Knigth and Weapon
        if show_weapon :
            weapon.draw_animation(animation_index, camera_angle, fov, direction)

        knight.draw_animation(animation_index, camera_angle, fov, direction)

        # Display Refresh
        pygame.display.flip()

        pygame.time.wait(10)

    
    glDeleteTextures([texture_knight, texture_weapon, texture_floor])         
    pygame.quit()
    quit()


main()
