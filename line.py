import math

from pygame import Vector2
import pygame


class Line:
    def __init__(self, seg_a, seg_b):
        self.a = seg_a
        self.b = seg_b
        self.vec = seg_b - seg_a

    @property
    def length(self):
        return self.vec.length()

    @property
    def unit(self):
        return self.vec / self.vec.length()

    @property
    def normal(self):
        return Vector2(self.vec[1], -self.vec[0]).normalize()

    @property
    def parallel_up(self):
        return Line(self.a + self.normal * 10, self.b + self.normal * 10)

    @property
    def parallel_down(self):
        return Line(self.a - self.normal * 10, self.b - self.normal * 10)

    def draw(self, screen, color=(255, 255, 255), width=1):
        pygame.draw.line(screen, color, self.a, self.b, width)
