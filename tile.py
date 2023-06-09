import pygame 
from settings import * 
# Tiles that make the maps
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((SIZE,SIZE))
        self.image = pygame.image.load('sprites/wall.png')
        self.rect = self.image.get_rect(topleft=pos)

