from pygame import *
init()
from random import randint
from time import time as t

class Enemy():
    def __init__(self, collision):
        self.rect = rect.Rect(randint(1500, 3000), randint(0, 700), 50, 50)
        self.collision = collision
        enemies.append(self)
    
def refresh_enemies():
    global lives
    for enemy in enemies:
        draw.rect(w, (255, 0, 0), enemy.rect)
        enemy.rect.x -= int(speed)
        if enemy.rect.colliderect(vehicle):
            if enemy.collision == False:
                enemy.collision = True
                lives -= 1
        if enemy.rect.x <= 0:
            enemy.rect.x = 1500
            enemy.rect.y = randint(0, 700)
            enemy.collision = False

def check_finish():
    global close
    global win
    marker.x -= int(speed)
    if marker.x <= -100000:
        close = True
        win = True
    if lives <= 0:
        close = True

def move_vehicle():
    global speed
    global accelerate
    global deccelerate
    keyspressed = key.get_pressed()
    if keyspressed[K_d] or keyspressed[K_RIGHT]:
        accelerate = True
    else:
        accelerate = False
    if keyspressed[K_a] or keyspressed[K_LEFT]:
        deccelerate = True
    else:
        deccelerate = False
    if (keyspressed[K_w] or keyspressed[K_UP]) and vehicle.y > 0:
        vehicle.y -= 10
    if (keyspressed[K_s] or keyspressed[K_DOWN]) and vehicle.y < 720:
        vehicle.y += 10
    if accelerate:
        if speed <= 300:
            speed += 0.5
    if deccelerate and speed > 0:
        speed -= 1  
    if accelerate == False and deccelerate == False:
        speed -= 0.05
    if speed < 0:
        speed = 0
    draw.rect(w, (0, 255, 0), vehicle)

closeall = False
while closeall == False:
    w = display.set_mode((1500, 750))
    display.set_caption('Acceleration')
    marker = rect.Rect(0, 0, 0, 0)
    lives = 5
    enemies = []
    for i in range(5):
        new_enemy = Enemy(False)
    speed = 0
    vehicle = rect.Rect(100, 300, 50, 30)
    clock = time.Clock()
    close = False
    accelerate = False
    deccelerate = False
    win = False
    start = t()
    while close == False:
        w.fill((255, 255, 255))
        w.blit(font.SysFont('Arial', 50).render('speed:' + str(int(speed)), True, (0, 0, 0)), (100, 0))
        w.blit(font.SysFont('Arial', 50).render('lives:' + str(lives), True, (0, 0, 0)), (300, 0))
        for i in event.get():
            if i.type == QUIT:
                close = True
                closeall = True
        move_vehicle()
        refresh_enemies()
        check_finish()
        display.update()
        clock.tick(60)
    end = t()
    if win:
        close = False
        while close == False:
            w.fill((255, 255, 255))
            if closeall:
                close = True
            for i in event.get():
                if i.type == QUIT:
                    close = True
                    closeall = True
            keyspressed = key.get_pressed()
            if keyspressed[K_1]:
                close = True
            w.blit(font.SysFont('Arial', 50).render('you win! (1-try again)', True, (255, 0, 0)), (100, 100))
            w.blit(font.SysFont('Arial', 50).render('time:' + str(end - start) + ' seconds', True, (255, 0, 0)), (100, 150))
            display.update()
            clock.tick(60)
    else:
        close = False
        while close == False:
            w.fill((255, 255, 255))
            if closeall:
                close = True
            for i in event.get():
                if i.type == QUIT:
                    close = True
                    closeall = True
            keyspressed = key.get_pressed()
            if keyspressed[K_1]:
                close = True
            w.blit(font.SysFont('Arial', 50).render('Game over (1-try again)', True, (255, 0, 0)), (100, 100))
            display.update()
            clock.tick(60)