import pygame


#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r'C:\Users\kudai\Desktop\piccc\car game_bg.png')
background = pygame.transform.scale(background, (400,600))

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'C:\Users\kudai\Desktop\piccc\car game_car1.png')
        self.image = pygame.transform.scale(self.image, (150, 50))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)







class coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r'C:\Users\kudai\Desktop\piccc\coin.png')
        self.image = pygame.transform.scale(self.image, (20,20))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
        


    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\kudai\Desktop\piccc\car game_car.png")
        self.image = pygame.transform.scale(self.image, (50, 150))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = coin()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(E1)

    

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    Coins = font_small.render(str(COIN), True, RED)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(Coins, (30,30))
 
    #Moves and Re-draws all Sprites
    

    if pygame.sprite.spritecollide(P1, coins, True):
        COIN += 1
        C1 = coin()
        coins.add(C1)
        all_sprites.add(C1)
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1,[C1]):
        COIN+=1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
            time.sleep(2)
            pygame.quit()
            sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)