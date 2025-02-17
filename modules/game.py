import pygame

from modules.drawing import Drawing
from modules.ray_casting import ray_casting
from modules.player import Player
from modules.constants import *
from modules.maze_generator import MazeGenerator


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MazeEscape")
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
        maze_generator = MazeGenerator()
        maze_generator.generate_maze()
        maze_generator.fill_collision_walls()
        self.maze = maze_generator.maze
        self.collision_walls = maze_generator.collision_walls
        self.drawing = Drawing(self.screen)
        pygame.mouse.set_visible(False)

    def run(self):
        while self.running:
            self.drawing.draw_bg()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            is_finish = self.drawing.draw_walls(
                self.player, self.maze
            )
            self.player.movement(self.collision_walls)
            if is_finish:
                self.drawing.draw_finish_text()
            self.clock.tick(FPS)
            pygame.display.flip()
