from pygame import Vector2


class Rigidbody:
    def __init__(self, pos, vel, acc, mass, friction):
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.acc = Vector2(acc)
        self.mass = mass
        self.friction = friction

    def apply_force(self, force):
        self.acc += force

    def move(self, t, constant=False):
        self.vel += self.acc * t
        self.vel *= self.friction
        self.pos += self.vel * t

        if not constant:
            self.acc = Vector2(0, 0)

    def bounce(self, normal):
        self.vel -= 2 * normal * (self.vel.dot(normal))
