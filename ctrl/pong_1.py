import pygame

#-- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)  
YELLOW = (255,255,0)

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
done = False
clock = pygame.time.Clock()
ball_width = 20
padd_length = 15
padd_width = 60
padd_x = 0
padd_y = 50
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
score = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        padd_y = padd_y - 5
    if keys[pygame.K_DOWN]:
        padd_y = padd_y + 5
    x_val = x_val + x_direction
    y_val = y_val + y_direction
    if x_val == 620:
        x_direction = -1
    if y_val == 460:
        y_direction = -1
    if x_val == 0:
       x_val = 150
       y_val = 200
       x_direction = 1
       y_direction = 1
       score = score + 1
    if y_val == 0:
        y_direction = 1
    if x_val == 15 and y_val >= padd_y and y_val <= padd_y + 60:
        x_direction = 1
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
    pygame.draw.rect(screen, WHITE, (padd_x, padd_y, padd_length, padd_width))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()