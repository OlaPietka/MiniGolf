import numpy as np
from pygame import Vector2
import pygame


class Circle:
    def __init__(self, pos, radius):
        self.pos = Vector2(pos)
        self.radius = radius

    def draw(self, screen, color=(255, 255, 255), width=1):
        pygame.draw.circle(screen, color, np.array(self.pos, dtype=int), self.radius, width)


class Line:
    def __init__(self, a, b):
        self.a = Vector2(a)
        self.b = Vector2(b)
        self.vec = Vector2(b) - Vector2(a)

    @property
    def length(self):
        return self.vec.length()

    @property
    def unit(self):
        return self.vec / self.vec.length()

    @property
    def normal(self):
        return Vector2(self.vec[1], -self.vec[0]).normalize()

    def parallel_up(self, offset):
        return Line(self.a + self.normal * offset, self.b + self.normal * offset)

    def parallel_down(self, offset):
        return Line(self.a - self.normal * offset, self.b - self.normal * offset)

    def draw(self, screen, color=(255, 255, 255), width=1):
        pygame.draw.line(screen, color, self.a, self.b, width)
