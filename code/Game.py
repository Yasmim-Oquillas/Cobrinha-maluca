#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame as pg

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Start import Start


class Game:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                start = Start(self.window, 'Start')
                start_return = start.run()
            elif menu_return == MENU_OPTION[1]:
                sys.exit()
            else:
                pass



