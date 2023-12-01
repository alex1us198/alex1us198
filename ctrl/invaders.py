import pygame
import math
import random



BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)  
YELLOW = (255,255,0)

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
pygame.display.set_caption("invaders")
class Invader(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(0, 50)
        self.speed = speed
        
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = (size[0] - height)
        self.speed = 0
    def player_set_speed(val):
        while val.rect.x > 0 and val.rect.x < 460:
            val.rect.x = val.rect.x + val
    lives = 5

invader_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
number_of_invaders = 50
for x in range (number_of_invaders):
    my_invader = Invader(WHITE, 10, 10, 1)
    invader_group.add (my_invader)
    all_sprites_group.add (my_invader)
def update(self):
    self.rect.y = self.rect.y + self.speed


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.player_set_speed(-3)
            elif event.key == pygame.K_RIGHT:
                Player.player_set_speed(3)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player.player_set_speed(0)
    all_sprites_group.update() 
    player_hit_group = pygame.sprite.spritecollide(Player, invader_group, True) 
    for foo in player_hit_group:
        Player.lives = Player.lives - 1      
    screen.fill(BLACK)
    all_sprites_group.draw (screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
