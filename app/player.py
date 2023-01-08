import pygame


class Player:
  def __init__(self, name, sprite):
    self.name = name
    self.sprite_url = sprite
    self.sprite = pygame.image.load(self.sprite_url)