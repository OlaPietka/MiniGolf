import math

from pygame import Vector2
from shapes import Circle, Line


class Ball(Circle):
    friction = 0.98

    def __init__(self, pos=Vector2(180, 200), vel=Vector2(0, 0)):
        super().__init__(pos)
        self.vel = vel
        self.image = 'images/ball_golf.png'
        self.acc = Vector2(0, 0)
        self.mass = math.pi * self.radius * self.radius

    def apply_force(self, force):
        self.acc += force

    def move(self, t):
        self.vel += self.acc * t
        self.vel *= self.friction
        self.pos += self.vel * t
        self.acc = Vector2(0, 0)

    def bounce(self, normal):
        self.vel -= 2 * normal * (self.vel.dot(normal))


class Wall(Line):
    def __init__(self, a, b, hitbox_offset):
        super().__init__(a, b)
        self.hitbox_offset = hitbox_offset

    @property
    def hitbox(self):
        return [self.parallel_up(self.hitbox_offset), self.parallel_down(self.hitbox_offset),
                Circle(self.a, self.hitbox_offset), Circle(self.b, self.hitbox_offset)]

    def draw_hitbox(self, screen):
        for shape in self.hitbox:
                shape.draw(screen)
