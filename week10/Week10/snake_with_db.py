from glob import glob
from os import scandir
from select import select
import pygame
from random import *
import psycopg2 

BLACK = (0, 0, 0) # our playground
LINE_COLOR = (50, 50, 50) # grid color
HEIGHT = 400 
WIDTH = 400

BLOCK_SIZE = 20 # blocks on grid

global result
result = []


class Point: #To get coordinates from object
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall: # Our wall
    def __init__(self, level):
        self.body = []
        f = open("levels\\level{}.txt".format(level), "r") #open txt files to get coordinates of walls
        for y in range(0, HEIGHT//BLOCK_SIZE + 1):
            for x in range(0, WIDTH//BLOCK_SIZE + 1):
                if f.read(1) == '#':
                    self.body.append(Point(x, y)) #create wall
    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)                    

class Food: # food
    def __init__(self, color):
        self.color = color
        self.location = Point(randint(3, 17), randint(3, 17))

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, self.color, rect)


class Snake: # Snake
    def __init__(self):
        self.body = [Point(randint(0, 20), randint(0, 20))]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1): # to move all body
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        # move head and its body
        self.body[0].x += self.dx 
        self.body[0].y += self.dy 
        #if we get out of playground to return again
        if self.body[0].x * BLOCK_SIZE > WIDTH: 
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (128, 255, 128), rect)

    def check_collision(self, food, wall): # checking collision
        global score
        for i in range(0, len(self.body)): #we check for full body to avoid apple on snake
            if self.body[i].x == food.location.x: 
                if self.body[i].y == food.location.y:
                    self.body.append(Point(food.location.x, food.location.y))
                    if food.color == (255, 0, 0):
                        score +=1
                    return True                
        for i in range(1, len(self.body)): #for snake 
            if self.body[0].x == self.body[i].x:
                if self.body[0].y == self.body[i].y:
                    return 2
        for i in range(0, len(wall.body)): #for walls
            if self.body[0].x == wall.body[i].x:
                if self.body[0].y == wall.body[i].y:
                    return 2  

    def check_collision1(self, food): # checking collision with special apple
        global score
        for i in range(0, len(self.body)): #we check for full body to avoid apple on snake
            if self.body[i].x == food.location.x: 
                if self.body[i].y == food.location.y:
                    self.body.append(Point(food.location.x, food.location.y))
                    if food.color == (0, 0, 255):
                        score +=2
                    return True                                      
                                   
def drawGrid(): #grid
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    snake = Snake()
    food = Food((255, 0, 0))
    food1 = Food((0, 0, 255))
    wall = Wall(1)
    dirs = {'W': True, 'S': True, 'A':True, 'D': True} #dictonary to avoid moving through body
    lvl = 1
    global score 
    score = 0
    fps = 7
    cur = 5
    font = pygame.font.SysFont('Verdana', 16, True) #font of score and level
    inc_speed = pygame.USEREVENT + 1
    pygame.time.set_timer(inc_speed, 5000) #disappearing apples
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == inc_speed: #event of disappearing apples
                food = Food((255, 0, 0))
                food1 = Food((0, 0, 255))    
            if event.type == pygame.KEYDOWN: #control motion of snake
                if event.key == pygame.K_RIGHT and dirs['D']:
                    snake.dx = 1
                    snake.dy = 0
                    dirs = {'W': True, 'S': True, 'A':False, 'D': True}
                if event.key == pygame.K_LEFT and dirs['A']:
                    snake.dx = -1
                    snake.dy = 0
                    dirs = {'W': True, 'S': True, 'A':True, 'D': False}
                if event.key == pygame.K_UP and dirs['W']:
                    snake.dx = 0
                    snake.dy = -1
                    dirs = {'W': True, 'S': False, 'A':True, 'D': True}
                if event.key == pygame.K_DOWN and dirs['S']:
                    snake.dx = 0
                    snake.dy = 1
                    dirs = {'W': False, 'S': True, 'A':True, 'D': True}

        if score > 15: #to avoid infinite level
            cur = 1000000000000


        snake.move()
        if snake.check_collision(food, wall) == 2:
            result.append(score)
            result.append(lvl)
            break
        if snake.check_collision(food, wall):   #if collision happened then new events                         
            #new levels
            food = Food((255, 0, 0))
            if score > cur and cur <= 15: #level up
                lvl+=1 
                fps+=3        
                cur += 5                

        if snake.check_collision1(food1):
            food1 = Food((0, 0, 255))
            if score > cur and cur <= 15: #level up
                lvl+=1 
                fps+=3        
                cur += 5 
                
        
        wall = Wall(lvl)                    

        SCREEN.fill(BLACK) 
        
        snake.draw()
        food.draw()
        food1.draw()
        wall.draw()
        render_score = font.render(f'SCORE: {score}', True, (255, 255, 255)) #current score on screen
        render_level = font.render(f'LEVEL: {lvl}', True, (255, 255, 255)) #current level on screen
        

        drawGrid() #grid
        #showing score and level
        SCREEN.blit(render_score, (290, 20))
        SCREEN.blit(render_level, (290, 0))
        pygame.display.update()
        CLOCK.tick(fps)


def check_name(name):
    cur.execute("SELECT name, score, level from SNAKE")
    row = cur.fetchall()
    for rows in row:
        if name == rows[0]:
            print(f'Hello, {name}. Your current score and level: {rows[1]}, {rows[2]}.')
            return False
    return True


def check_score(name):
    cur.execute("SELECT name, score, level from SNAKE")
    row = cur.fetchall()
    for rows in row:
        if name == rows[0]:
            if result[1] >= int(rows[2]) and result[0] > int(rows[1]):
                cur.execute(f"UPDATE SNAKE set score = {str(result[0])}, level = {str(result[1])} where name = '{name}'")
                con.commit()
                return True
    return False


global con, cur

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='12345678',
    host="localhost",
    port="5432"
)
print('You have successfully connected to the databases')

cur = con.cursor()
# CREATE TABLE
# cur.execute('''DROP TABLE "SNAKE SCORE"''')
# cur.execute('''CREATE TABLE snake
#     (NAME TEXT PRIMARY KEY NOT NULL,
#     SCORE TEXT NOT NULL,
#     LEVEL TEXT NOT NULL);'''
# )

name = input('Input your name: ')


if check_name(name):
    cur.execute(f'''INSERT INTO SNAKE (name, score, level) VALUES('{name}', 0, 0)''')
    con.commit()
    print('You are a new player! Your username is added to the databases.')
    

main()
con.commit()
if check_score(name):
    print(f'Congratulations! You have achieved a new result: {score}.')

con.commit()