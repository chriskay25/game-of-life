import pygame
import numpy as np

class GameOfLife:
    def __init__(self, surface, width=1920, height=1080, scale=10, offset=1, active_color=(255, 255, 255), inactive_color=(50, 50, 50)):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)
