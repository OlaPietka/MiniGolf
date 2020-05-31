from enum import Enum
import pygame
from config import sheet_path
from transformation import indexes_2_rect

sheet = pygame.image.load(sheet_path)


def image_at(i, j):
    # Loads image from x, y, x+offset, y+offset.
    rect = pygame.Rect(indexes_2_rect(i, j))
    image = pygame.Surface(rect.size)
    image.blit(sheet, (0, 0), rect)
    return image


class Type(Enum):
    GRASS = 1
    WATER = 2
    WALL = 3
    SAND = 4
    DARK_GRASS = 5
    GREEN = 6
    FLOWER_RED = 7
    FLOWER_BLUE = 8
    FLOWER_WHITE = 9


position_map = {Type.GRASS: image_at(5, 0),
                Type.WATER: image_at(0, 0),
                Type.SAND: image_at(8, 0),
                Type.WALL: image_at(1, 26),
                Type.DARK_GRASS: image_at(3, 16),
                Type.GREEN: image_at(10, 26),
                Type.FLOWER_RED: image_at(3, 7),
                Type.FLOWER_BLUE: image_at(3, 13),
                Type.FLOWER_WHITE: image_at(3, 10)}


def get_image(cell_type):
    return position_map[cell_type]
