import numpy as np
from pygame import Vector2


class Ball:
    ball_mass = 0.5
    friction = 0.9
    size = 20
    radius = size // 2

    def __init__(self):
        self.pos = Vector2(100, 100)
        self.vel = Vector2(0, 0)
        self.image = 'images/ball_golf.png'

    def update_pos(self, force, t):
        self.vel = (self.vel + (force / self.ball_mass) * t) * self.friction
        self.pos += self.vel * t


