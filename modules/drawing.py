import pygame

from modules.ray_casting import ray_casting
from modules.constants import *


def draw_all(screen, player):
    player.draw(screen)
    ray_casting(screen, player.pos, player.direction)
    with open('maze.txt', 'r') as maze:
        lines = maze.read().split('\n')
        for i, row in enumerate(lines):
            for j, symbol in enumerate(list(row)):
                if symbol == '1':
                    pygame.draw.rect(
                        screen, 'black', (j * TILE_SIZE, i * TILE_SIZE,
                                          TILE_SIZE, TILE_SIZE))