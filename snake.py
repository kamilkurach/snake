import pygame as pg
import sys
import time
import random


class Snake:
    def __init__(self, snake_length=20) -> None:
        self.snake_length = snake_length
        self.snake_arr = []
        self.snake_head = pg.Rect((0, 0), (0, 0))
        self.snake_pos_x = 100
        self.snake_pos_y = 100

    def get_snake_length(self):
        return self.snake_length

    def increase_snake_length(self):
        self.snake_length += 10

    def get_snake_arr(self):
        return self.snake_arr

    def get_snake_head(self):
        return self.snake_head

    def set_snake_head(self, snake_head):
        self.snake_head = snake_head

    def update_snake_arr(self):
        position = [self.snake_pos_x, self.snake_pos_y]
        self.snake_arr.append(position)

    def pop_snake_arr(self):
        self.snake_arr.pop(0)


class Fruit:
    def __init__(self) -> None:
        self.fruit_pos_x = random.randint(150, 400)
        self.fruit_pos_y = random.randint(150, 400)
        self.fruit = pg.Rect((self.fruit_pos_x, self.fruit_pos_y), (20, 20))

    def generate_new_position(self):
        self.fruit_pos_x = random.randint(150, 400)
        self.fruit_pos_y = random.randint(150, 400)

    def make_new_fruit(self):
        self.generate_new_position()
        self.fruit = pg.Rect((self.fruit_pos_x, self.fruit_pos_y), (20, 20))

    def get_fruit(self):
        return self.fruit


class MainWindow:
    def __init__(self) -> None:
        self.window = pg.display.set_mode(
            size=(640, 520), flags=0, depth=0, display=0, vsync=0)
        self.score_surface = pg.Surface(size=(640, 45))
        self.game_area_surface = pg.Surface(size=(640, 520))
        self.border = pg.draw.rect(
            self.game_area_surface, (202, 201, 245), pg.Rect(25, 25, 600, 425), 5)

    def init_main_window(self):
        pg.display.set_caption("Snake")
        pg.init()
        pg.display.init()

    def draw_display_score_bar(self, score=0):
        self.score_surface.fill((63, 150, 102))
        self.window.blit(self.score_surface, (0, 0))
        font = pg.font.SysFont(None, 40)
        img = font.render('SCORE: {0}'.format(score), True, (144, 210, 245))
        self.window.blit(img, (240, 10))

    def draw_game_area(self):
        self.game_area_surface.fill((202, 201, 245))
        self.window.blit(self.game_area_surface, (0, 40))

    def game_over(self):
        font = pg.font.SysFont(None, 50)
        img = font.render('GAME OVER', True, (144, 210, 245))
        self.game_area_surface.fill((0, 0, 0))
        self.window.blit(self.game_area_surface, (0, 0))
        self.window.blit(img, (200, 240))

    def draw_snake(self, snake):
        snake_size = (25, 25)
        snake_arr = snake.get_snake_arr()
        for i, e in enumerate(snake_arr):
            if i == len(snake_arr)-1:
                snake_head = pg.draw.rect(
                    self.game_area_surface, (80, 145, 250), pg.Rect((e[0], e[1]), snake_size))
                snake.set_snake_head(snake_head)
            else:
                if i % 4 == 0:
                    pg.draw.rect(self.game_area_surface, (42, 122,
                                 250), pg.Rect((e[0], e[1]), snake_size))
                else:
                    pg.draw.rect(self.game_area_surface, (83, 93,
                                 110), pg.Rect((e[0], e[1]), snake_size))
            if len(snake_arr) > snake.get_snake_length():
                snake.pop_snake_arr()

        self.window.blit(self.game_area_surface, (0, 40))

    def draw_fruit(self, fruit):
        pg.draw.rect(self.game_area_surface, (130, 13, 29), fruit.get_fruit())
        self.window.blit(self.game_area_surface, (0, 40))

    def get_border(self):
        return self.border


class GameLoop:
    def __init__(self) -> None:
        self.score = 0
        self.k_up = False
        self.k_down = False
        self.k_right = True
        self.k_left = False
        self.music = 'sound/Snake-Song-2-E.mp3'
        self.capture_effect = 'sound/Snake-Capture-Fruit.mp3'
        self.game_over_music = 'sound/Game-Over.mp3'

        self.snake = Snake()
        self.fruit = Fruit()
        self.main_window = MainWindow()

    def update_display(self):
        pg.display.update()

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def background_music(self):
        pg.mixer.music.load(self.music)
        pg.mixer.music.set_volume(0.6)
        pg.mixer.music.play(-1)

    def capture_sound(self):
        capture_sound = pg.mixer.Sound(self.capture_effect)
        pg.mixer.Sound.play(capture_sound)

    def game_over(self):
        self.main_window.game_over()
        pg.display.update()
        pg.mixer.music.stop()
        time.sleep(0.5)
        pg.mixer.music.load(self.game_over_music)
        pg.mixer.music.play(1)
        time.sleep(6)
        sys.exit(1)

    def position_update(self, snake):
        if self.k_up == True:
            snake.snake_pos_y -= 3
        elif self.k_down == True:
            snake.snake_pos_y += 3
        elif self.k_right == True:
            snake.snake_pos_x += 3
        elif self.k_left == True:
            snake.snake_pos_x -= 3

        snake.update_snake_arr()

    def check_for_border_hit(self, snake, main_window):
        snake_head = snake.get_snake_head()
        border = main_window.get_border()
        if snake_head.colliderect(border) == False:
            self.game_over()

    def check_for_self_hit(self, snake):
        snake_head = snake.get_snake_head()
        snake_arr = snake.get_snake_arr()
        for e in snake_arr[:len(snake_arr)-15]:
            if e[0] == snake_head.center[0] and e[1] == snake_head.center[1]:
                self.game_over()

    def check_fruit_capture(self, snake, fruit):
        snake_head = snake.get_snake_head()
        if snake_head.colliderect(fruit.get_fruit()) == True:
            self.capture_sound()
            self.increase_score()
            fruit.make_new_fruit()
            snake.increase_snake_length()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if self.k_down != True and event.key == pg.K_UP:
                    self.k_up = True
                    self.k_down = False
                    self.k_right = False
                    self.k_left = False
                elif self.k_up != True and event.key == pg.K_DOWN:
                    self.k_up = False
                    self.k_down = True
                    self.k_right = False
                    self.k_left = False
                elif self.k_left != True and event.key == pg.K_RIGHT:
                    self.k_up = False
                    self.k_down = False
                    self.k_right = True
                    self.k_left = False
                elif self.k_right != True and event.key == pg.K_LEFT:
                    self.k_up = False
                    self.k_down = False
                    self.k_right = False
                    self.k_left = True

            if event.type == pg.QUIT:
                sys.exit(1)

    def init_window(self):
        self.main_window.init_main_window()
        self.main_window.draw_game_area()
        self.main_window.draw_display_score_bar()

    def main(self):
        self.init_window()
        self.background_music()

        if pg.display.get_init() == True:

            while True:

                time.sleep(0.01)

                self.position_update(self.snake)

                self.main_window.draw_game_area()

                self.main_window.draw_display_score_bar(self.get_score())

                self.main_window.draw_snake(self.snake)

                self.main_window.draw_fruit(self.fruit)

                self.event_loop()

                self.check_for_border_hit(self.snake, self.main_window)

                self.check_for_self_hit(self.snake)

                self.check_fruit_capture(self.snake, self.fruit)

                self.update_display()


if __name__ == "__main__":
    game = GameLoop()
    game.main()
