import pygame as pg
import sys
import time
import random


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

pg.display.init()

if pg.display.get_init() == True:
    window = pg.display.set_mode(size=(640, 480), flags=0, depth=0, display=0, vsync=0)
    surface = pg.Surface(size=(640, 480))
    surface.fill((250, 250, 250))
    window.blit(surface, (0, 0))
    pg.display.update()
    i = 1
    j = 1
    
    fruit_pos_x = random.randint(150, 400)
    fruit_pos_y = random.randint(150, 400)
    k_up = False
    k_down = False
    k_right = True
    k_left = False

    while True:
        print(k_up, k_down)
        time.sleep(0.01)
        surface.fill((250, 250, 250))

        if k_up == True:
            j-=2
        elif k_down == True:
            j+=2
        elif k_right == True:
            i+=2
        elif k_left == True:
            i-=2

        snake_pos_x = 100+i
        snake_pos_y = 100+j
        
        pg.draw.rect(surface, (50, 50, 250), pg.Rect((snake_pos_x, snake_pos_y), (30, 30)))
        pg.draw.rect(surface, (50, 250, 250), pg.Rect((fruit_pos_x, fruit_pos_y), (30, 30)))
        window.blit(surface, (0, 0))
        pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    k_up = True
                    k_down = False
                    k_right = False
                    k_left = False
                elif event.key == pg.K_DOWN:
                    k_up = False
                    k_down = True
                    k_right = False
                    k_left = False
                elif event.key == pg.K_RIGHT:
                    k_up = False
                    k_down = False
                    k_right = True
                    k_left = False
                elif event.key == pg.K_LEFT:
                    k_up = False
                    k_down = False
                    k_right = False
                    k_left = True

            if event.type == pg.QUIT:
                sys.exit(1)

pg.display.quit()
