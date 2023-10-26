import pygame as pg
from pygame.locals import *
from sys import exit
from variables import *
from functions import *
from classes import *
from math import *

pg.init()
pg.mixer.music.load('./sounds/music.mp3')
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)

def main_menu():
    start_button = MMButton(395, 320, 200, 40, 'Começar', buttons, amarelo, laranja)
    quit_button = MMButton(455, 420, 80, 40, 'Sair', buttons, amarelo, laranja)

    while True:
        relogio.tick(30)
        mpos = pg.mouse.get_pos()
        tela.blit(MMbg, (0, 0))
        draw_text('FISQUETE', MTfont, laranja, tela, 270, 20)

        start_button.update(tela)
        quit_button.update(tela)

        click = False
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if start_button.rect.collidepoint(mpos) and click:
            game_start()
        if quit_button.rect.collidepoint(mpos) and click:
            pg.quit()
            exit()

        pg.display.flip()

def game_start():
    mapa_x = 0

    balls = pg.sprite.Group()
    cests = pg.sprite.Group()
    ball = Ball()
    cest = Cest(randint(1100, 8000), randint(200, 550))
    balls.add(ball)
    cests.add(cest)

    counter = 0
    seconds = 0
    minutes = 0

    throw_ball = False

    while True:
        relogio.tick(fps)
        for c in range(0, 1800, 450):
            for i in range(mapa_x, 9000 + mapa_x, 450):
                tela.blit(main_bg, (i, c))
        

        if not throw_ball:
            counter += 1
            if counter >= 60:
                seconds += 1
                counter = 0
            if seconds >= 60:
                minutes += 1
                seconds = -1

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    throw_ball = True
                    ball.shoot = True
                    ball.has_thrown = True
                    ball.mx, ball.my = pg.mouse.get_pos()

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    throw_ball = True
                    ball.shoot = True
                    ball.has_thrown = True
                    ball.mx, ball.my = pg.mouse.get_pos()

                if event.key == K_ESCAPE:
                    game_start()

        pg.draw.rect(tela, verde, (0, 700, 5000, 300))

        balls.draw(tela)
        balls.update(tela)
        cests.draw(tela)
        cests.update(tela, throw_ball, ball, mapa_x)

        if ball.shoot:
            mapa_x -= int(ball.xvel)

        #draw_text(f'ball v: {ball.yvel}', buttons, preto, tela, 700, 600)
        #draw_text(f'ball y: {ball.rect.y/100} m', buttons, preto, tela, 700, 700)
        
        pg.display.flip()

main_menu()