import pygame
from modules.drawing import draw_all
from modules.player import Player
from modules.constants import *
from modules.maze_generator import MazeGenerator


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("2d_version")
        size = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.player = Player(
            TILE_SIZE, TILE_SIZE, self.player_group, self.all_sprites
        )
        self.running = True
        MazeGenerator().generate_maze()

    def run(self):
        while self.running:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            draw_all(self.screen, self.player)
            self.player.movement()
            #ray_casting(self.screen, self.player.pos, self.player.direction)
            self.clock.tick(FPS)
            pygame.display.flip()