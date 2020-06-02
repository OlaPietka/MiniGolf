import numpy as np

import physics
import pygame
from pygame import Vector2
from levels import Level1, Level2, Level3, Level4, Levels
from game_objects import Ball, Hole
from shapes import Line
import config
from transformation import pixels_2_indexes


def new_game(level):
    level.init()
    return level.carts(), Ball(level.start_point, config.ball_radius), Hole(level.end_point, config.ball_radius + 5)


pygame.init()
screen = pygame.display.set_mode(config.screen_size)
clock = pygame.time.Clock()

game_end = False

mi = Vector2(0, 0)
mf = Vector2(0, 0)

levels = Levels()
level = levels.get_next()

ball = Ball(level.start_point, config.ball_radius)
hole = Hole(level.end_point, config.ball_radius + 5)
ball_moving = False
show_arrow = False

if __name__ == "__main__":
    level.init()
    carts = level.carts()

    while not game_end:
        screen.fill(level.background_color)
        dt = clock.tick(140) / 100.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mi = Vector2(pygame.mouse.get_pos())
                if physics.point_in_circle(ball, mi) and ball.not_moving():
                    show_arrow = True
            if event.type == pygame.MOUSEBUTTONUP:
                if ball.not_moving() and show_arrow:
                    mf = Vector2(pygame.mouse.get_pos())
                    ball.apply_force((mi-mf)*4)
                    show_arrow = False

        ball.move(dt)
        time_line = Line(ball.pos, ball.pos + ball.vel * dt)
        time_line.draw(screen)

        i, j = pixels_2_indexes(*ball.pos)
        cell = level.board[i][j]
        ball.ground_friction(cell.type)

        physics.check_collisions(level.walls, time_line, ball)

        level.blit(screen)
        hole.blit(screen)
        ball.blit(screen)
        level.draw_hitboxes(screen)

        if carts is not None:
            for cart in carts:
                cart.blit(screen)
                cart.move_cart(dt)

                if physics.ball_rectangle_intersect(ball, cart):
                    carts, ball, hole = new_game(level)

        if show_arrow:
            mm = Vector2(pygame.mouse.get_pos())
            force_length = (ball.pos-mm).length()
            if force_length > 100:
                force_length = 100
            pygame.draw.line(screen, (255, 255, 255), ball.pos, (ball.pos - mm).normalize() * force_length + ball.pos)

        pygame.display.flip()

        if physics.point_in_circle(hole, ball.pos):
            ball.vel += (hole.pos - ball.pos)

        if (ball.pos - hole.pos).length() <= hole.radius - ball.radius:
            level = levels.get_next()

            if level is None:
                game_end = True
                continue
            carts, ball, hole = new_game(level)

        if cell.type.value == 11 or cell.type.value == 6 or cell.type.value == 16:
            carts, ball, hole = new_game(level)

    pygame.quit()
    exit(0)
