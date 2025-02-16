import pygame
import math

from modules.constants import *

def ray_casting(screen, player_pos, player_direction):
    cur_dir = player_direction - FOV / 2
    x0, y0 = player_pos
    for ray in range(NUM_RAYS):
        sin_d = math.sin(cur_dir)
        cos_d = math.cos(cur_dir)
        for depth in range(MAX_DEPTH):
            x = x0 + depth * cos_d
            y = y0 + depth * sin_d
            pygame.draw.line(screen, "gray", player_pos, (x, y), 2)
        cur_dir += DELTA_ANGLE
