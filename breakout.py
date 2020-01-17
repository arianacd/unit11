# by ariana daney
# last modified january 17, 2020
# breakout game
import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball
# commented out code is there for later use

pygame.init()

win_sound = pygame.mixer.Sound('applause4.wav')


def win_game(main_surface):
    """
    this function displays "winner!" when the player wins
    :param main_surface: where the words are displayed
    :return: nothing
    """
    main_surface.fill((255, 200, 200))
    font = pygame.font.SysFont('Comic Sana MS', 100)
    label = font.render('WINNER!', 1, (0, 0, 255))
    main_surface.blit(label, (40, 250))
    win_sound.play()
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()


def game_over(main_surface):
    """
    this function displays "game over" on the screen when the player looses
    :param main_surface: the surface they words are projected on
    :return: nothing
    """
    main_surface.fill((0, 0, 0))
    font = pygame.font.SysFont('Comic Sana MS', 50)
    label = font.render('GAME OVER', 1, (255, 0, 0))
    main_surface.blit(label, (100, 250))
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()


def main():
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]

    # creates a sprite fo the sprite groups so the bricks and paddle can collide with the ball
    bricks_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    # creates a main surface with a picture as the background
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    bg = pygame.image.load("construction.jpeg")
    main_surface.blit(bg, (0, 0))

    # the following code displays the bricks on the screen
    x_pos = BRICK_SEP
    y_pos = BRICK_Y_OFFSET
    for hue in colors:
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, hue)
                my_brick.rect.x = x_pos
                my_brick.rect.y = y_pos
                bricks_group.add(my_brick)
                main_surface.blit(my_brick.image, my_brick.rect)
                x_pos += BRICK_WIDTH + BRICK_SEP
            y_pos += BRICK_HEIGHT + BRICK_SEP
            x_pos = BRICK_SEP
    # displays the paddle
    my_paddle = paddle.Paddle(main_surface, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_group.add(my_paddle)
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image, my_paddle.rect)
    # displays the ball
    my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    my_ball.rect.x = APPLICATION_WIDTH/2
    my_ball.rect.y = APPLICATION_HEIGHT/2
    main_surface.blit(my_ball.image, my_ball.rect)

    tries = 0

    while True:
        main_surface.fill(WHITE)
        main_surface.blit(bg, (0, 0))
        # makes the paddle move with the mouse
        for a_brick in bricks_group:
            main_surface.blit(a_brick.image, a_brick.rect)
        my_paddle.move(pygame.mouse.get_pos())
        main_surface.blit(my_paddle.image, my_paddle.rect)
        my_ball.move()
        my_ball.collide(paddle_group)
        my_ball.collide_brick(bricks_group)
        main_surface.blit(my_ball.image, my_ball.rect)
        end_sound = pygame.mixer.Sound('maybe-next-time.wav')
        # resets the ball if it goes off the screen
        if my_ball.rect.bottom >= APPLICATION_HEIGHT:
            end_sound.play()
            my_ball.rect.y = APPLICATION_HEIGHT / 2
            tries += 1
        # displays "game over" if the player looses. The >= makes the game over displays even when the ball
        # keeps hitting the bottom of the screen
        if tries >= 3:
            game_over(main_surface)
        # displays "winner!" when the player wins by breaking all the bricks
        if len(bricks_group) == 0:
            win_game(main_surface)
        pygame.display.update()
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()


main()
