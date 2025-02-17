import pygame

from modules.constants import *
from modules.ray_casting import ray_casting


class Drawing:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 34)

    def draw_bg(self):
        pygame.draw.rect(self.screen, 'blue', (0, 0, WIDTH, HEIGHT / 2))
        pygame.draw.rect(self.screen, 'gray', (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    def draw_walls(self, player, maze):
        is_finish = ray_casting(
            self.screen, player.pos, player.direction, maze
        )
        return is_finish

    def draw_finish_text(self):
        text = self.font.render('FINISH!', True, (255, 255, 255))
        text_x = (WIDTH - text.get_width()) / 2
        text_y = (HEIGHT - text.get_height()) / 2
        self.screen.blit(text, (text_x, text_y))