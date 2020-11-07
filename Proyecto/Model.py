import time
from utils import *
from ObjectParser import Obj


class Animated_Model:
    objs = []
    frames = 0
    qty = 0
    current_frame = 0
    text = ""
    init_time = 0

    def __init__(self, frames, qty, name, text):
        self.init_time = time.time()
        self.frames = frames
        self.qty = qty
        self.text = text
        for i in range(qty):
            obj = Obj()
            obj.load(f"./objs/{name}_{i}.obj")
            self.objs.append(obj)
    
    def draw(self):
        frame = int((time.time() - self.init_time) * self.frames % self.qty)
        model = self.objs[frame]
        drawMultipleTriangles(model.get_vertices(),model.get_normales(),model.get_texturas(), self.text)

