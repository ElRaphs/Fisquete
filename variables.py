import pygame as pg

pg.init()

fps = 60
largura, altura = 1000, 800
icon = pg.transform.scale(pg.image.load('./images/ball.png'), (16, 16))
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Fisquete')
pg.display.set_icon(icon)
relogio = pg.time.Clock()

branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
azul = (0, 0, 255)
amarelo = (242, 231, 0)
rosa = (236, 0, 242)
cinza = (150, 150, 150)
preto = (0, 0, 0)
azul_claro = (153, 217, 234)
verde_escuro = (34, 177, 76)
laranja = (249, 118, 0)
roxo = (166, 20, 182)

MTfont = pg.font.Font('./fonts/main_title.ttf', 100)
buttons = pg.font.Font('./fonts/geral.ttf', 50)
eixos = pg.font.Font('./fonts/geral.ttf', 20)

MMbg = pg.transform.scale(pg.image.load('./images/MMbg.jpg'), (largura, altura))
main_bg = pg.image.load('./images/game_bg.jpg')


