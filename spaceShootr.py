
import pygame
from pygame import mixer
import random
import math

import pygame_menu
import time

pygame.init()

# screen display
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])
screen1 = pygame.display.set_mode([screen_width, screen_height])
# background sound
mixer.music.load('D://my games//space shooter//background.wav')
mixer.music.play(-1)
game_over = False

# title and window logo
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("D://my games//space shooter//ufo.png")
icon = pygame.transform.scale(icon, (64, 64))
pygame.display.set_icon(icon)

# background
background = pygame.image.load('D://my games//space shooter//background.png')
background_x = 0
background_y = 0
background = pygame.transform.scale(background, (500, 500))

# bullet
# Ready -- you can't see bullet on screen
# Fire -- the bullet is moving
bullet = pygame.image.load('D://my games//space shooter//laser.png')
bulletX = 0
bulletY = 420
bulletX_change = 0
bulletY_change = 4
bullet = pygame.transform.scale(bullet, (40, 60))
bullet_state = "ready"

#bullet 1
bullet1 = pygame.image.load('D://my games//space shooter//laser.png')
bulletX1 = 0
bulletY1 = 420
bulletX1_change = 0
bulletY1_change = 4
bullet1 = pygame.transform.scale(bullet, (40, 60))
bullet1_state = "ready"

# player
playerImg = pygame.image.load('D://my games//space shooter//spaceship.png')
playerX = 200
playerY = 420
playerImg = pygame.transform.scale(playerImg, (80, 80))
playerX_change = 0
playerY_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_ememies = 6

for i in range(num_of_ememies):
    enemyImg.append(pygame.image.load('D://my games//space shooter//enemy.png'))
    enemyImg.append(pygame.transform.scale(enemyImg[i], (40, 40)))
    enemyX.append(random.randint(0, 420))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(4)
    enemyY_change.append(15)
    
    
        
    
# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 0
textY = 0

# game over
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,0,0))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text,(50,200))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x-10, y-65))


def fire_bullet1(x, y):
    global bullet1_state
    bullet1_state = "fire"
    screen.blit(bullet1, (x-10, y-65))



def isCOllision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance <= 30:
        return True
    else:
        return False


def isCOllision1(enemyX, enemyY, bulletX1, bulletY1):
    distance1 = math.sqrt((math.pow(enemyX - bulletX1, 2)) + (math.pow(enemyY - bulletY1, 2)))
    if distance1 <= 30:
        return True
    else:
        return False
def isCOllision2(enemyX, enemyY, playerX,plauerY):
    distance1 = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - plauerY, 2)))
    if distance1 <= 50:
        return True
    else:
        return False

def loop():
    global playerX,playerY,bulletX,bulletX1,bulletY,bulletY1,bullet1_state,bullet_state,bullet1_state,playerX_change,score_value,playerY_change,num_of_ememies,game_over
    # game loop
    # running = True
    while True:
        screen.blit(background, (background_x, background_y))
        player(playerX, playerY)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
        
            # if keystroke is pressed check whether its right or left
        # if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5  
                if event.key == pygame.K_UP:
                    playerY_change = -3  
                if event.key == pygame.K_DOWN:
                    playerY_change = +3
                if event.key == pygame.K_KP_ENTER:
                    if bullet_state is "ready":
                        bulletSound = mixer.Sound("D://my games//space shooter//laser.wav")
                        bulletSound.play()
                        bulletX = playerX
                        bulletY = playerY
                        fire_bullet(bulletX, bulletY)
        
                    if bullet1_state is "ready":
                        bulletsound = mixer.Sound('D://my games//space shooter//laser.wav')
                        bulletsound.play()
                        bulletX1 = playerX +64
                        bulletY1 = playerY
                        fire_bullet1(bulletX1, bulletY1)
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.4
                if event.key == pygame.K_RIGHT:
                    playerX_change = +0.4
                if event.key == pygame.K_UP:
                    playerY_change = 0
                if event.key == pygame.K_DOWN:
                    playerY_change = 0
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"
        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change
    
        if bulletY1 <= 0:
            bulletY1 = 480
            bullet1_state = "ready"
        if bullet1_state is "fire":
            fire_bullet1(bulletX1, bulletY1)
            bulletY1 -= bulletY1_change
    
        playerX += playerX_change
        playerY += playerY_change
        show_score(textX,textY)
    
        
    
        if playerX <= 0:
            playerX = 0
        if playerX >= 420:
            playerX = 420
        if playerY>=420:
            playerY = 420
        if playerY<=0:
            playerY = 0
        
        for i in range(num_of_ememies):
            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 3
                enemyY[i] += enemyY_change[i]
            if enemyX[i] >= 464:
                enemyX_change[i] = -3
                enemyY[i] += enemyY_change[i]
            
            if enemyY[i] >= 400:
                for j in range(num_of_ememies):
                    enemyY[i] == 600
                game_over_text()
                break
    
    
            collision = isCOllision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound =mixer.Sound("D://my games//space shooter//explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 420)
                enemyY[i] = random.randint(0, 50)
            
            collision1 = isCOllision1(enemyX[i], enemyY[i], bulletX1, bulletY1)
            if collision1:
                explosionSound1 =mixer.Sound("D://my games//space shooter//explosion.wav")
                explosionSound1.play()
                bulletY1 = 480
                bullet1_state = "ready"
                score_value += 1
                enemyX[i] = random.randint(0, 420)
                enemyY[i] = random.randint(0, 50)
            collision2 = isCOllision2(enemyX[i], enemyY[i],playerX, playerY)
            if collision2:
                for j in range(num_of_ememies):
                    enemyX[i]=600
                    enemyY[i] = 600
                explosionSound =mixer.Sound("D://my games//space shooter//explosion.wav")
                explosionSound.play()
                game_over_text()
                time.sleep(2)
                break
    
            enemy(enemyX[i], enemyY[i],i)
    
        pygame.display.update()

menu = pygame_menu.Menu('SPACE SHOOTER', 500, 500,
                        theme=pygame_menu.themes.THEME_BLUE)

image_path = pygame_menu.baseimage.IMAGE_EXAMPLE_PYGAME_MENU
menu.add.image(image_path, angle=0, scale=(0.15, 0.15))

menu.add.text_input('Name :', default=' ')
menu.add.button('Play', loop) 
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)

