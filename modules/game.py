import pygame
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

    def run(self):
        while self.running:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            ray_casting(
                self.screen, self.player.pos, self.player.direction, self.maze
            )
            self.player.movement(self.collision_walls)

            #self.player.draw(self.screen)
            #for i, row in enumerate(self.maze):
            #    for j, symbol in enumerate(list(row)):
            #        if symbol == 1:
            #            pygame.draw.rect(
            #                self.screen, 'black', (j * TILE_SIZE, i * TILE_SIZE,
            #                                  TILE_SIZE, TILE_SIZE))

            self.clock.tick(FPS)
            pygame.display.flip()
