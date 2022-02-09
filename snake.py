import pygame
import math
from random import randrange

RES = 800
SIZE = 50

g = 1
x, y = 400, 400
BREAK_FLAG = None
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 8
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
dirs_1 = {'↑': True, '↓': True, '→': True, '←': True, }
pygame.init()

sr = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sr.fill(pygame.Color('black'))

    [(pygame.draw.rect(sr, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sr, pygame.Color('red'), (*apple, SIZE, SIZE))

    x += dx * SIZE 
    y += dy * SIZE 
    snake.append((x, y))
    snake = snake[-length:]
    pygame.display.flip()

    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("You Lose")
            print("Score: " + str(score))
            exit()

    if snake[-1] == apple:
        apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
        length += 1
        score += 1
    if x < 0:               
        x, y = 800, y
    elif x > RES - SIZE:
        x, y = 0, y
    elif y < 0:
        x, y = x, 800
    elif y > RES - SIZE:
        x, y = x, 0 

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True,}


    elif key[pygame.K_UP]:
        if dirs_1['↑']:
            dx, dy = 0, -1
            dirs_1 = {'↑': True, '↓': False, '→': True, '←': True, }
    elif key[pygame.K_DOWN]:
        if dirs_1['↓']:
            dx, dy = 0, 1
            dirs_1 = {'↑': False, '↓': True, '→': True, '←': True, }
    elif key[pygame.K_RIGHT]:
        if dirs_1['→']:
            dx, dy = 1, 0
            dirs_1 = {'↑': True, '↓': True, '→': True, '←': False, }
    elif key[pygame.K_LEFT]:
        if dirs_1['←']:
            dx, dy = -1, 0
            dirs_1 = {'↑': True, '↓': True, '→': False, '←': True, } 

     
