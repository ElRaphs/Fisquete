import pygame as pg
from pygame.locals import *
from sys import exit
from variables import *
from functions import *
from classes import *

pg.init()

def main_menu():
    start_button = MMButton(400, 350, 150, 50, 'Começar', buttons, amarelo, laranja)

    while True:
        relogio.tick(30)
        tela.blit(MMbg, (0, 0))
        draw_text('FISQUETE', MTfont, laranja, tela, 270, 20)

        start_button.update(tela)

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                exit()

        pg.display.flip()

main_menu()