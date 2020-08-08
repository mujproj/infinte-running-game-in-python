import pygame
import math
import time
from pygame import mixer

pygame.init()

# screen width 
SCREEN_WIDTH = 1000

# screen height
SCREEN_HEIGHT = 600

# setting the screen dimensions
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# loading the background image
background = pygame.image.load('background.jpg')

# loading the player image
player = pygame.image.load('player1.png')

# player dimensions
playerX = 300
playerY = 375
# player_change = 1

# defining a function to display man image
def displayPlayer(x, y):
    screen.blit(player, (x, y))

# rectangle dimension X 
rect1X1 = 600
rectX2 = 30
rect2X1 = 200

# rectangle dimension Y
rectY1 = 396
rectY2 = 40

# change in dimension of rect x
rectX_change = -1

# function to display rectangle
def displayRect(x, y, x2, y2):
    pygame.draw.rect(screen, (255, 0, 0), (x, y, x2, y2))

# defining function for collision
def collision(x1, y1, x2, y2):
    if abs(math.sqrt(((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1)))) < 30:
        return True
    else:
        return False

# score 
score_val = 0

# font for score
font = pygame.font.Font('freesansbold.ttf', 32)

# setting the dimesin of the text
textX = 10
textY = 10

# defining a function for displaying the score
def displayScore(x, y):
    score = font.render("Score :" + str(int(score_val)), True, (255, 255, 255))
    screen.blit(score, (x, y))
    # time.sleep(0.1)

# function for displaying sound of jump
def soundJump():
    mixer.music.load('jump3.mp3')
    mixer.music.play()

isBackgroundTrue = True 
# function for displaying sound of background
def soundBackground():
    mixer.music.load('backgroundsound.mp3')
    mixer.music.play()

# setting up a variable to hold the screen
running = True

# game loop starts
while running:

    screen.fill((0, 0, 0))
    # print(background)
    # print(displayBackground())
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY = 330
                isBackgroundTrue = False
                soundJump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerY = 375
                isBackgroundTrue = True
                soundJump()

    hurdle1 = displayRect(rect1X1, rectY1, rectX2, rectY2)
    rect1X1 += rectX_change
    hurdle2 = displayRect(rect2X1, rectY1, rectX2, rectY2)
    rect2X1 += rectX_change

    if rect1X1 < 0:
        rect1X1 = 999
    
    if rect2X1 < 0:
        rect2X1 = 999

    rectX_change -= 0.0001
    # playerX += player_change
    displayPlayer(playerX, playerY)
    # if playerX == 999:
    #     playerX = 0
    
    # print(math.sqrt(((playerX - rect1X1)*(playerX - rect1X1)) + ((playerY - rectY1)*(playerY - rectY1))))
    # print(playerY - rectY1)
    if collision(playerX, playerY, rect1X1, rectY1) or collision(playerX, playerY, rect2X1, rectY1):
        score_val = 0
        displayScore(textX, textY)

    else:
        score_val += 0.1
        displayScore(textX, textY)

    if isBackgroundTrue:
        soundBackground()

    pygame.display.update()
