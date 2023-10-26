import pygame as pg
from pygame.locals import *
from sys import exit
from variables import *
from functions import *
from random import randint

class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('./images/ball.png'), (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(100, 500), randint(100, 600))
        self.xvel = 0
        self.yvel = 0
        self.gravity = 1

    def update(self):
        self.rect.y += self.yvel
        self.yvel += self.gravity
        if self.rect.y >= 520:
            self.yvel *= -1

def game_start():
    mapa_x = 0

    balls = pg.sprite.Group()
    ball = Ball()
    balls.add(ball)

    while True:
        relogio.tick(fps)
        for c in range(0, 1800, 450):
            for i in range(mapa_x, 9000 + mapa_x, 450):
                tela.blit(main_bg, (i, c))

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.draw.rect(tela, verde, (0, 600, largura, 200))

        balls.draw(tela)
        balls.update()

        draw_text(f'ball v: {ball.yvel}', buttons, preto, tela, 700, 600)

        pg.display.flip()

game_start()
        