import pygame as pg
from random import randint
from math import sqrt


class Ball:
    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int, radius: int, colour: tuple):
        self.x_range: tuple = min_x, max_x
        self.y_range: tuple = min_y, max_y
        self.pos: list = [randint(self.x_range[0], self.x_range[1]), randint(self.y_range[0], self.y_range[1])]
        self.colour = colour # RGB
        self.radius = radius
        self.speed: list = [10, 10] # x, y

    def draw(self, display: pg.Surface):
        pg.draw.circle(display, self.colour, self.pos, self.radius)

    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
       
        if self.pos[0]-self.radius <= self.x_range[0] or self.pos[0]+self.radius >= self.x_range[1]:
            self.speed[0] *= -1

        if self.pos[1]-self.radius <= self.y_range[0] or self.pos[1]+self.radius >= self.y_range[1]:
            self.speed[1] *= -1

    def collide(self, player_pos, player_radius):
        dis = sqrt((self.pos[0]-player_pos[0])**2 + (self.pos[1]-player_pos[1])**2)
        if dis <= (self.radius + player_radius):
            return True
