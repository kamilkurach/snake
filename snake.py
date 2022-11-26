import pygame as pg
import sys
import time


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
    while True:
        
        time.sleep(0.01)
        surface.fill((250, 250, 250))

        pos_x = 100+i
        pos_y = 100+j
        
        pg.draw.rect(surface, (50, 50, 250), pg.Rect((pos_x, pos_y), (30, 30)))
       
        pg.draw.rect(surface, (50, 250, 250), pg.Rect((166, 300), (30, 30)))
        window.blit(surface, (0, 0))
        pg.display.update()
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    j-=20
                elif event.key == pg.K_DOWN:
                    j+=20
                elif event.key == pg.K_RIGHT:
                    i+=20
                elif event.key == pg.K_LEFT:
                    i-=20

            if event == pg.QUIT:
                sys.exit(1)

pg.display.quit()
