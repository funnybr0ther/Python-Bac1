import pygame
import numpy
import random
pygame.init()
win = pygame.display.set_mode((700,700))
pygame.display.set_caption("Forces et accélérations")
radius = 10
x = 350; y=350; speed = 5
run = True
dots_number = 20
dots =  []

for i in range(dots_number):
    dots.append((random.randint(10,690),random.randint(10,690)))
while run:
    removed_dots = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(dots_number):
        if numpy.sqrt((dots[i][0]-x)**2 + (dots[i][1]-y)**2)<=radius:
            removed_dots.append(dots[i])
            dots.pop(i)
            dots.append((random.randint(10,690),random.randint(10,  690)))
            radius += 3
            print(radius)
    pygame.time.delay(50)
    x_mouse, y_mouse = pygame.mouse.get_pos()
    if x == x_mouse:
        print("Hé toi tg aussi")
    direction = ((x_mouse-x)/(numpy.sqrt((x_mouse-x)**2 + (y_mouse-y)**2)), (y_mouse-y)/(numpy.sqrt((x_mouse-x)**2 + (y_mouse-y)**2)))
    pygame.draw.circle(win,(0,0,0), (int(x),int(y)), radius)
    x += direction[0]*10
    y += direction[1]*10
    pygame.draw.circle(win,(0,255,0), (int(x),int(y)), radius)
    for i in removed_dots:
        pygame.draw.circle(win,(0,0,0),(int(i[0]),int(i[1])),10)       
    for i in dots:
        pygame.draw.circle(win,(255,255,255),(int(i[0]),int(i[1])),10)
    pygame.display.update()