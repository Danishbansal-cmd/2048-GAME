import pygame
import random
import time

pygame.init()
width,height = 500,500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption('try3')
clock = pygame.time.Clock()

#variables
NUM_FONT = pygame.font.SysFont("comicsans",30)
WHITE = (255,255,255)

#colors
GREY = (128,128,128)
L_RED = (255,102,102) #2
ORANGE = (255,128,0) #4
YELLOW = (200,255,0) #8
D_GREEN = (102,204,0) #16
GREEN = (0,255,0) #32
L_GBLUE = (0,255,128) #64
BLUE = (0,255,255) #128
M_BLUE = (0,128,255) #256
D_BLUE = (0,0,255) #512
VIOLET = (127,0,255) #1024
BLACK = (0,0,0) #2048
D_PINK = (255,0,127) #4096
RED = (255,0,0) #8192
D_RED = (153,0,0)# 16384
PINK = (255,0,255)# 32768


class Box:
    def __init__(self,row ,col,width,number):
        self.row = row
        self.col = col
        self.x = col * width
        self.y = row * width
        self.width = width
        self.color = GREY
        self.number = number
        self.text = NUM_FONT.render(str(self.number),1,WHITE)
        self.rect = pygame.Rect(self.x + 1,self.y + 1,self.width - 1,self.width -1 )

    def drawbox(self,win):

        pygame.draw.rect(win,self.color,self.rect)
        win.blit(self.text,(self.rect.x + 50 - self.text.get_width()/2,self.rect.y + 50 - self.text.get_height()/2))
    def get_number(self):
        for x in range(1,16):
            y = 2**x
            if self.number == y:
                return self.number
    def get_pos(self):
        return self.row,self.col
    def set_number(self,num):
        self.number = num
        self.text = NUM_FONT.render(str(self.number), 1, WHITE)
        if self.number == 2:
            self.color = L_RED  #2
        elif self.number == 4:
            self.color = ORANGE  #4
        elif self.number == 8:
            self.color = YELLOW  #8
        elif self.number == 16:
            self.color = D_GREEN  #16
        elif self.number == 32:
            self.color = GREEN  #32
        elif self.number == 64:
            self.color = L_GBLUE #64
        elif self.number == 128:
            self.color = BLUE #128
        elif self.number == 256:
            self.color = M_BLUE  #256
        elif self.number == 512:
            self.color = D_BLUE  #512
        elif self.number == 1024:
            self.color = VIOLET  #1024
        elif self.number == 2048:
            self.color = BLACK  #2048
        elif self.number == 4096:
            self.color = D_PINK  #4096
        elif self.number == 8192:
            self.color = RED  #8192
        elif self.number == 16384:
            self.color = D_RED # 16384
        elif self.number == 32768:
            self.color = PINK # 32768
        else:
            self.color = GREY #normal number
    def get_color(self):
        return self.color
    def get_number(self):
        return self.number
    def check(self):
        if self.row <= 0:
            self.row = 0
        if self.row >= 3:
            self.row = 3
        if self.col <= 0:
            self.col = 0
        if self.col >= 3:
            self.col = 3
    def __lt__(self,other):
        return False
#VARIABLES
WHITE = (255,255,255)
list = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]





def drawwin(win,grid):
    for x in grid:
        for y in x:
            y.drawbox(win)

    draw_grid(win)


def make_grid(rows,width):
    grid = []
    for x in range(rows):
        grid.append([])
        for y in range(rows):
            box = Box(x,y,width,0)
            grid[x].append(box)

    return grid

def draw_grid(win):
    for x in range(0,401,100):
        pygame.draw.aaline(win,(0,0,0),(x,0),(x,400))
    for x in range(0,401,100):
        pygame.draw.aaline(win,(0,0,0),(0,x),(400,x))


def random_box(list,grid):
    r = round(random.random() * 100)
    number = 0
    if r < 80:
        number = 2
    else:
        number = 4
    x = random.choice(list)
    grid[x[0]][x[1]].set_number(number)


def press_fun1(p,grid):
    value = False
    for i in range(p[0],p[1],p[2]):
        for j in range(p[0],p[1],p[2]):
            if grid[i][j].get_color() != (128, 128, 128) and j != p[3]:
                for x in range(j + p[4], p[5], p[2]):
                    if grid[i][x].get_color() != (128, 128, 128):
                        if grid[i][j].get_color() == grid[i][x].get_color():
                            print(f'i,j:{i},{j};i,x:{i},{x}')
                            a = grid[i][j].get_number() + grid[i][x].get_number()
                            grid[i][j].set_number(a)
                            grid[i][x].set_number(0)
                            value = True
                            break
                        else:
                            break
    for k in range(3):
        for i in range(p[6],p[7]):
            for j in range(p[8],p[9]):
                if grid[i][j].get_color() != (128, 128, 128):
                    if grid[i][j - p[10]].get_color() == (128, 128, 128):
                        a = grid[i][j].get_number()
                        grid[i][j - p[10]].set_number(a)
                        grid[i][j].set_number(0)
                        value = True
    c_list = []
    for x in grid:
        for y in x:
            if y.get_color() == (128, 128, 128):
                a1, a2 = y.get_pos()
                c_list.append([a1, a2])
    print(value)
    if value:
        random_box(c_list, grid)


def press_fun2(p,grid):
    value = False
    for j in range(p[0], p[1], -p[11]):
        for i in range(p[0], p[1], -p[11]):
            if grid[i][j].get_color() != (128, 128, 128) and i != p[2]:
                for x in range(i + p[3], p[4], -p[11]):
                    if grid[x][j].get_color() != (128, 128, 128):
                        if grid[i][j].get_color() == grid[x][j].get_color():
                            print(f'i,j:{i},{j};x,j:{x},{j}')
                            a = grid[i][j].get_number() + grid[x][j].get_number()
                            grid[i][j].set_number(a)
                            grid[x][j].set_number(0)
                            value = True
                            break
                        else:
                            break
    for k in range(3):
        for i in range(p[5],p[6]):
            for j in range(p[7],p[8]):
                if grid[i][j].get_color() != (128, 128, 128):
                    if grid[i - p[9]][j - p[10]].get_color() == (128, 128, 128):
                        a = grid[i][j].get_number()
                        grid[i - p[9]][j - p[10]].set_number(a)
                        grid[i][j].set_number(0)
                        value = True
    c_list = []
    for x in grid:
        for y in x:
            if y.get_color() == (128, 128, 128):
                a1, a2 = y.get_pos()
                c_list.append([a1, a2])
    print(value)
    if value:
        random_box(c_list, grid)


def main():
    ROWS = 4
    width = 100
    grid = make_grid(ROWS,width)

    list = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0],
            [3, 1], [3, 2], [3, 3]]

    random_box(list,grid)
    random_box(list,grid)


    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    left = [0,4,1,3,1,4,0,4,1,4,1]
                    press_fun1(left,grid)
                if event.key == pygame.K_RIGHT:
                    right = [3,-1,-1,0,-1,-1,0,4,0,3,-1]
                    press_fun1(right,grid)
                if event.key == pygame.K_UP:
                    up = [0,4,3,1,4,1,4,0,4,1,0,-1]
                    press_fun2(up,grid)
                if event.key == pygame.K_DOWN:
                    down = [3,-1,0,-1,-1,0,3,0,4,-1,0,1]
                    press_fun2(down,grid)
        win.fill(WHITE)
        drawwin(win,grid)
        pygame.display.update()
    pygame.quit()

main()