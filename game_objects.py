import math

import pygame
import config
from rigidbody import Rigidbody
from shapes import Circle, Line
from sprite_sheet import Type, get_image


class Ball(Circle, Rigidbody):
    def __init__(self, pos, radius, friction=0.98):
        Circle.__init__(self, pos, radius)
        Rigidbody.__init__(self, pos, (0, 0), (0, 0), math.pi * self.radius * self.radius, friction)
        image = pygame.image.load('images/ball_golf.png')
        image = pygame.transform.scale(image, (radius*2, radius*2))
        self.image = image

    def ground_friction(self, ground_type):
        if ground_type == Type.GRASS or ground_type == Type.ORANGE_GRASS:
            self.friction = 0.98
        elif ground_type == Type.SAND:
            self.friction = 0.80
        elif ground_type == Type.WATER:
            self.friction = 0.70

    def not_moving(self):
        return self.vel.length() <= 0.1

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


class Cart(Rigidbody):
    def __init__(self, pos, power, a, b, is_vertical=False):
        Rigidbody.__init__(self, pos, (1*power, 0) if not is_vertical else (0, 1*power), 0, 0, 1)
        self.image = get_image(Type.CART, is_vertical)
        self.move_vertical = is_vertical
        self.size = config.cart_size
        self.a = a
        self.b = b

    def move_cart(self, t, constant=False):
        self.move(t, constant)

        current_pos = self.pos[0] if not self.move_vertical else self.pos[1]
        if current_pos < self.a or current_pos > self.b:
            self.vel *= -1

    def blit(self, screen):
        screen.blit(self.image, self.pos)


