#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, Window):
        self.window = Window
        self.surf = pygame.image.load('./asset/menu_cobra.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pg.mixer_music.load('./asset/musica_manu.mp3')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Cobrinha Maluca", COLOR_ORANGE, ((WIN_WIDTH / 2), 140))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 230 + 40 * i))

            pygame.display.flip()

            # Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Verdana", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)