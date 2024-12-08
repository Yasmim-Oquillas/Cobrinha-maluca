from ctypes import windll

from pygame.examples.go_over_there import clock
from pygame.examples.playmus import Window
from pygame.locals import *
from pygame.font import Font
from code.Const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_BLUE, COLOR_GREEN, COLOR_LIGHTGREEN, COLOR_RED
from code.Entity import Entity
import pygame as pg
from pygame import Surface, Rect
from random import randint #sortear posições diferentes

from code.Menu import Menu


class Start:
    def __init__(self, window, name):
        pg.init()
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.name = name

    def increase_snake(self, list_snake):
        for i in list_snake:
            pg.draw.rect(self.window, COLOR_GREEN, (i[0], i[1], 20, 20))

    def reset_game(self, ):
        global pontos, initial_length, x_snake, y_snake, list_snake, list_snakehead, x_food, y_food, end_game
        pontos = 0
        initial_length = 2
        x_snake = int(WIN_WIDTH / 2)
        y_snake = int(WIN_HEIGHT / 2)
        list_snake = []
        list_snakehead = []
        x_food = randint(40, 610)
        y_food = randint(40, 440)
        end_game = False


    def run(self,):
        global pontos, initial_length, x_snake, y_snake, list_snake, list_snakehead, x_food, y_food, end_game
        x_snake = int(WIN_WIDTH/2)
        y_snake = int(WIN_HEIGHT/2)
        pontos = 0

        speed = 10
        x_cont = speed
        y_cont = 0

        #sortear posições diferentes
        x_food = randint(40, 610)
        y_food = randint(40, 440)
        pg.display.set_caption('Cobrinha maluca')

        pg.mixer_music.set_volume(0.5)
        pg.mixer_music.load('./asset/musica_manu.mp3')
        pg.mixer_music.play(-1)
        dot_music = pg.mixer.Sound('./asset/Pontos.mp3')
        end_game_music = pg.mixer.Sound('./asset/Fim_jogo.mp3')

        clock = pg.time.Clock()
        list_snake = []
        initial_length = 2
        end_game = False

        while True:
            #tempo de movimento objeto
            clock.tick(30)
            self.window.fill(COLOR_LIGHTGREEN)
            self.menu_text(30, f'Pontos: {pontos}', COLOR_BLUE, (600, 30))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # close window
                    quit()  # end pygame

                if event.type == pg.KEYDOWN:
                    if event.key == K_LEFT:
                        if x_cont == speed:
                            pass
                        else:
                            x_cont = - speed
                            y_cont = 0
                    if event.key == K_RIGHT:
                        if x_cont == -speed:
                            pass
                        else:
                            x_cont = speed
                            y_cont = 0
                    if event.key == K_UP:
                        if y_cont == speed:
                            pass
                        else:
                            y_cont = -speed
                            x_cont = 0
                    if event.key == K_DOWN:
                        if y_cont == -speed:
                            pass
                        else:
                            y_cont =  speed
                            x_cont = 0

            x_snake = x_snake + x_cont
            y_snake = y_snake + y_cont

            #objetos
            snake = pg.draw.rect(self.window, COLOR_GREEN, (x_snake, y_snake, 20, 20))
            food = pg.draw.rect(self.window, COLOR_RED, (x_food, y_food, 20, 20))


            # colisão entre snake e food
            if snake.colliderect(food):
                x_food = randint(40, 610)
                y_food = randint(40, 440)
                pontos = pontos +1
                dot_music.play()
                initial_length = initial_length +1

            #armazena os novos valores
            list_snakehead = []
            list_snakehead.append(x_snake)
            list_snakehead.append(y_snake)
            #armazena valor atual
            list_snake.append(list_snakehead)

            if list_snake.count(list_snakehead) > 1:
                end_game = True
                end_game_music.play()
                while end_game:
                    self.window.fill(COLOR_LIGHTGREEN)
                    for event in pg.event.get():
                        if event.type == QUIT:
                            pg.quit()
                            exit()
                        if event.type == KEYDOWN and event.key == K_r:
                                self.reset_game()
                                end_game = False
                    self.menu_text(20, f'Você perdeu! Pressione a tecla R para jogar novamente', COLOR_BLUE, (350, 200))
                    pg.display.update()

            if x_snake > WIN_WIDTH:
                x_snake = 0
            if x_snake < 0:
                x_snake = WIN_WIDTH
            if y_snake < 0:
                y_snake = WIN_HEIGHT
            if y_snake > WIN_HEIGHT:
                y_snake = 0


            if len(list_snake) > initial_length:
                del list_snake[0]

            self.increase_snake(list_snake)

            pg.display.update()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Verdana", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)