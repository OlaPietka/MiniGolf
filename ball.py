import numpy as np


class Ball:
    ball_mass = 0.5
    friction = 0.9
    size = 20
    radius = size / 2

    def __init__(self):
        self.pos = np.array([100, 100], dtype=float)
        self.vel = np.zeros(2, dtype=float)
        self.image = 'images/ball_golf.png'

    def update_pos(self, force, t):
        self.vel += (force / self.ball_mass) * t
        self.vel *= self.friction
        self.pos += self.vel * t


