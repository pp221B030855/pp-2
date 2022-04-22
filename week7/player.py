import pygame
import os

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Music player')
pygame.init()

start_img = pygame.image.load('play.png').convert_alpha()
stop_img = pygame.image.load('stop.png').convert_alpha()
next_img = pygame.image.load('next.png').convert_alpha()
previous_img = pygame.image.load('previous.png').convert_alpha()

start_img = pygame.transform.scale(start_img, (50, 50))
stop_img = pygame.transform.scale(stop_img, (50, 50))
next_img = pygame.transform.scale(next_img, (50, 50))
previous_img = pygame.transform.scale(previous_img, (50, 50))

class Button():
    def __init__(self, x, y, image):
        self.image = image 
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y) 
        self.clicked = False

    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == 0:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0: 
            self.clicked = 0        

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

start_button = Button(260, 150, start_img)
stop_button = Button(175, 150, stop_img)
next_button = Button(350, 153, next_img)
previous_button = Button(80, 153, previous_img)
st = 0

ls = []
for file in os.listdir(os.getcwd() +'\\music'):
    ls.append(file)
    pygame.mixer.music.load('music\\' + ls[0])

clicked = 1
curr = 0
font_music = pygame.font.SysFont('Arial', 30, bold=True)

done = True
while done:
    render_music = font_music.render(ls[curr][:-4], True, (0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            clicked = 1        
    screen.fill((255, 255, 255))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and clicked == 1 or next_button.draw():
        curr+=1 
        if curr > len(ls)-1: curr = 0
        pygame.mixer.music.load('music\\' + ls[curr])
        pygame.mixer.music.play()
        clicked = 0
    if pressed[pygame.K_LEFT] and clicked == 1 or previous_button.draw():
        curr-=1
        if curr<0: curr = len(ls)-1
        pygame.mixer.music.load('music\\' + ls[curr])
        pygame.mixer.music.play()
        clicked = 0
    if start_button.draw():
        if st!= 0: pygame.mixer.music.unpause()
        else: 
            pygame.mixer.music.play(-1)
            st+=1    
    if stop_button.draw():
        pygame.mixer.music.pause()            
    screen.blit(render_music, (80, 70))
    pygame.display.update()