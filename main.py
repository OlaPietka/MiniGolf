from game_manager import GameManager
import physics
import pygame
from pygame import Vector2
from game_objects import Ball, Hole
from shapes import Line
import config
from transformation import pixels_2_indexes


pygame.init()
screen = pygame.display.set_mode(config.screen_size)
clock = pygame.time.Clock()

game_end = False
game_start = False

mi = Vector2(0, 0)
mf = Vector2(0, 0)

game_manager = GameManager()

ball = Ball(game_manager.current_level.start_point, config.ball_radius)
hole = Hole(game_manager.current_level.end_point, config.ball_radius + 5)

ball_moving = False
show_arrow = False

if __name__ == "__main__":
    while not game_start:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = Vector2(pygame.mouse.get_pos())
                x = config.screen_size[0] // 2 - 140
                y = config.screen_size[1] // 2 - 70
                if physics.point_in_rect((x, y, x + 319, y + 85), mouse):
                    game_start = True

        game_manager.blit_start(screen)
        pygame.display.flip()

    game_manager.current_level.init()
    carts = game_manager.current_level.carts

    while not game_end:
        screen.fill(game_manager.current_level.background_color)
        dt = clock.tick(140) / 100.0
        print(dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mi = Vector2(pygame.mouse.get_pos())
                if physics.point_in_circle(ball, mi) and ball.not_moving():
                    show_arrow = True
            if event.type == pygame.MOUSEBUTTONUP:
                if ball.not_moving() and show_arrow:
                    mf = Vector2(pygame.mouse.get_pos())
                    ball.apply_force((mi-mf)*4)
                    show_arrow = False
                    game_manager.throw_number += 1

        ball.move(dt)
        time_line = Line(ball.pos, ball.pos + ball.vel * dt)

        i, j = pixels_2_indexes(*ball.pos)
        cell = game_manager.current_level.board[i][j]
        ball.ground_friction(cell.type)

        physics.check_collisions(game_manager.current_level.walls, time_line, ball)

        game_manager.current_level.blit(screen)
        hole.blit(screen)
        ball.blit(screen)
        game_manager.blit_text(screen)
        game_manager.blit_lives(screen)

        if carts is not None:
            for cart in carts:
                cart.blit(screen)
                cart.move_cart(dt)

                if game_manager.ball_touch_cart(ball, cart):
                    game_manager.reset_level(ball, hole)

        if show_arrow:
            mm = Vector2(pygame.mouse.get_pos())
            force_length = (ball.pos-mm).length()
            if force_length > 100:
                force_length = 100
            pygame.draw.line(screen, (255, 255, 255), ball.pos, (ball.pos - mm).normalize() * force_length + ball.pos)

        pygame.display.flip()

        if physics.point_in_circle(hole, ball.pos):
            ball.vel += (hole.pos - ball.pos)

        if game_manager.ball_in_hole(ball, hole):
            carts, is_end = game_manager.new_level(ball, hole)

            if is_end:
                game_end = True
                continue

        if game_manager.ball_outside(cell.type.value):
            game_manager.reset_level(ball, hole)

        if game_manager.no_lives():
            carts = game_manager.new_game(ball, hole)

    exit_game = False
    font = pygame.font.SysFont('Comic Sans MS', 30)

    while not exit_game:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

        pygame.draw.line(screen, (255, 255, 0), (10, 10), (100, 100))
        game_manager.blit_the_end(screen)

        pygame.display.flip()

    pygame.quit()
    exit(0)
