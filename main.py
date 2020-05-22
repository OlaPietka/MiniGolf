import time
import numpy as np
import pygame
from pygame import Vector2
from ball import Ball


SCREEN_SIZE = 600
game_end = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

ball = Ball()

mi = Vector2(0, 0)
mf = Vector2(0, 0)
p1 = Vector2(150, 180)
p2 = Vector2(250, 250)
c = 10

ti = time.time()


def get_image(obj):
    image = pygame.image.load(obj.image)
    image = pygame.transform.scale(image, (obj.size, obj.size))
    return image


def center_pos(obj):
    return obj.pos - obj.radius


def closest_point_on_seg(seg_a, seg_b, circle_pos):
    seg_v = seg_b - seg_a  # vector ab
    pt_v = circle_pos - seg_a  # vector ac (from a to center of the circle c)

    seg_v_unit = seg_v / seg_v.length()  # A/|A|
    proj = pt_v.dot(seg_v_unit)  # length of vector from a to closest

    if proj <= 0:
        return seg_a  # closest point is start of the line
    if proj >= seg_v.length():
        return seg_b  # closest point is end of the line

    proj_v = seg_v_unit * proj  # vector from a to closest
    closest = proj_v + seg_a
    return closest


def segment_circle(seg_a, seg_b, circle):
    closest = closest_point_on_seg(seg_a, seg_b, circle.pos)
    dist_v = circle.pos - closest
    if dist_v.length() > circle.radius:
        return Vector2(0, 0)
    offset = dist_v / dist_v.length() * (circle.radius - dist_v.length())
    return offset


while not game_end:
    screen.fill(0)

    tf = time.time()
    dt = (tf - ti)
    ti = tf

    force = np.zeros(2, dtype=float)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mi = Vector2(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            mf = Vector2(pygame.mouse.get_pos())
            force = (mi-mf) * c

    ball.update_pos(force, dt)
    if ball.pos[0] + ball.radius >= 600 or ball.pos[0] - ball.radius <= 0:
        ball.vel[0] *= -1
    if ball.pos[1] + ball.radius >= 600 or ball.pos[1] - ball.radius <= 0:
        ball.vel[1] *= -1

    y = segment_circle(p1, p2, ball)
    print(y)

    pygame.draw.circle(screen, (0, 0, 255), np.array(ball.pos, dtype=int), ball.radius)
    pygame.draw.line(screen, (0, 255, 255), p1, p2, 4)
    #screen.blit(get_image(ball), np.array(center_pos(ball), dtype=int))
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
exit(0)
