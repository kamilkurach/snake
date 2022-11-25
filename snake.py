import pygame as pg
import sys
import time

pg.display.init()

if pg.display.get_init() == True:
    window = pg.display.set_mode(size=(640, 480), flags=0, depth=0, display=0, vsync=0)
    surface = pg.Surface(size=(640, 480))
    surface.fill((250, 250, 250))
    window.blit(surface, (0, 0))
    pg.display.update()
    i = 1
    while True:
        
        time.sleep(0.01)
        surface.fill((250, 250, 250))
        pg.draw.rect(surface, (50, 50, 250), pg.Rect((100+i, 100), (30, 30)))
        pg.draw.rect(surface, (50, 50, 250), pg.Rect((133+i, 100), (30, 30)))
        pg.draw.rect(surface, (50, 50, 250), pg.Rect((166+i, 100), (30, 30)))

        pg.draw.rect(surface, (50, 250, 250), pg.Rect((166, 300), (30, 30)))
        window.blit(surface, (0, 0))
        pg.display.update()
        if i < 300:
            i+=2

        for event in pg.event.get():
            print(event)
            if event == pg.QUIT:
                sys.exit(1)

pg.display.quit()
