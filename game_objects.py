import math
from rigidbody import Rigidbody
from shapes import Circle, Line


class Ball(Circle, Rigidbody):
    def __init__(self, pos, radius, friction=0.98):
        Circle.__init__(self, pos, radius)
        Rigidbody.__init__(self, pos, (0, 0), (0, 0), math.pi * self.radius * self.radius, friction)
        self.image = 'images/ball_golf.png'


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
