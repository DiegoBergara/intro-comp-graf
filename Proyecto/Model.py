import time
from utils import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from ObjectParser import Obj


class Animation:
    def __init__(self, frames, qty, name,directory):
        self.init_time = time.time()
        self.frames = frames
        self.qty = qty
        self.directory = directory
        self.name = name
        self.objs=[]
        self.current_frame=0
       
        for i in range(qty):
            obj = Obj()
            obj_dir = f"{directory}/{name}_{i}.obj" 
            obj.load(obj_dir)
            self.objs.append(obj)
    
    def draw(self, text):
        frame = int((time.time() - self.init_time) * self.frames % self.qty)
        model = self.objs[frame]
        drawMultipleTriangles(model.get_vertices(),model.get_normales(),model.get_texturas(), text)


class Model:
    def __init__(self, animations, texture, directory):
        self.texture = texture
        self.animations = []
        print(animations)
        for elem in animations:
            anim = Animation(elem["frames"], elem["qty"], elem["name"],directory)
            self.animations.append(anim)

    def draw_animation (self, action, camera_angle, fov, direction):
        before_draw(camera_angle, fov)
        if direction == 0:
            glRotatef(-90, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
        elif direction == 1:
            glRotatef(90, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
        elif direction == 3:
            glRotatef(-180, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
        elif direction == 2:
            glRotatef(0, 0, 1, 0)
            glRotatef(-90, 1, 0, 0)
        self.animations[action].draw(self.texture)
        
class Static:
    def __init__(self, name, texture, obj_directory):
        self.name = name
        self.texture = texture
        self.x=0
        self.y=0
        obj = Obj()
        obj_dir = f"{obj_directory}/{name}.obj" 
        obj.load(obj_dir)
        self.obj = obj
    
    def draw(self, camera_angle, fov, walking, direction):
        before_draw(camera_angle,fov)
        if (walking):
            if direction == 0:
                self.x -=1
            elif direction == 1:
                self.x +=1
            elif direction == 3:
                self.y +=1
            elif direction == 2:
                self.y -=1
        glTranslate(self.y,0,self.x)
        drawMultipleTriangles(self.obj.get_vertices(),self.obj.get_normales(),self.obj.get_texturas(), self.texture)
