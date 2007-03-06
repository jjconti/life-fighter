#Import Modules 
import os

import pygame
from pygame.locals import *

from settings import *

#Defined values
DEAD = 0
ALIVE = 1

#Clsses definition
class Cell(pygame.sprite.Sprite):
    '''A life cell'''
    
    def __init__(self, grid, state, x_off, y_off, i, j):        
        pygame.sprite.Sprite.__init__(self)
	self.state = state
	self.next_state = state
        self.grid = grid
        self.color = cell_color
        step = self.grid.step
        self._image()
        self.rect = self.image.get_rect()      
        self.rect.x = x_off + i * step
        self.rect.y = y_off + j * step

    def __str__(self):
        return str(self.state)
		
    def get_state(self):
	return self.state

    def is_alive(self):
        return self.state == ALIVE
	    
    def set_next_state(self, state):
	self.next_state = state

    def birth(self):
        self.set_next_state(ALIVE)

    def birth_now(self):
        self.state = ALIVE
        self.next_state = ALIVE
        self._image()

    def die(self):
        self.set_next_state(DEAD)

    def die_now(self):
        self.state = DEAD
        self.next_state = DEAD
        self._image()
		
    def update_state(self):
	self.state = self.next_state
        self._image()
        
    def _image(self):
        step = self.grid.step
        self.image = pygame.Surface((step, step))
        self.image.set_colorkey(bg_color)
        self.image.fill(bg_color)
        if self.is_alive():
            pos = (step/2 + 1,step/2 + 1)
            radius = int(0.4 * step)
            pygame.draw.circle(self.image, self.color, pos, radius, 0)
            self.image.set_alpha(150)

    def be_hero(self):
        self.color = hero_color
        self.birth_now()

    def be_normal(self):
        self.color = cell_color
        self.die_now()


class Grid(pygame.sprite.Sprite):
    '''A life grid'''

    def __init__(self, columns, rows, x_off, y_off, step, line):
        pygame.sprite.Sprite.__init__(self)
	self.columns = columns
	self.rows = rows
        self.step = step
	self.cells = {}

	for i in range(columns):
            for j in range(rows):
                self.cells[i,j] = Cell(self, DEAD, x_off, y_off, i, j)

        self.hero_alive = False

        self.rect = Rect(x_off, y_off, step * columns, step * rows)
        self.image = pygame.Surface((self.rect.width, self.rect.height))
        self.image.set_colorkey(bg_color)
        self.image.fill(bg_color)
        r = Rect(0, 0, step * columns, step * rows)
        pygame.draw.rect(self.image, grid_color, r, line)

        for i in range(step, step * columns, step):
            start = (i, line)
            end = (i, step * rows +line - 1)
            pygame.draw.line(self.image, grid_color, start, end, line)

        for i in range(step, step * rows, step):
            start = (line, i)
            end = (step * columns + line - 1, i)
            pygame.draw.line(self.image, grid_color, start, end, line)

    def __str__(self):
        s = ""
        for j in range(self.rows):
            for i in range(self.columns):
                s += str(self.cells[i,j])
            s += "\n"
        return s
				
    def add_cells(self, cells):
        '''cells is a dict of Cells'''
	for k in cells:
            self.cells[k] = cells[k]

    def add_living_cells(self, cells):
        '''cells is a list of tuples i,j'''
        for k in cells:
            self.cells[k].birth_now()

    def alive_neights(self, i, j):
	t = [(-1,-1), (0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
	count = 0
	for o,p in t:
            try:
                count += self.cells[i+o,j+p].get_state()
            except KeyError:
                pass
	return count

    def beat(self):
        cells = self.cells

	for i,j in cells:
            n = self.alive_neights(i,j)
	    c = cells[i,j]
	    if c.is_alive():
		if n <= 1 or n >= 4: c.die()
	    else:
		if n == 3: c.birth()

        for k in cells:
            cells[k].update_state()

        #Update hero situation in needed
        if self.is_hero_alive() and not self.cells[self.i, self.j].is_alive():
            self.cells[self.i, self.j].color = cell_color
            self.hero_alive = False
        

    def set_hero(self, i, j):
        if self.cells[i,j].is_alive():
            self.i = i
            self.j = j
            self.cells[i,j].be_hero()
            self.hero_alive = True
            
    def get_hero(self):
        return (self.i, self.j)

    def is_hero_alive(self):
        return self.hero_alive

    def hero_left(self):
        i,j = self.i, self.j
        if self.is_hero_alive() and i > 0 and not self.cells[i-1,j].is_alive():
            self.cells[i,j].be_normal()
            i -= 1
            self.cells[i,j].be_hero()
            self.i, self.j = i,j

    def hero_right(self):
        i,j = self.i, self.j
        if self.is_hero_alive() and i < self.columns - 1 \
                                and not self.cells[i+1,j].is_alive():
            self.cells[i,j].be_normal()
            i += 1
            self.cells[i,j].be_hero()
            self.i, self.j = i,j
            
    def hero_up(self):
        i,j = self.i, self.j
        if self.is_hero_alive() and j > 0 and not self.cells[i,j-1].is_alive():
            self.cells[i,j].be_normal()
            j -= 1
            self.cells[i,j].be_hero()
            self.i, self.j = i,j
            
    def hero_down(self):
        i,j = self.i, self.j
        if self.is_hero_alive() and j < self.rows - 1 and not self.cells[i,j+1].is_alive():
            self.cells[i,j].be_normal()
            j += 1
            self.cells[i,j].be_hero()
            self.i, self.j = i,j

    def kill_all(self):
        for k in self.cells:
            self.cells[k].die_now()

    def alive_cells(self):
        return len([c for c in self.cells.values() if c.is_alive()])


class Pattern(object):

    def __init__(self, name, kind, period, cells):
        self.name = name
        self.kind = kind
        self.period = period
        self.alive_cells = cells