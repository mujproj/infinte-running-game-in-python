import pygame 
from pygame import mixer
import math

pygame.init()

# SCREEN WIDTH
SCREEN_WIDTH = 1000

# screen height
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('background.jpg')

# defining a function for displaying the background image
def displayBackground():
    screen.blit(background, (0, 0))

# defining variables for rectangle
rectX1 = 600
rectY1 = 396
rect2X2 = 200
rectX2 = 30
rectY2 = 40
rectX_change = -1
# defiing fnction for drawing rectangle
def drawRect(x, y, x2, y2):
    pygame.draw.rect(screen, (255, 255, 255), (x, y, x2, y2))

player = pygame.image.load('player1.png')

# setting dimenions of the player
playerX = 300
playerY = 372

# defining display the man image
def displayPlayer(x, y):
    screen.blit(player, (x, y))

score_val = 0

font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def scoreDisplay(x, y):
    score = font.render("SCORE IS :" + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

# checking for collision
def collision(x1, y1, x2, y2):
    if math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1))) < 30:
        return True
    
    else:
        return False

isbackgroundmusic = True 
def soundBackground():
    if isbackgroundmusic:
        mixer.music.load('backgroundsound.mp3')
        mixer.music.play()

def soundJump():
    mixer.music.load('jump3.mp3')
    mixer.music.play()

running = True
while running:
    
    displayBackground()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY = 330
                isbackgroundmusic = False
                soundJump()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerY = 372
                soundJump()
                isbackgroundmusic = True

    drawRect(rectX1, rectY1, rectX2, rectY2)
    rectX1 += rectX_change

    drawRect(rect2X2, rectY1, rectX2, rectY2)
    rect2X2 += rectX_change

    if rectX1 < 0:
        rectX1 = 999
    
    if rect2X2 < 0:
        rect2X2 = 999

    displayPlayer(playerX, playerY)

    if collision(playerX, playerY, rectX1, rectY1):
        score_val = 0
        scoreDisplay(textX, textY)

    else:
        score_val += 1
        scoreDisplay(textX, textY)

    soundBackground()
    pygame.display.update()


    