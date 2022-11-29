import pygame as pg
import sys
import time
import random
import os


# class SnakeBody:
#     def __init__(self, snake_length) -> None:
#         self.snake_length = snake_length
#         self.snake = self.make_snake()

#     def make_snake(self):
#         return list(range(self.snake_length))

#     def add_snake_module(self):
#         pass

#     def get_snake_len(self):
#         return len(self.snake)
    
#     def get_snake(self):
#         return self.snake

# class Fruit:
#     def __init__(self) -> None:
#         pass

# snake = SnakeBody(3)

def display_score_bar(score):
    surface = pg.Surface(size=(640, 45))
    surface.fill((63, 150, 102))
    window.blit(surface, (0, 0))
    font = pg.font.SysFont(None, 40)
    img = font.render('SCORE: {0}'.format(score), True, (144, 210, 245))
    window.blit(img, (240, 10))

pg.init()
pg.display.init()

if pg.display.get_init() == True:
    window = pg.display.set_mode(size=(640, 520), flags=0, depth=0, display=0, vsync=0)
    surface = pg.Surface(size=(640, 520))
    surface.fill((202, 201, 245))
    window.blit(surface, (0, 0))

    pg.display.update()

    i = 1
    j = 1
    score = 0
    fruit_pos_x = random.randint(150, 400)
    fruit_pos_y = random.randint(150, 400)
    k_up = False
    k_down = False
    k_right = True
    k_left = False

    pg.mixer.music.load('Snake-Song-2.mp3')
    capture_sound = pg.mixer.Sound('Snake-Capture-Fruit.mp3')
    pg.mixer.music.set_volume(0.6)
    pg.mixer.music.play(-1)
    arr = []
    snake_length = 20
    while True:
        time.sleep(0.01)
        surface.fill((202, 201, 245))

        if k_up == True:
            j-=3
        elif k_down == True:
            j+=3
        elif k_right == True:
            i+=3
        elif k_left == True:
            i-=3

        snake_pos_x = 100+i
        snake_pos_y = 100+j
        arr.append([snake_pos_x, snake_pos_y])
        border = pg.draw.rect(surface, (202, 201, 245), pg.Rect(25, 70, 590, 425), 5)
        
        for ii, e in enumerate(arr):
            if ii == len(arr)-1:
                snake_head = pg.draw.rect(surface, (50, 50, 250), pg.Rect((e[0], e[1]), (30, 30)))
            else:
                pg.draw.rect(surface, (50, 50, 250), pg.Rect((e[0], e[1]), (30, 30)))
            if len(arr) > snake_length:
                arr.pop(0)
 
        fruit = pg.draw.rect(surface, (50, 200, 250), pg.Rect((fruit_pos_x, fruit_pos_y), (20, 20)))
        
        window.blit(surface, (0, 0))

        if snake_head.colliderect(fruit) == True:
            pg.mixer.Sound.play(capture_sound)
            score+=1
            snake_length+=10
            fruit_pos_x = random.randint(150, 400)
            fruit_pos_y = random.randint(150, 400)
            fruit = pg.draw.rect(surface, (50, 250, 250), pg.Rect((fruit_pos_x, fruit_pos_y), (20, 20)))

        
        if snake_head.colliderect(border) == False:
            pg.mixer.music.stop()
            time.sleep(0.5)
            music = pg.mixer.music.load('Game-Over.mp3')
            pg.mixer.music.play(1)
            font = pg.font.SysFont(None, 50)
            img = font.render('GAME OVER', True, (144, 210, 245))
            surface.fill((0, 0, 0))
            window.blit(surface, (0, 0))
            window.blit(img, (200, 240))
            pg.display.update()
            time.sleep(6)
            sys.exit(1)

        for e in arr[:len(arr)-15]:
            if e[0] == snake_head.center[0] and e[1] == snake_head.center[1]:
                pg.mixer.music.stop()
                time.sleep(0.5)
                music = pg.mixer.music.load('Game-Over.mp3')
                pg.mixer.music.play(1)
                font = pg.font.SysFont(None, 50)
                img = font.render('GAME OVER', True, (144, 210, 245))
                surface.fill((0, 0, 0))
                window.blit(surface, (0, 0))
                window.blit(img, (200, 240))
                pg.display.update()
                time.sleep(6)
                sys.exit(1)


        display_score_bar(score)
        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if k_down != True and event.key == pg.K_UP:
                    k_up = True
                    k_down = False
                    k_right = False
                    k_left = False
                elif k_up != True and event.key == pg.K_DOWN:
                    k_up = False
                    k_down = True
                    k_right = False
                    k_left = False
                elif k_left != True and event.key == pg.K_RIGHT:
                    k_up = False
                    k_down = False
                    k_right = True
                    k_left = False
                elif k_right != True and event.key == pg.K_LEFT:
                    k_up = False
                    k_down = False
                    k_right = False
                    k_left = True

            if event.type == pg.QUIT:
                sys.exit(1)

pg.display.quit()
