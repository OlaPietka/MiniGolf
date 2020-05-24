import physics
import numpy as np
import pygame
from pygame import Vector2
from ball import Ball
from line import Line


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

ball = Ball()

mi = Vector2(0, 0)
mf = Vector2(0, 0)
line = Line(Vector2(150, 100), Vector2(150, 200))


if __name__ == "__main__":
    while not game_end:
        screen.fill(0)
        dt = clock.tick(140)
        force = np.zeros(2, dtype=float)

        #pygame.draw.circle(screen, (255, 0, 255), np.array(ball.next_pos(force, dt), dtype=int), ball.radius, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mi = Vector2(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                mf = Vector2(pygame.mouse.get_pos())
                force = (mi-mf) * 0.0005

        ball.update_pos(force, dt)
        next_ball = Ball(*ball.next(force, dt+1))
        time_line = Line(ball.pos, next_ball.pos)
        time_line.draw(screen)

        if ball.pos[0] + ball.radius >= SCREEN_SIZE or ball.pos[0] - ball.radius <= 0:
            ball.vel[0] *= -1
        if ball.pos[1] + ball.radius >= SCREEN_SIZE or ball.pos[1] - ball.radius <= 0:
            ball.vel[1] *= -1

        collided, normal, depth, closest = physics.segment_circle(line, next_ball)
        if collided:
            if depth > 0 and physics.intersects(line.parallel_up, time_line):
                print("sets pos", depth)
                ball.set_pos(physics.intersection_point(line.parallel_up, time_line))

            ball.vel -= 2*normal*(ball.vel.dot(normal))
            ball.pos += normal * depth
        collided, normal, depth, closest = physics.segment_circle(line, ball)

        pygame.draw.circle(screen, (0, 0, 255), np.array(ball.pos, dtype=int), ball.radius, 1)
        #pygame.draw.circle(screen, (255, 0, 0), np.array(next_ball.pos, dtype=int), ball.radius, 1)
        line.draw(screen)
        line.parallel_up.draw(screen)
        #screen.blit(get_image(ball), np.array(center_pos(ball), dtype=int))

        pygame.display.flip()
    pygame.quit()
    exit(0)
