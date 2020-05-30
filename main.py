import physics
import pygame
from pygame import Vector2
from levels import Level1
from game_objects import Ball
from shapes import Line, Circle
import config
from transformation import pixels_2_indexes


def get_image(obj):
    image = pygame.image.load(obj.image)
    image = pygame.transform.scale(image, (obj.size, obj.size))
    return image


def center_pos(obj):
    return obj.pos - obj.radius


pygame.init()
screen = pygame.display.set_mode(config.screen_size)
clock = pygame.time.Clock()

game_end = False

mi = Vector2(0, 0)
mf = Vector2(0, 0)

level = Level1()
ball = Ball(level.start_point, config.ball_radius)
whole = Circle(level.end_point, config.ball_radius+5)

if __name__ == "__main__":
    level.init()

    while not game_end:
        screen.fill(0)
        dt = clock.tick(140) / 100.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mi = Vector2(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                mf = Vector2(pygame.mouse.get_pos())
                ball.apply_force((mi-mf)*2)

        ball.move(dt)
        time_line = Line(ball.pos, ball.pos + ball.vel * dt)
        time_line.draw(screen)

        i, j = pixels_2_indexes(*ball.pos)
        cell = level.board[i][j]
        ball.ground_friction(cell.type)

        physics.check_collisions(level.walls, time_line, ball)
        level.blit(screen)
        whole.draw(screen, (0, 0, 0), 0)
        ball.blit(screen)
        pygame.display.flip()

        if physics.point_in_circle(whole, ball.pos):
            ball.vel = whole.pos - ball.pos
            print("lolo")

    pygame.quit()
    exit(0)
