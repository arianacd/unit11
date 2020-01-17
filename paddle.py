import pygame
# commented out code is there for later use


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        super().__init__()
        self.color = color
        self.width = width
        self.height = height

        self.main_surface = main_surface

        # Create a surface with the correct height and width
        self.image = pygame.Surface((width, height))
        self.image = pygame.image.load("900-179-2.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # self.image.fill(color)

    def move(self, position):
        """
        this function lets the paddle move, only in the x direction
        :param position:
        :return: nothing
        """
        self.rect.x = position[0]
