import numpy as np


class Ball:
    ball_mass = 0.5
    friction = 0.9

    def __init__(self):
        self.pos = np.zeros(2, dtype=float)
        self.vel = np.zeros(2, dtype=float)

    def update_pos(self, force, t):
        self.vel += (force / self.ball_mass) * t
        self.vel *= self.friction
        self.pos += self.vel * t