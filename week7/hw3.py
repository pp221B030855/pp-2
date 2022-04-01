import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False 
x = 300 
y = 400 
step = 20
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_w]: 
        if y>39: y-=step
    elif pressed[pygame.K_s]: 
        if y<561: y+=step
    elif pressed[pygame.K_a]: 
        if x>39: x-=step
    elif pressed[pygame.K_d]: 
        if x<761: x+=step

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)  
    pygame.display.flip()     
    clock.tick(60)     