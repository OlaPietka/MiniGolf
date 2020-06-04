import pygame
from enum import Enum
from config import sheet_path, cart_size
from transformation import indexes_2_rect

sheet = pygame.image.load(sheet_path)


def image_at(i, j, resize=False, size=(0, 0)):
    # Loads image from x, y, x+offset, y+offset.
    rect = pygame.Rect(indexes_2_rect(i, j))
    image = pygame.Surface(rect.size)
    image.blit(sheet, (0, 0), rect)

    if resize:
        image = pygame.transform.scale(image, size)

    if image.get_at((0, 0)) == (0, 0, 0, 255):
        image.set_colorkey((0, 0, 0))
        image.set_alpha(255)
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
    ORANGE_GRASS = 10
    ORANGE = 11
    CACTUS = 12
    ORANGE_TREE = 13
    EMPTY_TREE = 14
    CART1 = 15
    BLUE = 16
    BLUE_GRASS = 17
    CLOUD1 = 18
    CLOUD2 = 19
    CLOUD3 = 20
    MUSHROOM = 21
    CART2 = 22


position_map = {Type.GRASS: image_at(5, 0),
                Type.WATER: image_at(0, 0),
                Type.SAND: image_at(8, 0),
                Type.WALL: image_at(1, 26),
                Type.DARK_GRASS: image_at(3, 16),
                Type.GREEN: image_at(10, 26),
                Type.FLOWER_RED: image_at(3, 7),
                Type.FLOWER_BLUE: image_at(3, 13),
                Type.FLOWER_WHITE: image_at(3, 10),
                Type.ORANGE_GRASS: image_at(11, 14),
                Type.ORANGE: image_at(13, 26),
                Type.CACTUS: image_at(22, 9),
                Type.ORANGE_TREE: image_at(17, 9),
                Type.EMPTY_TREE: image_at(27, 9),
                Type.CART1: image_at(49, 18, resize=True, size=(cart_size, cart_size)),
                Type.CART2: image_at(51, 18, resize=True, size=(cart_size, cart_size)),
                Type.BLUE: image_at(0, 0),
                Type.BLUE_GRASS: image_at(11, 8),
                Type.CLOUD1: image_at(54, 24),
                Type.CLOUD2: image_at(55, 24),
                Type.CLOUD3: image_at(56, 24),
                Type.MUSHROOM: image_at(48, 5),
                }


def get_image(cell_type):
    return position_map[cell_type]
