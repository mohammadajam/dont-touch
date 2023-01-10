import pygame as pg

class Player:
    def __init__(self, radius: int, colour: tuple):
        self.colour = colour
        pg.mouse.set_visible(False)
        self.radius = radius
    def draw(self, display: pg.surface, mouse_pos: tuple):
        pg.draw.circle(display, self.colour, mouse_pos, self.radius)
