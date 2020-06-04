import pygame
import config
import physics
from levels import Levels

pygame.init()

heart = pygame.image.load('images/heart.png')
heart = pygame.transform.scale(heart, (50, 50))

font1 = pygame.font.SysFont('Comic Sans MS', 20)
font2 = pygame.font.SysFont('Comic Sans MS', 30)
font3 = pygame.font.SysFont('Comic Sans MS', 60)


class GameManager(Levels):
    def __init__(self):
        Levels.__init__(self)
        self.current_level = self.get_next()
        self.throw_number = 0
        self.lives_number = 3

    def reset_stats(self):
        self.throw_number = 0
        self.lives_number = 3

    def reset_level(self, ball, hole):
        self.throw_number = 0
        self.lives_number -= 1

        ball.reset(self.current_level.start_point)
        hole.reset(self.current_level.end_point)

    def no_lives(self):
        if self.lives_number == 0:
            self.reset_stats()
            self.current = 0
            self.current_level = self.get_next()
            return True
        return False

    def new_level(self, ball, hole):
        self.current_level = self.get_next()

        if self.current_level is None:
            return None, True
        self.reset_stats()

        return self.new_game(ball, hole), False

    def new_game(self, ball, hole):
        self.current_level.init()
        ball.reset(self.current_level.start_point)
        hole.reset(self.current_level.end_point)
        return self.current_level.carts

    def ball_in_hole(self, ball, hole):
        return (ball.pos - hole.pos).length() <= hole.radius - ball.radius

    def ball_outside(self, cell_type):
        return cell_type == 11 or cell_type == 6 or cell_type == 16

    def ball_touch_cart(self, ball, cart):
        return physics.ball_rectangle_intersect(ball, cart)

    def blit_lives(self, screen):
        for i in range(self.lives_number):
            screen.blit(heart, (config.screen_size[0] - 60 - i * 60, 0))

    def blit_text(self, screen):
        points_text = font1.render("Number of throws: {}".format(self.throw_number), False, (0, 0, 0))
        level_text = font2.render("Level {}".format(self.current), False, (0, 0, 0))

        screen.blit(points_text, (0, 0))
        screen.blit(level_text, (config.screen_size[0] // 2 - 80, 0))

    def blit_the_end(self, screen):
        end_text = font3.render("The End", False, (0, 0, 0))

        screen.blit(end_text, (config.screen_size[0] // 2 - 110, config.screen_size[1] // 2 - 80))

    def blit_start(self, screen):
        start_text = font3.render("Start game", False, (0, 0, 0))

        screen.blit(start_text, (config.screen_size[0] // 2 - 140, config.screen_size[1] // 2 - 70))
