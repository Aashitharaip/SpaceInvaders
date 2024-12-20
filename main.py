import pygame
import random
#Initialise the pygame
pygame.init

#Background Image
screenImage = pygame.image.load('background-space.jpg')

#create the screen
screen= pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 380
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 40

#Bullet
#Ready - You cant see the bullet on the screen
#Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = 'ready'

def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

#Game Loop
running = True
while running:
    #RGB
    screen.fill((0,0,0))
    #Background Image
    screen.blit(screenImage, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
                # print('Left arrow is pressed')
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
                # print('Right arrow is pressed')
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('KeyStroke has been released')
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #Bullet Movement
    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()