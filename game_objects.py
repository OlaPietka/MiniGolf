import math

import pygame
import config
from rigidbody import Rigidbody
from shapes import Circle, Line
from sprite_sheet import Type


class Ball(Circle, Rigidbody):
    def __init__(self, pos, radius, friction=0.98):
        Circle.__init__(self, pos, radius)
        Rigidbody.__init__(self, pos, (0, 0), (0, 0), math.pi * self.radius * self.radius, friction)
        image = pygame.image.load('images/ball_golf.png')
        image = pygame.transform.scale(image, (radius*2, radius*2))
        self.image = image

    def ground_friction(self, ground_type):
        if ground_type == Type.GRASS:
            self.friction = 0.985
        elif ground_type == Type.SAND:
            self.friction = 0.80
        elif ground_type == Type.WATER:
            self.friction = 0.70

    def not_moving(self):
        return self.vel.length() <= 0.05

    def blit(self, screen):
        screen.blit(self.image, (self.pos - pygame.Vector2(self.radius)))


class Hole(Circle, Rigidbody):
    def __init__(self, pos, radius):
        Circle.__init__(self, pos, radius)
        Rigidbody.__init__(self, pos, (0, 0), (0, 0), 314, 0)

    def blit(self, screen):
        self.draw(screen, (0, 0, 0), 0)


class Wall(Line):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.hitbox_offset = config.ball_radius

    @property
    def hitbox(self):
        return [self.parallel_up(self.hitbox_offset), self.parallel_down(self.hitbox_offset),
                Circle(self.a, self.hitbox_offset), Circle(self.b, self.hitbox_offset)]

    def draw_hitbox(self, screen):
        for shape in self.hitbox:
                shape.draw(screen)
