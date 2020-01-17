import pygame
# commented out code is there for later use


class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()

        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.image.load("brick.png")

        self.rect = self.image.get_rect()

        # self.image.fill(color)


