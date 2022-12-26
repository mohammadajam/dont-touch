import pygame as pg


class Pointer:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour

    def draw(self, display: pg.Surface, mouse_pos):
        pg.draw.circle(display, self.colour, mouse_pos, self.radius)
