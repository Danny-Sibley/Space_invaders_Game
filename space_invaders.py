import pygame
import random
import math
from pygame import mixer
from space_invaders_pkg.Player_class import Player
from space_invaders_pkg.Image_Load import Image_Load


# initialize the pygame
pygame.init()

# create the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Background, instantiates Image load class
imageload = Image_Load()
background = imageload.image_display('space_invaders_pkg/space_background.jpg')

# background sound
mixer.music.load('space_invaders_pkg/Background_music.mp3')
mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Danny's Space Invaders Game")
icon = imageload.image_display('space_invaders_pkg/spaceship.png')
pygame.display.set_icon(icon)

# player
# instantiates class with player coordinates 370 and 480
player_char = Player(370, 480)
playerimg = imageload.image_display('space_invaders_pkg/spaceship_player.png')
player_char_x_change = 0

# enemy
enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('space_invaders_pkg/alien.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    # enemy speed
    enemyx_change.append(2)
    enemyy_change.append(40)

# bullet
# ready :  you can't see bullet onscrenn
# fire : the bullet is currently moving
bulletimg = pygame.image.load('space_invaders_pkg/bullet.png')
bullet_char = Player(0, 480)
bulletx = bullet_char.x
bullety = bullet_char.y
bulletx_change = bullet_char.pos_change(0)
bullety_change = bullet_char.pos_changeY(5)
bullet_state = "ready"

# stores score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 16)
textx = 10
texty = 10

# game instructions
game_font = pygame.font.Font('freesansbold.ttf', 16)

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def game_text():
    game_text = game_font.render(
        "Move the spaceship with left and right arrow keys. Shoot with spaceebar", True, (255, 255, 255))
    screen.blit(game_text, (100, 10))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) +
                         (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


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
                # player speed
                player_char_x_change = player_char.pos_change(-4)
            if event.key == pygame.K_RIGHT:
                # player speed
                player_char_x_change = player_char.pos_change(4)
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound(
                        'space_invaders_pkg/bullet_sound.mp3')
                    bullet_sound.play()
                    bulletx = player_char.x
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_char_x_change = player_char.pos_change(0)

# Checking for boundaries of spaceship
    player_char.x += player_char_x_change
    if player_char.x <= 0:
        player_char.x = 0
    elif player_char.x >= 736:
        player_char.x = 736

    # enemy movement
    for i in range(num_of_enemies):
        # game over
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            # enemy speed
            enemyx_change[i] = 2
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            # enemy speed
            enemyx_change[i] = -2
            enemyy[i] += enemyy_change[i]

        # collision
        collision = isCollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            collision_sound = mixer.Sound('space_invaders_pkg/explosion2.mp3')
            collision_sound.play()
            bullety = 480
            bullet_state = 'ready'
            score_value += 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)

    # bullet movement
    if bullety <= 0:
        bullety = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change

    game_text()
    player(player_char.x, player_char.y)
    show_score(textx, texty)
    pygame.display.update()
