import random

import pygame

import config
from game_objects import Wall
from transformation import indexes_2_pixels, indexes_2_rect


class Scene:
    def __init__(self):
        self.walls = []
        self.board = self.init_board()

    def init_board(self):
        return [[None for _ in range(config.screen_size[1] // config.cell_size)]
                for _ in range(config.screen_size[0] // config.cell_size)]

    def add_walls(self, *walls):
        for wall in walls:
            self.walls.append(wall)

    def add_cell(self, row, col, cell):
        cell.pos = indexes_2_pixels(col, row)
        cell.rect = indexes_2_rect(col, row, with_offset=True)
        self.board[col][row] = cell

    def horizontal_line(self, start, end, row, cell, down=False):
        for x in range(start, end + 1):
            if cell.is_wall:
                self.add_walls(Wall(indexes_2_pixels(start, row+int(down)), indexes_2_pixels(end+1, row+int(down))))
            self.add_cell(row, x, cell)

    def vertical_line(self, start, end, column, cell, right=False):
        for x in range(start, end + 1):
            if cell.is_wall:
                self.add_walls(Wall(indexes_2_pixels(column+int(right), start), indexes_2_pixels(column+int(right), end+1)))
            self.add_cell(x, column, cell)

    def rectangle(self, i1, j1, i2, j2, cell):
        for row in range(j1, j2 + 1):
            self.horizontal_line(i1, i2, row, cell)

    def single(self, row, col, cell):
        self.add_cell(col, row, cell)

    def random_on_rect(self, i1, j1, i2, j2, cell, n):
        for i in range(n):
            random_i = random.randint(i1, i2)
            random_j = random.randint(j1, j2)
            self.single(random_i, random_j, cell)

    def blit(self, screen):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is None:
                    continue
                screen.blit(self.board[i][j].image, indexes_2_pixels(i, j))

    def draw_walls(self, screen):
        for wall in self.walls:
            wall.draw(screen)

    def draw_hitboxes(self, screen):
        for wall in self.walls:
            wall.draw_hitbox(screen)
