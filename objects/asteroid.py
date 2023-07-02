import pygame
import random
from config import SCREEN_HEIGHT, SCREEN_WIDTH, RED

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(SCREEN_HEIGHT)

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = -20
            self.rect.x = random.randrange(SCREEN_WIDTH)