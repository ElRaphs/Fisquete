import pygame as pg
from functions import *

class MMButton:
    def __init__(self, xpos, ypos, w, h, text, font, Color1, Color2):
        self.text = text
        self.font = font
        self.rect = pg.Rect(xpos, ypos, w, h)
        self.color1 = Color1
        self.color2 = Color2
   
    def update(self, screen):
        mpos = pg.mouse.get_pos()
        GColor = self.color1
        pg.draw.rect(screen, (255, 0, 0), self.rect)

        if self.rect.collidepoint(mpos):
            GColor = self.color2
        else:
            GColor = self.color1

        draw_text(self.text, self.font, GColor, screen, self.rect.x+5, self.rect.y+5)