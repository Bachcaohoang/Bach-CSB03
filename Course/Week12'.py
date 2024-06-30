import pygame
import sys

pygame.init()

screenW = 600
screenH = 600

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('Pong')

ballIMG = pygame.image.load('Course/ball.png')
paddleIMG = pygame.image.load('Course/paddle.png')

ballx = screenW/2
bally = screenH/2

player1 = 5
player11 = screenH/2

player2 = 590
player22 = screenH/2

wpress = False
spress = False
uppress = False
downpress = False

clock = pygame.time.Clock()  # Create a clock to control the frame rate

while True:  # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                wpress = True
            elif event.key == pygame.K_s:
                spress = True
            elif event.key == pygame.K_UP:
                uppress = True
            elif event.key == pygame.K_DOWN:
                downpress = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                wpress = False
            elif event.key == pygame.K_s:
                spress = False
            elif event.key == pygame.K_UP:
                uppress = False
            elif event.key == pygame.K_DOWN:
                downpress = False

    # Game logic goes here
    # Update the ball and paddles based on user input and game state

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black

    # Draw the game elements
    screen.blit(ballIMG, (ballx, bally))
    screen.blit(paddleIMG, (player1, player11))
    screen.blit(paddleIMG, (player2, player22))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)