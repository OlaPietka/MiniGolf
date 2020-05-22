from enum import Enum
import numpy as np


class CellType(Enum):
    GRASS = 1
    WATER = 2
    BORDER = 3
    SAND = 4


class Cell:
    def __init__(self, cell_type, position, is_border=False):
        self.type = cell_type
        self.friction = self.get_friction()
        self.image = self.get_image()
        self.size = 20
        self.is_border = is_border
        self.position = np.array(position, dtype=float)

    def get_friction(self):
        if self.type == CellType.GRASS:
            return 0.9
        elif self.type == CellType.WATER:
            return 0.05
        elif self.type == CellType.SAND:
            return 0.4
        else:
            return None

    def get_image(self):
        if self.type == CellType.GRASS:
            return 85, 0, 101, 0
        elif self.type == CellType.WATER:
            return 0, 0, 16, 16
        elif self.type == CellType.SAND:
            return 136, 0, 152, 0
        elif self.type == CellType.BORDER:
            return 17, 442, 33, 458


class Board:
    def __init__(self):
        self.board = []

    def fill(self):
        self.board.append([])
        for i in range(30):
            self.board[0].append(Cell(CellType.GRASS, [i*16, 0]))



