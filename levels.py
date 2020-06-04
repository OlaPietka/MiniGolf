from cell import Cell
from game_objects import Cart
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
orange_grass_cell = Cell(Type.ORANGE_GRASS)
orange_cell = Cell(Type.ORANGE)
orange_tree_cell = Cell(Type.ORANGE_TREE)
cactus_cell = Cell(Type.CACTUS)
empty_tree_cell = Cell(Type.EMPTY_TREE)
blue_cell = Cell(Type.BLUE)
blue_grass_cell = Cell(Type.BLUE_GRASS)
cloud1_cell = Cell(Type.CLOUD1)
cloud2_cell = Cell(Type.CLOUD2)
cloud3_cell = Cell(Type.CLOUD3)
mushroom_cell = Cell(Type.MUSHROOM)


class Levels:
    def __init__(self):
        self.levels = [Level1(), Level2(), Level3(), Level4(), Level5(), Level6(), Level7(), Level8(), Level9()]
        self.current = 7
        self.count = len(self.levels)

    def get_next(self):
        self.current += 1

        if self.current > self.count:
            return None

        return self.levels[self.current-1]


class Level1(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(20, 45)
        self.end_point = indexes_2_pixels(75, 20)
        self.background_color = (123, 172, 44)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, green_cell)

        self.random_on_rect(0, 0, 89, 59, flower_red_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_blue_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_white_cell, 100)
        self.random_on_rect(0, 0, 89, 59, mushroom_cell, 100)

        self.rectangle(10, 10, 30, 50, grass_cell)
        self.rectangle(30, 10, 80, 30, grass_cell)

        self.horizontal_line(10, 80, 10, wall_cell, down=True)
        self.vertical_line(10, 50, 10, wall_cell, right=True)
        self.horizontal_line(10, 30, 50, wall_cell, down=False)
        self.vertical_line(30, 50, 30, wall_cell, right=False)
        self.horizontal_line(30, 80, 30, wall_cell, down=False)
        self.vertical_line(10, 30, 80, wall_cell, right=False)

    @property
    def carts(self):
        return None


class Level2(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(20, 45)
        self.end_point = indexes_2_pixels(75, 35)
        self.background_color = (123, 172, 44)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, green_cell)

        self.random_on_rect(0, 0, 89, 59, flower_red_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_blue_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_white_cell, 100)
        self.random_on_rect(0, 0, 89, 59, mushroom_cell, 100)

        self.rectangle(10, 10, 30, 50, grass_cell)
        self.rectangle(30, 10, 50, 20, grass_cell)
        self.rectangle(40, 20, 50, 40, grass_cell)
        self.rectangle(50, 30, 60, 40, grass_cell)
        self.rectangle(60, 20, 80, 50, grass_cell)

        self.rectangle(15, 20, 25, 25, sand_cell)

        self.horizontal_line(10, 50, 10, wall_cell, down=True)
        self.vertical_line(10, 50, 10, wall_cell, right=True)
        self.horizontal_line(10, 30, 50, wall_cell, down=False)
        self.vertical_line(20, 50, 30, wall_cell, right=False)
        self.horizontal_line(30, 40, 20, wall_cell, down=False)
        self.vertical_line(10, 30, 50, wall_cell, right=False)
        self.vertical_line(20, 40, 40, wall_cell, right=True)
        self.horizontal_line(40, 60, 40, wall_cell, down=False)
        self.horizontal_line(50, 60, 30, wall_cell, down=True)
        self.vertical_line(20, 30, 60, wall_cell, right=True)
        self.vertical_line(40, 50, 60, wall_cell, right=True)
        self.horizontal_line(60, 80, 20, wall_cell, down=True)
        self.horizontal_line(60, 80, 50, wall_cell, down=False)
        self.vertical_line(20, 50, 80, wall_cell, right=False)

    @property
    def carts(self):
        return None


