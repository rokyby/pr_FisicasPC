import pygame as pg
import moderngl as opgl
#import glfw
#from OpenGL.GL import *
import numpy as np
import sys

#pg.init() 
size=(600,600) 
screen = pg.display.set_mode(size)
run = True
pg.display.set_caption("Fisicas")
particulaTamano = 23
class obj():
    
    def __init__(self,pos,radio,masa,tamano,rapidez,ang):
        self.pos = pos
        self.radio = radio
        self.masa = masa
        self.tamano = tamano
        self.ang = ang
        self.u = np.array([[np.cos(self.ang)],
                           [np.sin(self.ang)]])
        self.rapidez = rapidez 
        self.v = self.rapidez * self.u
    def mov(self):   
       pg.draw.circle(screen,white,(self.pos[0][0], self.pos[1][0]),self.tamano) 
    def moverse(self):
        self.pos = self.pos + self.v

matriz = np.array([[0,-1],
                   [1,0]])
def chocar(partic1, partic2):
    r12 = partic2.pos - partic1.pos
    dist_part12 = np.linalg.norm(r12)
    if dist_part12 <= (partic1.radio + partic2.radio):
        tg = r12 / np.linalg.norm(r12)
        n = np.dot(matriz, tg)
        rapi1tg_ia = np.dot(partic1.v.T, tg)
        rapi1n_ia = np.dot(partic1.v.T, n)
        rapi2tg_ia = np.dot(partic2.v.T, tg)
        rapi2n_ia = np.dot(partic2.v.T, n)
        rapi1tg_id = (2 * partic2.masa / (partic1.masa + partic2.masa)) * rapi2tg_ia + \
                     ((partic1.masa - partic2.masa) / (partic1.masa + partic2.masa)) * rapi1tg_ia
        rapi2tg_id = (2 * partic1.masa / (partic1.masa + partic2.masa)) * rapi1tg_ia + \
                     ((partic2.masa - partic1.masa) / (partic1.masa + partic2.masa)) * rapi2tg_ia
        rapi1n_id = rapi1n_ia
        rapi2n_id = rapi2n_ia
        partic1.v = rapi1tg_id * tg + rapi1n_id * n
        partic2.v = rapi2tg_id * tg + rapi2n_id * n
        partic1.rapi = np.linalg.norm(partic1.v)
        partic2.rapi = np.linalg.norm(partic2.v)
        partic1.pos = partic1.pos + partic1.v * 0.1
        partic2.pos = partic2.pos + partic2.v * 0.1
"""def chocar(rad1,rad2):
    r12 = rad1.pos - rad2.pos
    dis_12 = np.linalg.norm(r12)
    if dis_12 <= (rad1.radio + rad2.radio):
        print("choque")
        tg = r12 / np.linalg.norm(r12)
        n = np.dot(matriz,tg)
        ra1_a = np.dot(part1.v.T, tg)
        ra1_a1 = np.dot(part1.v.T, n)
        ra2_a = np.dot(part2.v.T, tg)
        ra2_a1 = np.dot(part2.v.T, n)
        rapi1tg_id = (2 * part2.masa / (part1.masa + part2.masa)) * ra2_a + \
                     ((part1.masa - part2.masa) / (part1.masa + part2.masa)) * ra1_a
        rapi2tg_id = (2 * part1.masa / (part1.masa + part2.masa)) * ra2_a1 + \
                     ((part2.masa - part1.masa) / (part1.masa + part2.masa)) * ra1_a1
        rapi1n_id = ra1_a1
        rapi2n_id = ra2_a1
        part1.v = rapi1tg_id * tg + rapi1n_id * n
        part2.v = rapi2tg_id * tg + rapi2n_id * n
        part1.pos = part1.pos + part1.v * 0.1
        part2.pos = part2.pos + part2.v * 0.1
#parti1_pos = (300,300)"""
parti1_pos = np.array([[300],
                       [100]])
parti1_rad = particulaTamano
parti1_mas = 12
parti1_tam = particulaTamano
parti1_rap = 0.1
parti1_ang = np.pi/2
part1 = obj(parti1_pos,parti1_rad,parti1_mas,parti1_tam,parti1_rap,parti1_ang)        

parti2_pos = np.array([[300],
                       [500]])
parti2_rad = particulaTamano
parti2_mas = 45435
parti2_tam = particulaTamano
parti2_rap = 0.1
parti2_ang = -np.pi/2
part2 = obj(parti2_pos,parti2_rad,parti2_mas,parti2_tam,parti2_rap,parti2_ang)

black = (0,0,0)
white=(255,255,255) 
class inicio(): 
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        # Modificar la variable 'rapidez' según lo que desees
        #part1.rapidez = 0.1  # Cambia el valor de 'rapidez' según tus necesidades
        #part2.rapidez = 0.1
        # Actualizar la velocidad del objeto 'part1' con base en 'rapidez'
        #part1.v = part1.rapidez * part1.u
        #part2.v = part2.rapidez * part2.u
        chocar(part1,part2)
        # Mover el objeto
        part1.moverse()
        part2.moverse()
        
        # Resto del código
        screen.fill(black)
        part1.mov()
        part2.mov()
        pg.display.flip()

    pg.quit()
    sys.exit()
        


 

