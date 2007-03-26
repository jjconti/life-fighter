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

    #Package stages data
    sd = StageData()
    sd.clock = clock
    sd.screen = screen
    sd.bg = background
    sd.grid = Grid(n1, n2, x_off, y_off, step, line)

    #Menus data
    font0 = pygame.font.Font(FONT1, 65)
    font1 = pygame.font.Font(FONT1, 50)
    font2 = pygame.font.Font(FONT1, 45)
    font3 = pygame.font.Font(FONT1, 40)
    font4 = pygame.font.Font(FONT1, 35)
    sound1 = load_sound(TYPEW1)
    sound2 = load_sound(TYPEW2)

    #Menu functions

    def f_exit():
        sys.exit(0)

    def f_train():
        return Train(sd, True, f_play)

    def f_moves():
        return Moves(sd, False, f_play)

    def f_clock():
        return Clock(sd, False, f_play)

    def f_life():
        return Life(sd, f_main)

    def f_editor():
        return Editor(sd, f_main)

    def f_play():
        options = [("Entrenamiento", f_train),
                   ("Cuenta pasos", f_moves),
                   ("Contra Reloj", f_clock),
                   ("Combinado", None),
                   ("Volver", f_main),]
        
        return Menu(screen, background, font1, font2, font0, color1, color2, logo_color, \
                    sound1, sound2, "Jugar", options)

    def f_help():
        options = [("El juego", None),
                   ("Reglas de evolucion", None),
                   ("Controles", None),
                   ("Creditos", None),
                   ("Volver", f_main),]
        
        return Menu(screen, background, font1, font2, font0, color1, color2, logo_color, \
                sound1, sound2, "Ayuda", options)

    def f_main():
        options = [("Jugar", f_play),
                   ("Salon de la fama", None),
                   ("Vida", f_life),
                   ("Editor", f_editor),
                   ("Configuracion", None),
                   ("Ayuda", f_help),
                   ("Salir", f_exit),]
        
        return Menu(screen, background, font3, font4, font0, color1, color2, logo_color, \
                sound1, sound2, WINDOW_TITLE, options)


    f = f_main

    while f is not f_exit:
        op = f().main_loop()
        if op:
            f = op

    f()


if __name__ == '__main__':
    main()
