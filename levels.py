from cell import Cell
from scene import Scene
from sprite_sheet import Type
from transformation import indexes_2_pixels

water_cell = Cell(Type.WATER)
grass_cell = Cell(Type.GRASS)
wall_cell = Cell(Type.WALL)
sand_cell = Cell(Type.SAND)
dark_grass_cell = Cell(Type.DARK_GRASS)
green_cell = Cell(Type.GREEN)
flower_red_cell = Cell(Type.FLOWER_RED)
flower_blue_cell = Cell(Type.FLOWER_BLUE)
flower_white_cell = Cell(Type.FLOWER_WHITE)


class Level1(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(20, 45)
        self.end_point = indexes_2_pixels(75, 20)

    def init(self):
        self.rectangle(0, 0, 89, 59, green_cell)
        self.random_on_rect(0, 0, 89, 59, flower_red_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_blue_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_white_cell, 100)
        self.rectangle(10, 10, 30, 50, grass_cell)
        self.rectangle(30, 10, 80, 30, grass_cell)
        self.horizontal_line(10, 80, 10, wall_cell, down=True)
        self.vertical_line(10, 50, 10, wall_cell, right=True)
        self.horizontal_line(10, 30, 50, wall_cell, down=False)
        self.vertical_line(30, 50, 30, wall_cell, right=False)
        self.horizontal_line(30, 80, 30, wall_cell, down=False)
        self.vertical_line(10, 30, 80, wall_cell, right=False)
