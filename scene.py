import numpy as np


class Scene:
    def __init__(self):
        self.walls = []

    def add_walls(self, *walls):
        for wall in walls:
            self.walls.append(wall)

    def hitboxes(self):
        return [wall.hitbox for wall in self.walls]

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)

    def draw_hitboxes(self, screen):
        for wall in self.walls:
            wall.draw_hitbox(screen)

    def pixels_2_indexes(self, x, y):
        pass
