import physics
import pygame
from pygame import Vector2
from game_objects import Ball, Wall
from shapes import Line


def get_image(obj):
    image = pygame.image.load(obj.image)
    image = pygame.transform.scale(image, (obj.size, obj.size))
    return image


def center_pos(obj):
    return obj.pos - obj.radius


SCREEN_SIZE = 500
game_end = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

mi = Vector2(0, 0)
mf = Vector2(0, 0)

ball = Ball()
wall = Wall(Vector2(150, 100), Vector2(150, 200), ball.radius)
wall2 = Wall(Vector2(150, 100), Vector2(200, 150), ball.radius)


if __name__ == "__main__":
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
                ball.apply_force((mi-mf)*10)

        ball.move(dt)
        time_line = Line(ball.pos, ball.pos + ball.vel * dt)
        time_line.draw(screen)

        if ball.pos[0] + ball.radius >= SCREEN_SIZE or ball.pos[0] - ball.radius <= 0:
            ball.vel[0] *= -1
        if ball.pos[1] + ball.radius >= SCREEN_SIZE or ball.pos[1] - ball.radius <= 0:
            ball.vel[1] *= -1

        inter_point = physics.closest_intersection(wall.hitbox, time_line, ball.pos)
        if inter_point is not None:
            normal = physics.normal_segment_circle(wall, ball)
            ball.set_pos(inter_point)
            ball.bounce(normal)

        ball.draw(screen)
        wall.draw(screen)
        wall.draw_hitbox(screen)
        pygame.display.flip()

    pygame.quit()
    exit(0)
