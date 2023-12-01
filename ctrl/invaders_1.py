import pygame
import random
import math

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)  
YELLOW = (255,255,0)
CYAN = (0,255,255)
RED = (255,0,0)

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Invaders")
done = False
clock = pygame.time.Clock()
score = 0
lives = 5
frame = 0
flag = False

class Invader(pygame.sprite.Sprite):
    def __init__(self, color, height, width, speed):
        super().__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
        self.speed = speed

    def override(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 480:
            self.rect.y = 0

class Player(pygame.sprite.Sprite):
    bulletCount = 50

    def __init__(self, color, height, width, speed):
        super().__init__()
        self.image = pygame.surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
        self.speed = speed
    
    def override(self, x, y):
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 480:
            self.rect.y = 0

class bullet(pygame.sprite.Sprite):
    width = 2
    height = 2
    speed = 2
    def __init__(self,color, x, y):
        super().__init__()
        self.color = color
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.rect.y += self.speed

invaderGroup = pygame.sprite.Group()
allSpritesGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()

fontType = pygame.font.SysFont("Impact", 25)
scoreSurface = fontType.render("Score: " + str(score), True, (255,255,255))
scoreRect = scoreSurface.get_rect(midleft = (25,30))
livesSurface = fontType.render("Lives: " + str(lives), True, (255,255,255))
livesRect = livesSurface.get_rect(midleft = (25,30))
bulletLeftSurface = fontType.render("Bullets Remaining: 50", True, (255,255,255))
bulletLeftRect = bulletLeftSurface.get_rect(midleft = (25,30))

totalFlakes = 10

player = Player((255,255,0), 5, 5, 1)
player.override(320,400)
allSpritesGroup.add(player)
for i in range(totalFlakes):
    myInvader = Invader(BLUE, 5, 5, 1)
    invaderGroup.add(myInvader)
    allSpritesGroup.add(myInvader)

while not(done):
    scoreSurface = fontType.render("score: " + str(score), True, (255,255,255))
    livesSurface = fontType.render("Lives: " + str(lives), True, (255,255,255))
    bulletLeftSurface = fontType.render("Bullets remaining: " + str(player.bulletCount), True, (255,255,255))
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    invaderGroup.update()
    bulletGroup.update()
    allSpritesGroup.draw(screen)
    screen.blit(scoreSurface, scoreRect)
    screen.blit(livesSurface, livesRect)
    screen.blit(bulletLeftSurface, bulletLeftRect)
    playerHitGroup = pygame.sprite.spritecollide(player, invaderGroup, False)

    for i in bulletGroup:
        bulletHitGroup = pygame.sprite.spritecollide(i, invaderGroup, True)
        if i.rect.y == 0:
            bulletGroup.remove(i)
            allSpritesGroup.remove(i)
            del i
            player.bulletCount += 1
        if bulletGroup:
            score += 10
    if playerHitGroup:
        flag = True
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.rect.x -= 5
        if player.rect.x < 0:
            player.rect.x = 640
    elif keys[pygame.K_d]:
        player.rect.x += 5
        if player.rect.x == 640:
            player.rect.x = 0
    else:
        pass

    if keys[pygame.K_SPACE]:
        if player.bulletCount > 0:
            player.bulletCount -= 1
            bulletAdd = bullet(RED, player.rect.x, player.rect.y)
            bulletGroup.add(bulletAdd)
            allSpritesGroup.add(bulletAdd)
    
    pygame.display.flip()
    clock.tick(60)
    frame += 1
    if frame == 60:
        frame = 0
        if flag:
            flag = False
            lives -= -1
pygame.quit()

