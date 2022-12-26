import pygame as pg
from random import randint
from math import sqrt


class Ball:
    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int, radius: int, colour, ball_number):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.x = randint(min_x, max_x)
        self.y = randint(min_y, max_y)
        self.ball_number = ball_number

        self.speed_x = randint(5, 10)
        self.speed_y = randint(3, 6)

        self.radius = radius
        self.colour = colour

        self.collided = False

    def draw(self, display: pg.Surface):
        pg.draw.circle(display, self.colour, (self.x, self.y), self.radius)

    def move(self):
        if self.x-self.radius <= self.min_x or self.x+self.radius >= self.max_x:
            self.speed_x *= -1
        if self.y-self.radius <= self.min_y or self.y+self.radius >= self.max_y:
            self.speed_y *= -1

        self.x += self.speed_x
        self.y += self.speed_y

    def get_harder(self):
        if self.speed_x > 0:
            self.speed_x += 1
        elif self.speed_x < 0:
            self.speed_x -= 1
        if self.speed_y > 0:
            self.speed_y += 1
        elif self.speed_y < 0:
            self.speed_y -= 1
        self.radius += 1

    def collide(self, player_x, player_y, player_radius):
        distance = sqrt((self.x-player_x)**2 + (self.y-player_y)**2)
        if distance <= self.radius+player_radius:
            self.collided = True
