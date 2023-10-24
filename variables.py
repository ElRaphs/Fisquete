import pygame as pg

pg.init()

fps = 60
largura, altura = 1000, 800
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Fisquete')
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

MMbg = pg.transform.scale(pg.image.load('./images/MMbg.jpg'), (largura, altura))