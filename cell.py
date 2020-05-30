from pygame import Vector2
import config
from sprite_sheet import get_image, Type


class Cell:
    def __init__(self, cell_type):
        self.type = cell_type
        self.image = get_image(cell_type)
        self.size = config.cell_size
        self.is_wall = cell_type == Type.WALL
        self.pos = Vector2(0, 0)
        self.rect = (0, 0, 0, 0)
