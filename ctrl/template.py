import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)  
YELLOW = (255,255,0)

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My window")
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
