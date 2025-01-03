#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
import pygame as pg
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_BLUE, MENU_OPTION, COLOR_WHITE, COLOR_GREEN


class Menu:
    def __init__(self, Window):
        self.window = Window
        self.surf = pygame.image.load('./asset/menu_cobra_2.jpg')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pg.mixer_music.load('./asset/musica_manu.mp3')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Cobrinha Maluca", COLOR_BLUE, ((WIN_WIDTH / 2), 140))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_GREEN, ((WIN_WIDTH / 2), 230 + 40 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 230 + 40 * i))


            pygame.display.flip()

            # Check for all events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()  # end window
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN: #DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pg.K_UP: #UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pg.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Verdana", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
