import numpy as np
from pygame import Vector2


class Ball:
    ball_mass = 0.5
    friction = 0.98
    size = 20
    radius = size // 2

    def __init__(self, pos=Vector2(180, 200), vel=Vector2(0, 0)):
        self.pos = pos
        self.vel = vel
        self.image = 'images/ball_golf.png'

    def set_pos(self, p):
        self.pos = p

    def update_pos(self, force, t):
        self.vel = (self.vel + (force / self.ball_mass) * t) * self.friction
        self.pos += self.vel * t

    def next(self, force, t):
        vel = (self.vel + (force / self.ball_mass) * t) * self.friction
        pos = self.pos + vel * t
        return pos, vel