class Level3(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(20, 45)
        self.end_point = indexes_2_pixels(71, 45)
        self.background_color = (123, 172, 44)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, green_cell)

        self.random_on_rect(0, 0, 89, 59, flower_red_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_blue_cell, 100)
        self.random_on_rect(0, 0, 89, 59, flower_white_cell, 100)
        self.random_on_rect(0, 0, 89, 59, mushroom_cell, 100)

        self.rectangle(10, 10, 30, 50, grass_cell)
        self.rectangle(30, 10, 80, 20, grass_cell)
        self.rectangle(60, 20, 80, 50, grass_cell)

        self.rectangle(15, 30, 25, 35, sand_cell)

        self.rectangle(60, 20, 68, 25, water_cell)
        self.rectangle(72, 20, 80, 25, water_cell)

        self.horizontal_line(10, 80, 10, wall_cell, down=True)
        self.vertical_line(10, 50, 10, wall_cell, right=True)
        self.horizontal_line(10, 30, 50, wall_cell, down=False)
        self.vertical_line(20, 50, 30, wall_cell, right=False)
        self.horizontal_line(30, 60, 20, wall_cell, down=False)
        self.vertical_line(20, 50, 60, wall_cell, right=True)
        self.horizontal_line(60, 80, 50, wall_cell, down=False)
        self.vertical_line(10, 50, 80, wall_cell, right=False)
        self.horizontal_line(60, 68, 25, wall_cell, down=False)
        self.horizontal_line(60, 68, 26, wall_cell, down=True)
        self.vertical_line(25, 26, 68, wall_cell, right=True)

        self.horizontal_line(72, 80, 25, wall_cell, down=False)
        self.horizontal_line(72, 80, 26, wall_cell, down=True)
        self.vertical_line(25, 26, 72, wall_cell, right=False)

        self.horizontal_line(65, 75, 39, wall_cell, down=False)
        self.horizontal_line(65, 75, 40, wall_cell, down=True)
        self.vertical_line(39, 40, 65, wall_cell, right=False)
        self.vertical_line(39, 40, 75, wall_cell, right=True)

        self.vertical_line(20, 40, 20, wall_cell, right=False)
        self.vertical_line(20, 40, 21, wall_cell, right=True)
        self.horizontal_line(20, 21, 20, wall_cell, down=False)
        self.horizontal_line(20, 21, 40, wall_cell, down=True)

    @property
    def carts(self):
        return None


class Level4(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(15, 30)
        self.end_point = indexes_2_pixels(75, 30)
        self.background_color = (182, 94, 38)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, orange_cell)

        self.random_on_rect(0, 0, 89, 59, cactus_cell, 100)
        self.random_on_rect(0, 0, 89, 59, empty_tree_cell, 100)
        self.random_on_rect(0, 0, 89, 59, orange_tree_cell, 100)

        self.rectangle(10, 20, 80, 40, orange_grass_cell)

        self.horizontal_line(10, 80, 20, wall_cell, down=True)
        self.horizontal_line(10, 80, 40, wall_cell, down=False)
        self.vertical_line(20, 40, 10, wall_cell, right=True)
        self.vertical_line(20, 40, 80, wall_cell, right=False)

    @property
    def carts(self):
        return [Cart(indexes_2_pixels(40, 25), 15, *indexes_2_pixels(20, 39), is_vertical=True),
                Cart(indexes_2_pixels(50, 25), 10, *indexes_2_pixels(20, 39), is_vertical=True),
                Cart(indexes_2_pixels(60, 25), 20, *indexes_2_pixels(20, 39), is_vertical=True)]


class Level5(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(78, 20)
        self.end_point = indexes_2_pixels(76, 38)
        self.background_color = (182, 94, 38)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, orange_cell)

        self.random_on_rect(0, 0, 89, 59, cactus_cell, 100)
        self.random_on_rect(0, 0, 89, 59, empty_tree_cell, 100)
        self.random_on_rect(0, 0, 89, 59, orange_tree_cell, 100)

        self.rectangle(70, 10, 80, 30, orange_grass_cell)
        self.rectangle(60, 15, 70, 25, orange_grass_cell)
        self.rectangle(10, 10, 60, 30, orange_grass_cell)
        self.rectangle(10, 30, 25, 50, orange_grass_cell)
        self.rectangle(25, 45, 80, 50, orange_grass_cell)
        self.rectangle(70, 35, 80, 45, orange_grass_cell)

        self.rectangle(45, 15, 55, 25, sand_cell)

        self.horizontal_line(70, 80, 10, wall_cell, down=True)
        self.horizontal_line(70, 80, 30, wall_cell, down=False)

        self.vertical_line(10, 15, 70, wall_cell, right=True)
        self.vertical_line(25, 30, 70, wall_cell, right=True)
        self.vertical_line(10, 30, 80, wall_cell, right=False)

        self.horizontal_line(60, 70, 15, wall_cell, down=True)
        self.horizontal_line(60, 70, 25, wall_cell, down=False)

        self.vertical_line(10, 15, 60, wall_cell, right=False)
        self.vertical_line(25, 30, 60, wall_cell, right=False)

        self.horizontal_line(10, 60, 10, wall_cell, down=True)
        self.horizontal_line(25, 60, 30, wall_cell, down=False)

        self.vertical_line(10, 50, 10, wall_cell, right=True)
        self.vertical_line(30, 45, 25, wall_cell, right=False)

        self.horizontal_line(25, 70, 45, wall_cell, down=True)
        self.horizontal_line(10, 80, 50, wall_cell, down=False)

        self.vertical_line(35, 45, 70, wall_cell, right=True)
        self.vertical_line(35, 50, 80, wall_cell, right=False)

        self.horizontal_line(70, 80, 35, wall_cell, down=True)

    @property
    def carts(self):
        return [Cart(indexes_2_pixels(50, 20), 15, *indexes_2_pixels(10, 30-1), is_vertical=True),
                Cart(indexes_2_pixels(30, 20), 15, *indexes_2_pixels(10, 30 - 1), is_vertical=True),
                Cart(indexes_2_pixels(20, 35), 10, *indexes_2_pixels(10, 25-1), is_vertical=False),
                Cart(indexes_2_pixels(40, 47), 3, *indexes_2_pixels(45, 50-1), is_vertical=True)]


