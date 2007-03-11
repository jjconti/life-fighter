#!/usr/bin/env python
# -*- coding: latin-1 -*-
'''
Starts Life Fighter.
'''

#Import Modules
import pygame
from pygame.locals import *
del pygame.movieext

from settings import *
from utils import *
from life import Grid
from stages import *
from menu import Menu

import sys

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(WINDOW_TITLE)
    icon = load_image(ICON)
    pygame.display.set_icon(icon)

    background = load_image(BGIMAGE1)
    screen.blit(background, (0, 0))

    #Create the game clock
    clock = pygame.time.Clock()

    #Create main menu
    font1 = pygame.font.Font(FONT1, 40)
    font2 = pygame.font.Font(FONT1, 35)
    font_title = pygame.font.Font(FONT1, 65)
    sound1 = load_sound(TYPEW1)
    sound2 = load_sound(TYPEW2)
    options = ["Jugar", "Salon de la fama", "Vida", "Editor", \
               "Configuracion", "Ayuda", "Salir"]
    menu = Menu(screen, background, font1, font2, font_title, color1, color2, logo_color, \
                sound1, sound2, WINDOW_TITLE, options)

    #Create play menu
    font1 = pygame.font.Font(FONT1, 50)
    font2 = pygame.font.Font(FONT1, 45)
    options = ["Entrenamiento", "Cuenta pasos", "Contra Reloj", "Combinado", "Volver"]
    play = Menu(screen, background, font1, font2, font_title, color1, color2, logo_color, \
                sound1, sound2, "Jugar", options)

    #Create help menu
    options = ["El juego", "Reglas de evolucion", "Controles", "Creditos", "Volver"]
    help = Menu(screen, background, font1, font2, font_title, color1, color2, logo_color, \
                sound1, sound2, "Ayuda", options)

    while True:
        #Refactoring needed..
        op = menu.main_loop()

        if op == 0:
            p = True
            while p:
                op = play.main_loop()
                if op == 0:
                    Train(clock, screen, background, Grid(n1, n2, x_off, y_off, step, line)\
                          ).main_loop()
                elif op == 1:
                    Moves(clock, screen, background, Grid(n1, n2, x_off, y_off, step, line)\
                          ).main_loop()
                elif op == 2:
                    Clock(clock, screen, background, Grid(n1, n2, x_off, y_off, step, line)\
                          ).main_loop()
                elif op == 4:
                    p = False
        elif op == 2:
            Life(clock, screen, background, Grid(n1, n2, x_off, y_off, step, line)\
                 ).main_loop()
        elif op == 3:
            Editor(clock, screen, background, Grid(n1, n2, x_off, y_off, step, line)\
                   ).main_loop()
        elif op == 5:
            op = help.main_loop()
        elif op == 6:
            sys.exit(0)

if __name__ == '__main__':
    main()
