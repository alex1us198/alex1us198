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
pygame.display.set_caption("Snow")
class Snow(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,600)
        self.rect.y = random.randrange(0,400)
snow_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
number_of_flakes = 50
for x in range (number_of_flakes):
    my_snow = Snow(WHITE, 5, 5)
    snow_group.add (my_snow)
    all_sprites_group.add (my_snow)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(BLACK)
    all_sprites_group.draw (screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
