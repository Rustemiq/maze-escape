import pygame
from modules.constants import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.Surface(PLAYER_SIZE)
        pygame.draw.rect(self.image, "blue", (0, 0, *PLAYER_SIZE))
        self.rect = self.image.get_rect().move(x, y)
        self.x, self.y = self.rect.x, self.rect.y
        self.direction = math.pi / 2
        self.speed = 2

    def detect_collision(self, x, y, dx, dy, collision_walls):
        new_rect_x = pygame.rect.Rect(x + dx, y, self.rect.w, self.rect.h)
        new_rect_y = pygame.rect.Rect(x, y + dy, self.rect.w, self.rect.h)

        collide_list_x = new_rect_x.collidelistall(collision_walls)
        collide_list_y = new_rect_y.collidelistall(collision_walls)
        if len(collide_list_x) != 0:
            dx = 0
        if len(collide_list_y) != 0:
            dy = 0
        return dx, dy

    def movement(self, collision_walls):
        keys = pygame.key.get_pressed()
        sin_d = math.sin(self.direction)
        cos_d = math.cos(self.direction)
        dx, dy = 0, 0
        if keys[pygame.K_w]:
            dx += self.speed * cos_d
            dy += self.speed * sin_d
        if keys[pygame.K_s]:
            dx -= self.speed * cos_d
            dy -= self.speed * sin_d
        if keys[pygame.K_a]:
            dx += self.speed * sin_d
            dy += -self.speed * cos_d
        if keys[pygame.K_d]:
            dx += -self.speed * sin_d
            dy += self.speed * cos_d
        if keys[pygame.K_RIGHT]:
            self.direction += 0.03
        if keys[pygame.K_LEFT]:
            self.direction -= 0.03
        dx, dy = self.detect_collision(self.x, self.y, dx, dy, collision_walls)
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        ray_x = self.rect.centerx + math.cos(self.direction) * WIDTH
        ray_y = self.rect.centery + math.sin(self.direction) * HEIGHT
        pygame.draw.line(
            screen,
            "red",
            (self.pos),
            (ray_x, ray_y),
        )

    @property
    def pos(self):
        return self.rect.centerx, self.rect.centery
