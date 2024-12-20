import pygame
import random
from math import sqrt
#Initialise the pygame
pygame.init
pygame.font.init()

#Background Image
screenImage = pygame.image.load('images/background-space.jpg')

#create the screen
screen= pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('images/space-invaders.png')
playerX = 380
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

no_of_enemies = 6
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('images/alien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.1)
    enemyY_change.append(40)

#Bullet
#Ready - You cant see the bullet on the screen
#Fire - The bullet is currently moving
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.5
bullet_state = 'ready'

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render(f'Score: {score_value}',True, (255,255,255))
    screen.blit(score,(x,y))


def player(x,y):
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY,i):
    distance = sqrt((enemyX[i] - enemyY[i]) ** 2 + (bulletX - bulletY) ** 2)
    if distance < 27:
        return True
    return False


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
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print('KeyStroke has been released')
                playerX_change = 0

    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(no_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] < 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        #Collision
        collision = isCollision(enemyX, enemyY, bulletX, bulletY,i)
        if collision == True:
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)  

    #Bullet Movement
    if bulletY < 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()