class Level6(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(45, 48)
        self.end_point = indexes_2_pixels(45, 28)
        self.background_color = (182, 94, 38)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, orange_cell)

        self.random_on_rect(0, 0, 89, 59, cactus_cell, 100)
        self.random_on_rect(0, 0, 89, 59, empty_tree_cell, 100)
        self.random_on_rect(0, 0, 89, 59, orange_tree_cell, 100)

        self.rectangle(30, 40, 60, 50, orange_grass_cell)
        self.rectangle(35, 30, 40, 40, orange_grass_cell)
        self.rectangle(50, 30, 55, 40, orange_grass_cell)
        self.rectangle(10, 30, 40, 35, orange_grass_cell)
        self.rectangle(50, 30, 80, 35, orange_grass_cell)
        self.rectangle(10, 10, 20, 30, orange_grass_cell)
        self.rectangle(70, 10, 80, 30, orange_grass_cell)
        self.rectangle(20, 10, 70, 20, orange_grass_cell)
        self.rectangle(40, 20, 50, 30, orange_grass_cell)

        self.rectangle(20, 13, 30, 17, sand_cell)
        self.rectangle(60, 13, 70, 17, sand_cell)

        self.horizontal_line(30, 60, 50, wall_cell, down=False)
        self.horizontal_line(30, 35, 40, wall_cell, down=True)
        self.horizontal_line(40, 50, 40, wall_cell, down=True)
        self.horizontal_line(55, 60, 40, wall_cell, down=True)

        self.vertical_line(40, 50, 30, wall_cell, right=True)
        self.vertical_line(40, 50, 60, wall_cell, right=False)

        self.vertical_line(35, 40, 35, wall_cell, right=True)
        self.vertical_line(30, 40, 40, wall_cell, right=False)
        self.vertical_line(30, 40, 50, wall_cell, right=True)
        self.vertical_line(35, 40, 55, wall_cell, right=False)

        self.horizontal_line(10, 35, 35, wall_cell, down=False)
        self.horizontal_line(20, 40, 30, wall_cell, down=True)
        self.horizontal_line(55, 80, 35, wall_cell, down=False)
        self.horizontal_line(50, 70, 30, wall_cell, down=True)

        self.vertical_line(10, 35, 10, wall_cell, right=True)
        self.vertical_line(20, 30, 20, wall_cell, right=False)
        self.vertical_line(10, 35, 80, wall_cell, right=False)
        self.vertical_line(20, 30, 70, wall_cell, right=True)

        self.horizontal_line(10, 80, 10, wall_cell, down=True)
        self.horizontal_line(20, 40, 20, wall_cell, down=False)
        self.horizontal_line(50, 70, 20, wall_cell, down=False)

        self.vertical_line(20, 30, 40, wall_cell, right=True)
        self.vertical_line(20, 30, 50, wall_cell, right=False)

        self.horizontal_line(40, 50, 30, wall_cell, down=False)

    @property
    def carts(self):
        return [Cart(indexes_2_pixels(52, 39), 2, *indexes_2_pixels(50, 55-1), is_vertical=False),
                Cart(indexes_2_pixels(37, 39), 2, *indexes_2_pixels(35, 40 - 1), is_vertical=False),
                Cart(indexes_2_pixels(34, 32), 2, *indexes_2_pixels(30, 35 - 1), is_vertical=True),
                Cart(indexes_2_pixels(55, 32), 2, *indexes_2_pixels(30, 35 - 1), is_vertical=True),
                Cart(indexes_2_pixels(15, 29), 5, *indexes_2_pixels(10, 20-1), is_vertical=False),
                Cart(indexes_2_pixels(75, 29), 5, *indexes_2_pixels(70, 80-1), is_vertical=False),
                Cart(indexes_2_pixels(45, 20), 5, *indexes_2_pixels(40, 50-1), is_vertical=False)]


