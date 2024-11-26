import pygame
import random

pygame.init()

width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("VB Snake Game")

snake_x, snake_y = width / 2, height / 2
change_x, change_y = 0, 0
food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10

snake_body = [(snake_x, snake_y)]

clock = pygame.time.Clock()

def display_snake():
    global snake_x, snake_y
    global food_x, food_y
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    if (snake_x, snake_y) in snake_body[1:]:
        print("GAME OVER!!!!")
        pygame.quit()
        quit()

    snake_body.append((snake_x, snake_y))

    if food_x == snake_x and food_y == snake_y:
        food_x, food_y = random.randrange(0, width) // 10 * 10, random.randrange(0, height) // 10 * 10
    else:
        del snake_body[0]

    game_screen.fill((0, 0, 0))
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for (x, y) in snake_body:
        pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
    pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP:
                change_x = 0
                change_y = -10
            elif event.key == pygame.K_DOWN:
                change_x = 0
                change_y = 10
    
    display_snake()
    clock.tick(10)



'''import pygame
import random
import time

pygame.init()

width, height = 600, 600
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption ("VB snake Game")

snake_x, snake_y = width/2, height/2
change_x, change_y = 0,0 
food_x, food_y = random.randrange(0,width)//10*10,  random.randrange(0,height)//10*10

snake_body = [(snake_x, snake_y)]

clock = pygame.time.Clock()

def display_snake():
    global snake_x, snake_y
    global food_x, food_y
    snake_x = (snake_x + change_x)%width
    snake_y = (snake_y + change_y)%height

    if((snake_x, snake_y) in snake_body[1:]):
        print("GAME OVER!!!!")
        quit()

    snake_body.append((snake_x, snake_y))

    if(food_x == snake_x and food_y == snake_y):
        food_x, food_y = random.randrange(0,width)//10*10, random.ramdrange(0,height)//10*10
    else:
        del snake_body[0]

    game_screen.fill((0,0,0))
    pygame.draw.rect(game_screen, (0, 255, 0), [food_x, food_y, 10, 10])
    for (x,y) in snake_body:
        pygame.draw.rect(game_screen, (255, 255, 255), [x, y, 10, 10])
    pygame.display.update()

while True:
    events = pygame.event.get()
    for event in events:
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                change_x = -10
                change_y = 0
            elif(event.key == pygame.K_RIGHT):
                change_x = 10
                change_y = 0
            elif(event.key == pygame.K_UP):
                change_x = 0
                change_y = -10
            elif(event.key == pygame.K_DOWN):
                change_x = 0
                change_y = 10
            display_snake()
    if(not events):
        display_snake()
    clock.tick(10)




'''