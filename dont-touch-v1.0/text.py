import pygame as pg


class Text:
    def __init__(self, text, colour, display: pg.Surface, x, y):
        self.font = pg.font.SysFont('timesnewroman', 32)
        self.text = self.font.render(f'{text}', True, colour)
        display.blit(self.text, (x, y))
