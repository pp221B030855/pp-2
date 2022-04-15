import pygame
pygame.init() #initializes the Pygame
from pygame.locals import* #import all modules from Pygame
import random
import os
screen = pygame.display.set_mode((798,600))


#changing title of the game window
pygame.display.set_caption('Racing Beast')


#defining our gameloop function

def gameloop():

    #setting background image
    bg = pygame.image.load('car game_bg.png')
    
    
    # setting our player
    maincar = pygame.transform.scale(pygame.image.load(os.path.join('car game_car.png')),(50,150))
    maincar = pygame.transform.rotate(pygame.transform.scale(maincar, (50,100)),180)
    maincarX = 350
    maincarY = 495
    maincarX_change = 0
    maincarY_change = 0

    #other cars
    car1 = pygame.transform.scale(pygame.image.load(os.path.join('car game_car1.png')),(100,50))
    car1 = pygame.transform.rotate(pygame.transform.scale(car1, (100,50)),90)
    car1X = random.randint(178,490)
    car1Y = 100

    car2 = pygame.transform.scale(pygame.image.load(os.path.join('car game_car2.png')),(100,50))
    car2 = pygame.transform.rotate(pygame.transform.scale(car2, (100,50)),90)
    car2X = random.randint(178,490)
    car2Y = 100

    car3 = pygame.transform.scale(pygame.image.load(os.path.join('car game_car3.png')),(100,50))
    car3 = pygame.transform.rotate(pygame.transform.scale(car3, (100,50)),90)
    car3X = random.randint(178,490)
    car3Y = 100
    
    


   
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

                #checking if any key has been pressed
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 2
            
                if event.key == pygame.K_LEFT:
                    maincarX_change -= 2
                
                if event.key == pygame.K_UP:
                    maincarY_change -= 2
                    
                if event.key == pygame.K_DOWN:
                    maincarY_change += 2

                #checking if key has been lifted up
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0
            
                if event.key == pygame.K_LEFT:
                    maincarX_change = 0
                
                if event.key == pygame.K_UP:
                    maincarY_change = 0
                    
                if event.key == pygame.K_DOWN:
                    maincarY_change = 0            

        #setting boundary for our main car
        if maincarX < 178:
            maincarX = 178
        if maincarX > 490:
            maincarX = 490
        
        if maincarY < 0:
            maincarY = 0
        if maincarY > 495:
            maincarY = 495


        #CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE 
        screen.fill((0,0,0))

        #displaying the background image
        screen.blit(bg,(0,0))

        #displaying our main car
        screen.blit(maincar,(maincarX,maincarY))

        #displaing other cars
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))
        
        #updating the values
        maincarX += maincarX_change
        maincarY +=maincarY_change

        #movement of the enemies
        car1Y += 1
        car2Y += 1
        car3Y += 1


        #moving enemies infinitely
        if car1Y > 670:
            car1Y = -10
        if car2Y > 670:
            car2Y = -10
        if car3Y > 670:
            car3Y = -10



        pygame.display.update()


gameloop()