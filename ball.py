import pygame
# commented out code is there for later use

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, window_width, window_height, radius):
        super().__init__()
        self.color = color
        self.window_width = window_width
        self.window_height = window_height
        self.radius = radius

        self.sound = pygame.mixer.Sound('Hammering_Soung.wav')

        # self.image = pygame.Surface((radius, radius))
        # self.image.fill((255, 255, 255))
        self.image = pygame.image.load("allison.png")
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created.
        self.x_speed = 6
        self.y_speed = 5

    def move(self):
        """
        this function makes the ball move and bounce off walls
        :return: nothing
        """
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.left < 0 or self.rect.right > self.window_width:
            self.x_speed = -self.x_speed
        if self.rect.top < 0 or self.rect.bottom > self.window_height:
            self.y_speed = -self.y_speed

    def collide(self, sprite_group):
        """
        this function makes it so the ball can bounce off another object and go in the other direction
        :param sprite_group: the paddle
        :return: nothing
        """
        if pygame.sprite.spritecollide(self, sprite_group, False):
            self.y_speed = -self.y_speed

    def collide_brick(self, sprite_group):
        """
        this function allows the ball to collide and break bricks
        :param sprite_group: the bricks
        :return: nothing
        """
        if pygame.sprite.spritecollide(self, sprite_group, True):
            self.sound.play()
            self.y_speed = -self.y_speed




