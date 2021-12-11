import pygame
import random

# initialize the pygame
pygame.init()

# create the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Background
background = pygame.image.load('space_background.jpg')

#Title and Icon
pygame.display.set_caption("Danny's Space Invaders Game")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('spaceship_player.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
enemyimg = pygame.image.load('alien.png')
enemyx = random.randint(0, 800)
enemyy = random.randint(50, 150)
enemyx_change = 3
enemyy_change = 40

# bullet
# ready :  you can't see bullet onscrenn
# fire : the bullet is currently moving
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"

# player function


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y):
    screen.blit(enemyimg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


# game loop
running = True
while running:
    # RGB grey color
    screen.fill((0, 0, 0))
    # background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = - 5
            if event.key == pygame.K_RIGHT:
                playerx_change = + 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

# Checking for boundaries of spaceship
    playerx += playerx_change

    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736

    enemyx += enemyx_change

    if enemyx <= 0:
        enemyx_change = 3
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -3
        enemyy += enemyy_change

    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(playerx, bullety)
        bullety -= bullety_change

    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()
