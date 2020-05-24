from pygame import Vector2
from shapes import Circle, Line


class Ball(Circle):
    ball_mass = 0.5
    friction = 0.98

    def __init__(self, pos=Vector2(180, 200), vel=Vector2(0, 0)):
        super().__init__(pos)
        self.vel = vel
        self.image = 'images/ball_golf.png'

    def move(self, force, t):
        self.vel = (self.vel + (force / self.ball_mass) * t) * self.friction
        self.pos += self.vel * t

    def bounce(self, normal, depth):
        self.vel -= 2 * normal * (self.vel.dot(normal))
        self.pos += normal * depth

    def next(self, force, t):
        vel = (self.vel + (force / self.ball_mass) * t) * self.friction
        pos = self.pos + vel * t
        return pos, vel


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
