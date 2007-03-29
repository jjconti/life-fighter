# -*- coding: latin-1 -*-

# The TextPanel class was originally develop by Juan José Conti <jjconti@gnu.org>
# for Life Fighter game. It is intentionally placed in a separeted file so you
# can use it if it's fine for you. If not you can improve it :-)
# Please use it under GPL licence like the rest of the game.

# I am sorry. I have no include exausted controls here, so be carefull with the size
# of the images you use.

#import os
import sys

import pygame
from pygame.locals import *

class TextPanel(object):
    '''A generic TextPanel for showing text information.'''

    def __init__(self, hd, title, lines, f_father):
        '''font1 will be used for the title and font2 for the text in lines:
        ["this is text for one line", "this for a second one", .. ]'''
        self.screen = hd.screen
        self.done = False
        self.font = hd.font2
        self.color = hd.color2
        self.lines = lines
        self.hor_step = hd.font2.get_height()
        self.clock = pygame.time.Clock()
        self.f_father = f_father
        
        #self.screen.blit(self.background, (0,0))
        title_img = hd.font1.render(title, True, hd.color1)
        topleft = (hd.bg.get_rect().width - title_img.get_rect().width) / 2, 30
        bg = hd.bg.copy()
        bg.blit(title_img, topleft)
        self.background = bg

    def main_loop(self):

        while not self.done:

            self.clock.tick(10)

            self.screen.blit(self.background, (0,0))    

            for event in pygame.event.get():
                self.control(event)

            self._draw_lines()
            pygame.display.flip()

        return self.f_father
            

    def control(self, event):
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key in (K_SPACE, K_RETURN, K_KP_ENTER, K_DOWN):
                self.next()
            elif event.key in (K_UP, K_BACKSPACE):
                self.prev()
            elif event.key == K_ESCAPE:
                self.back()
        if event.type == MOUSEBUTTONDOWN:
            self.next()

    def _draw_lines(self):
        y = self.hor_step + 100 # Tune this value as you need
        for line in self.lines:
            line_img = self.font.render(line, True,self.color)
            x = (self.screen.get_width() - line_img.get_width()) / 2
            self.screen.blit(line_img, (x,y))
            
            y += self.hor_step

    def next(self):
        pass

    def prev(self):
        pass

    def back(self):
        self.done = True

                   
def main():
    '''Test the TextPanel class'''

    FONT1 = None

    white = (250, 250, 250)
    color1 = (200, 0, 0)
    color2 = (0, 100, 50)

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    #background = pygame.image.load(os.path.join("data", "imgs", "bg2.png"))
    background = pygame.Surface((800,600))
    background.fill(white)
    font1 = pygame.font.Font(FONT1, 60)
    font2 = pygame.font.Font(FONT1, 40)

    lines = ["This is a test for the", "TextPanel class.", "Coded by Juanjo Conti", "jjconti@gnu.org"]

    panel = TextPanel(screen, background, font1, font2, color1, color2, "Title", lines)

    panel.main_loop()
        
if __name__ == "__main__":
    main()
