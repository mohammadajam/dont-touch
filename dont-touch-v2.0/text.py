import pygame as pg


class Text:
    def __init__(self, txt, display: pg.Surface, x: int, y: int, colour: tuple):
        self.font = pg.font.SysFont('timesnewroman', 32)
        self.text = self.font.render(f'{txt}', True, colour)
        display.blit(self.text, (x, y))
