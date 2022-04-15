import pygame
import pygame.gfxdraw
#Initializing pygame module
pygame.init()

#Screen variables
screen_width = 700
screen_height =500

# Defining Colors
white = (255, 255, 255)
blue = (67,238,250)
red = (255, 0, 0)
black = (0, 0, 0)
green = (38,245,45)
pink = (255,192,203)
orange = (255,165,0)
yellow = (255,255,0)
violet = (177, 3, 252)
 
#Setting default color to black
pencolour = black


drawingwindow =  pygame.display.set_mode((700,500))
pygame.display.set_caption("Paint")
drawingwindow.fill((255,255,255))

#Loading backgroud image and drawing it on screen
backimg = pygame.image.load("paint.png")
drawingwindow.blit(backimg, (0,0))

#rect for the drawing area
clearrect = (0,0, 1200, 800)

#Defining rect value for colors in colorbox
col1= (22, 81, 30, 34)
col2= (56, 81, 34, 34)
col3= (22, 120, 30, 33)
col4= (56, 120, 34, 32)
col5= (22, 156, 30, 33)
col6= (56, 156, 34, 32)
col7= (22, 192, 30, 33)
col8= (56, 192, 34, 32)

#Rect that highlight which button is selected
buttonselect = (22, 81, 30, 34)

#Function to draw color box
def drawrectangle():    
    pygame.gfxdraw.box(drawingwindow, col1, black)
    pygame.gfxdraw.box(drawingwindow, col2, blue)
    pygame.gfxdraw.box(drawingwindow, col3, red)
    pygame.gfxdraw.box(drawingwindow, col4, green)
    pygame.gfxdraw.box(drawingwindow, col5, pink)
    pygame.gfxdraw.box(drawingwindow, col6, orange)
    pygame.gfxdraw.box(drawingwindow, col7, yellow)
    pygame.gfxdraw.box(drawingwindow, col8, violet)
drawrectangle()

#Set mouse cursor for pencil (default)
pygame.mouse.set_cursor(*pygame.cursors.broken_x)
exit_game = False

#Gameloop
while not exit_game:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
    
                        
        #Check for button clicks
        t = pygame.mouse.get_pressed()
        if t[0] == 1:     
            mousepos = pygame.mouse.get_pos()
            if 122 < mousepos[0] < 678 and 21 < mousepos[1] < 480:
                pygame.gfxdraw.filled_ellipse(drawingwindow,mousepos[0], mousepos[1],4,4,pencolour)
                
            elif 22 < mousepos[0] < 52 and 81 < mousepos[1] < 115:
                pencolour = black
                drawrectangle()         
                buttonselect = (22, 81, 30, 34)
                
            elif 56 < mousepos[0] < 90 and 81 < mousepos[1] < 115:
                pencolour = blue
                drawrectangle()
                buttonselect = (56, 81, 34, 34)
                
            elif 22 < mousepos[0] < 52 and 120 < mousepos[1] < 153:
                pencolour = red
                drawrectangle()
                buttonselect = (22, 120, 30, 33)
                
            elif 56 < mousepos[0] < 90 and 120 < mousepos[1] < 152:
                pencolour = green
                drawrectangle()
                buttonselect = (56, 120, 34, 32)
                
            elif 22 < mousepos[0] < 52 and 156 < mousepos[1] < 189:
                pencolour = pink
                drawrectangle()
                buttonselect = (22, 156, 30, 33)
                
            elif 56 < mousepos[0] < 90 and 156 < mousepos[1] < 188:
                pencolour = orange
                drawrectangle()
                buttonselect = (56, 156, 34, 32)
                
            elif 22 < mousepos[0] < 52 and 192 < mousepos[1] < 225:
                pencolour = yellow
                drawrectangle()
                buttonselect = (22, 192, 30, 33)
                
            elif 56 < mousepos[0] < 90 and 192 < mousepos[1] < 224:
                pencolour = violet
                drawrectangle()
                buttonselect = (56, 192, 34, 32)
            #Eraser
            elif 13 < mousepos[0] < 54 and 247 < mousepos[1] < 285:
                pencolour = white
                drawrectangle()
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            #Pencil
            elif 59 < mousepos[0] < 97 and 247 < mousepos[1] < 288:
                pencolour = black
                drawrectangle()
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)
                buttonselect = (22, 81, 30, 34)
                
            elif 15 < mousepos[0] < 96 and 363 < mousepos[1] < 400:                
                pygame.gfxdraw.box(drawingwindow, clearrect, white)

        pygame.gfxdraw.rectangle(drawingwindow, buttonselect, white)
        pygame.display.update()
                
            
pygame.quit()
                    