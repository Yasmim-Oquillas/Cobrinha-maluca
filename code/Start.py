from ctypes import windll

from pygame.examples.playmus import Window

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Entity import Entity
import pygame as pg
from pygame import Surface, Rect


class Start:
    def __init__(self, window, name):
        pg.init()
        window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.window = window
        self.name = name

    def run(self,):
        pg.mixer_music.load('./asset/musica_manu.mp3')
        pg.mixer_music.play(-1)
        while True:
            #self.window.blit(source=self.surf, dest=self.rect)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # close window
                    quit()  # end pygame
            pg.display.flip()
            pg.draw.rect("variavel da tela que não entendi"(255,0,0), (200, 300, 40, 50))
