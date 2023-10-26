import pygame as pg
from random import randint
from functions import *
from variables import *
from math import *

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
        #pg.draw.rect(screen, (255, 0, 0), self.rect)

        if self.rect.collidepoint(mpos):
            GColor = self.color2
        else:
            GColor = self.color1

        draw_text(self.text, self.font, GColor, screen, self.rect.x, self.rect.y-5)

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('./images/ball.png'), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(100, 500), randint(100, 500))
        self.gravity = 0
        self.shoot = False
        self.velocity = 0
        self.direction = 0
        self.cx = 0
        self.cy = 0
        self.mx = 0
        self.my = 0
        self.xvel = 0
        self.yvel = 0

    def update(self, screen):
        
        self.rect.y += self.yvel
        #self.rect.x += self.xvel
        self.yvel += self.gravity
        if self.rect.y >= 620:
            self.yvel *= -1
        if not self.shoot:
            self.mx, self.my = pg.mouse.get_pos()
            pg.draw.line(screen, vermelho, self.rect.center, (self.mx, self.my), 3)
            pg.draw.line(screen, preto, self.rect.center, (self.rect.centerx, self.rect.centery-150), 5)
            pg.draw.line(screen, preto, self.rect.center, (self.rect.centerx+150, self.rect.centery), 5)
            draw_text('y', eixos, preto, screen, self.rect.centerx-20, self.rect.centery-150)
            draw_text('x', eixos, preto, screen, self.rect.centerx+150, self.rect.centery)
            
            self.cx = self.mx-self.rect.centerx
            self.cy = self.rect.centery-self.my
            
            if self.mx-self.rect.centerx != 0:
                angulo_rad = atan(self.cy/self.cx)
            else:
                angulo_rad = pi/2

            angulo_graus = (180/pi) * angulo_rad

            draw_text(f'{angulo_graus:.2f}°', eixos, vermelho, screen, self.rect.centerx+30, self.rect.centery-30)
            self.velocity = sqrt(((self.cx)**2)+((self.cy)**2))/100
            draw_text(f'v = {(self.velocity):.2f} m/s', eixos, preto, screen, self.mx, self.my-30)
            pg.draw.line(screen, preto, (self.rect.centerx, self.rect.centery), (self.rect.centerx, 700))
            draw_text(f'h = {(700-self.rect.centery)/100} m', eixos, preto, screen, self.rect.centerx+30, self.rect.centery+200)
            self.direction = atan(self.cy/self.cx)
            
        else:        
            self.gravity = 0.27
            self.xvel = self.velocity*10*cos(self.direction)

class Cest(pg.sprite.Sprite):
    def __init__(self, posx, posy):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('./images/cesta.jpg'), (150, 150))
        self.image.set_colorkey(branco)
        self.rect = self.image.get_rect()
        self.posx = posx
        self.rect.center = (self.posx, posy)


    def update(self, screen, throw, ball, mapx):
        self.rect.x = self.posx + mapx
        if not throw:
            draw_text(f'd = {(self.rect.centerx-ball.rect.centerx)/100} m -->', eixos, preto, screen, largura-150, self.rect.centery)
            draw_text(f'h = {(700-self.rect.centery)/100} m -->', eixos, preto, screen, largura-150, self.rect.centery+20)

            