class Level7(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(15, 20)
        self.end_point = indexes_2_pixels(75, 30)
        self.background_color = (99, 197, 207)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, blue_cell)

        self.random_on_rect(0, 0, 89, 59, cloud1_cell, 100)
        self.random_on_rect(0, 0, 89, 59, cloud2_cell, 100)
        self.random_on_rect(0, 0, 89, 59, cloud3_cell, 100)

        self.rectangle(10, 10, 20, 50, blue_grass_cell)
        self.rectangle(20, 27, 70, 33, blue_grass_cell)
        self.rectangle(70, 10, 80, 50, blue_grass_cell)

        self.horizontal_line(10, 20, 10, wall_cell, down=True)
        self.horizontal_line(10, 20, 50, wall_cell, down=False)

        self.vertical_line(10, 50, 10, wall_cell, right=True)

        self.vertical_line(10, 27, 20, wall_cell, right=False)
        self.vertical_line(33, 50, 20, wall_cell, right=False)

        self.vertical_line(10, 50, 80, wall_cell, right=False)

    @property
    def carts(self):
        return None


class Level8(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(15, 12)
        self.end_point = indexes_2_pixels(75, 15)
        self.background_color = (99, 197, 207)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, blue_cell)

        self.random_on_rect(0, 0, 89, 59, cloud1_cell, 100)
        self.random_on_rect(0, 0, 89, 59, cloud2_cell, 100)
        self.random_on_rect(0, 0, 89, 59, cloud3_cell, 100)

        self.rectangle(10, 10, 20, 50, blue_grass_cell)
        self.rectangle(20, 40, 30, 50, blue_grass_cell)
        self.rectangle(30, 43, 45, 47, blue_grass_cell)
        self.rectangle(45, 10, 55, 47, blue_grass_cell)
        self.rectangle(55, 10, 80, 20, blue_grass_cell)

        self.horizontal_line(10, 20, 10, wall_cell, down=True)

        self.vertical_line(10, 15, 10, wall_cell, right=True)
        self.vertical_line(10, 15, 20, wall_cell, right=False)

        self.vertical_line(20, 30, 14, wall_cell, right=False)
        self.vertical_line(20, 30, 15, wall_cell, right=True)
        self.horizontal_line(14, 15, 20, wall_cell, down=False)
        self.horizontal_line(14, 15, 30, wall_cell, down=True)

        self.horizontal_line(10, 20, 50, wall_cell, down=False)

        self.horizontal_line(30, 45, 43, wall_cell, down=True)
        self.horizontal_line(30, 45, 47, wall_cell, down=False)

        self.vertical_line(30, 47, 55, wall_cell, right=False)

        self.horizontal_line(45, 55, 10, wall_cell, down=True)

        self.vertical_line(10, 20, 80, wall_cell, right=False)

    @property
    def carts(self):
        return None


class Level9(Scene):
    def __init__(self):
        super().__init__()
        self.start_point = indexes_2_pixels(15, 47)
        self.end_point = indexes_2_pixels(77, 15)
        self.background_color = (99, 197, 207)

    def init(self):
        self.init_board()
        self.walls = []

        self.rectangle(0, 0, 89, 59, blue_cell)

        self.random_on_rect(0, 0, 89, 59, cloud1_cell, 100)
        self.random_on_rect(0, 0, 89, 59, cloud2_cell, 100)
        self.random_on_rect(0, 0, 89, 59, cloud3_cell, 100)

        self.rectangle(10, 25, 20, 50, blue_grass_cell)
        self.rectangle(20, 25, 50, 30, blue_grass_cell)
        self.rectangle(40, 30, 50, 40, blue_grass_cell)
        self.rectangle(50, 30, 70, 40, blue_grass_cell)
        self.rectangle(60, 10, 70, 30, blue_grass_cell)
        self.rectangle(70, 10, 80, 20, blue_grass_cell)

        self.horizontal_line(10, 20, 50, wall_cell, down=False)

        self.vertical_line(40, 50, 10, wall_cell, right=True)
        self.vertical_line(40, 50, 20, wall_cell, right=False)

        self.horizontal_line(12, 18, 27, wall_cell, down=True)

        self.vertical_line(35, 40, 40, wall_cell, right=True)

        self.horizontal_line(40, 50, 40, wall_cell, down=False)

        self.vertical_line(32, 38, 60, wall_cell, right=False)

        self.horizontal_line(65, 70, 15, wall_cell, down=True)

    @property
    def carts(self):
        return None
