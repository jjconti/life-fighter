#!/usr/bin/env python
# -*- coding: latin-1 -*-
"""
Starts Life Fighter.
"""

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

    #Create a grid and a game clock
    grid = Grid(n1, n2, x_off, y_off, step, line)
    clock = pygame.time.Clock()

    #Create main menu
    font1 = pygame.font.Font(FONT1, 40)
    font2 = pygame.font.Font(FONT1, 35)
    sound1 = load_sound(TYPEW1)
    sound2 = load_sound(TYPEW2)
    options = ["Jugar", "Salon de la fama", "Vida", "Editor", \
               "Configuracion", "Ayuda", "Salir"]
    menu = Menu(screen, background, font1, font2, color1, color2, sound1, sound2, options)

    #Create play menu
    font1 = pygame.font.Font(FONT1, 50)
    font2 = pygame.font.Font(FONT1, 45)
    options = ["Entrenamiento", "Cuenta pasos", "Contra Reloj", "Combinado", "Volver"]
    play = Menu(screen, background, font1, font2, color1, color2, sound1, sound2, options)

    #Create help menu
    options = ["El juego", "Reglas de evolucion", "Controles", "Creditos", "Volver"]
    help = Menu(screen, background, font1, font2, color1, color2, sound1, sound2, options)

    while True:
        
        op = menu.main_loop()

        if op == 0:
            op = play.main_loop()
            if op == 0:
                Train(clock, screen, background, grid).main_loop()
            elif op == 1:
                Moves(clock, screen, background, grid).main_loop()
            elif op == 2:
                Clock(clock, screen, background, grid).main_loop()
        elif op == 2:
            Life(clock, screen, background, grid).main_loop()
        elif op == 3:
            Editor(clock, screen, background, grid).main_loop()
        elif op == 5:
            op = help.main_loop()
        elif op == 6:
            sys.exit(0)

    #Create a game
    #game = Editor(clock, screen, background, grid)
    #game = Train(clock, screen, background, grid)
    #game = Moves(clock, screen, background, grid)
    #game = Clock(clock, screen, background, grid)
    #game.main_loop()
    
if __name__ == '__main__':
    main()