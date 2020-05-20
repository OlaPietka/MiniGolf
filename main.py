import time
import numpy as np
import pygame
from ball import Ball

SCREEN_SIZE = 600

game_end = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
clock = pygame.time.Clock()

ball = Ball()

xi, yi = 0, 0
xf, yf = 0, 0

c = 10

ti = time.time()

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
            xi, yi = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            xf, yf = pygame.mouse.get_pos()
            force = np.array([xi - xf, yi - yf]) * c

    ball.update_pos(force, dt)
    if ball.pos[0] + 25 >= 600 or ball.pos[0] - 25 <= 0:
        ball.vel[0] *= -1
    if ball.pos[1] + 25 >= 600 or ball.pos[1] - 25 <= 0:
        ball.vel[1] *= -1

    pygame.draw.circle(screen, (0, 0, 255), np.array(ball.pos, dtype=int), 25)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()
exit(0)
