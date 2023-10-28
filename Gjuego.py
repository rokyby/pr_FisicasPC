import pygame as pg
import moderngl as opgl
import glfw
from OpenGL.GL import *
import numpy as np
import sys


class ventana():
    
    def __init__(self):
        pg.init()         
        white=(255,255,255) 
        size=(600,600) 
        screen = pg.display.set_mode(size)
        self.screen = screen 
        self.black = (0,0,0)
        red = (255,0,0)
        blue = (0,0,255)
        green = (0,255,0)
        pg.display.set_caption("Fisicas")
        run = True
        while run:
            screen.fill(self.black)
            pg.draw.circle(screen,white,(300,300),30,100)
            pg.display.flip()  

   
ventana()