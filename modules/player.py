import pygame
import math
from modules.constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(PLAYER_SIZE)
        pygame.draw.rect(self.image, "blue", (0, 0, *PLAYER_SIZE))
        self.rect = self.image.get_rect().move(x, y)
        self.direction = 0
        self.speed = 4

    def movement(self):
        keys = pygame.key.get_pressed()
        sin_d = math.sin(self.direction)
        cos_d = math.cos(self.direction)
        if keys[pygame.K_w]:
            self.rect.x += self.speed * cos_d
            self.rect.y += self.speed * sin_d
        if keys[pygame.K_s]:
            self.rect.x -= self.speed * cos_d
            self.rect.y -= self.speed * sin_d
        if keys[pygame.K_a]:
            self.rect.x += self.speed * sin_d
            self.rect.y += -self.speed * cos_d
        if keys[pygame.K_d]:
            self.rect.x += -self.speed * sin_d
            self.rect.y += self.speed * cos_d
        if keys[pygame.K_RIGHT]:
            self.direction += 0.05
        if keys[pygame.K_LEFT]:
            self.direction -= 0.05

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        ray_x = self.rect.centerx + math.cos(self.direction) * WIDTH
        ray_y = self.rect.centery + math.sin(self.direction) * HEIGHT
        pygame.draw.line(
            screen,
            "red",
            (self.rect.centerx, self.rect.centery),
            (ray_x, ray_y),
        )

    @property
    def pos(self):
        return self.rect.centerx, self.rect.centery
