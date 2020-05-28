import physics
import pygame
from pygame import Vector2
from game_objects import Ball, Wall
from scene import Scene
from shapes import Line
import config


def get_image(obj):
    image = pygame.image.load(obj.image)
    image = pygame.transform.scale(image, (obj.size, obj.size))
    return image


def center_pos(obj):
    return obj.pos - obj.radius


game_end = False

pygame.init()
screen = pygame.display.set_mode(config.screen_size)
clock = pygame.time.Clock()

mi = Vector2(0, 0)
mf = Vector2(0, 0)

ball = Ball((200, 200), config.ball_radius)
#ball.vel = Vector2(5, 5)
wall = Wall((150, 100), (150, 200), ball.radius)
wall2 = Wall((150, 100), (200, 100), ball.radius)
wall3 = Wall((180, 240), (50, 500), ball.radius)
wall4 = Wall((1, 1), (1, config.screen_size[0]-1), ball.radius)
wall5 = Wall((1, 1), (config.screen_size[0]-1, 1), ball.radius)
wall6 = Wall((config.screen_size[0]-1, 1), (config.screen_size[0]-1, config.screen_size[0]-1), ball.radius)
wall7 = Wall((1, config.screen_size[0]-1), (config.screen_size[0]-1, config.screen_size[0]-1), ball.radius)
wall8 = Wall((160, 170), (300, 200), ball.radius)
wall9 = Wall((100, 50), (400, 80), ball.radius)
scene = Scene()
scene.add_walls(wall, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9)

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

        physics.check_collisions(scene.walls, time_line, ball)
        scene.walls[0].hitbox[3].draw(screen)
        p = physics.circle_segment_intersection(time_line, scene.walls[0].hitbox[3])
        if p != None and p != []:
            #print(p)
            for x in p:
                Ball(x).draw(screen)

        ball.draw(screen)
        scene.draw(screen)
        scene.draw_hitboxes(screen)
        pygame.display.flip()

    pygame.quit()
    exit(0)
