import pygame


BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)  
YELLOW = (255,255,0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)

pygame.init()

size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maps")
done = False
clock = pygame.time.Clock()
score = 0
lives = 0
frame = 0
flag = False

tileMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

    ]

class tile(pygame.sprite.Sprite):
    def __init__(self, color, width, height, xref, yref):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = xref
        self.rect.y = yref

class player(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        if pygame.sprite.spritecollide(self, wallList, False):
            self.rect.x -= dx
            self.rect.y -= dy

allSpritesGroup = pygame.sprite.Group()
wallList = pygame.sprite.Group()

player1 = player(50, 50)
for i in range(10):
    for j in range(10):
        if tileMap[j][i] == 1:
            myWall = tile(BLUE, 20, 20, i*20, j*20)
            wallList.add(myWall)
            allSpritesGroup.add(myWall)
    
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(BLACK)
    allSpritesGroup.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
