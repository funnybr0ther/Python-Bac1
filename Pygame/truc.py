import pygame
from random import randint
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Bilibu")
width = 40
height = 60
x = 0
y = 500-height
c_width = 20
velocity = 2
run = True
isJump = False
jumpCount = 10
get = True
score = 0
while run:
    print(get)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not(get):
        print("now:" +" "+ str(a) +" "+ str(b) +" "+ str(x) +" "+ str(y))
        if x<=a<=x+width and y<=b<=y+height:
            score += 1
            print(score)
            get = True
    else:
        a = randint(0,500-c_width-30)
        b = randint(300,500-c_width-30)
        get = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_LEFT]:
        x-= velocity
        if x<0 or x>500-width:
            x+= velocity
    if keys[pygame.K_RIGHT]:
        x+= velocity
        if x<0 or x>500-width:
            x-= velocity
    if keys[pygame.K_SPACE]:
        if height == 30:
            height = 60
            y -= 30
        else:
            pass

    if not(isJump):
        if keys[pygame.K_DOWN]:
            height = 30
            y+=30
        if keys[pygame.K_UP]:
            isJump = True
    else:
        if jumpCount >= -25:
            y -= (jumpCount * abs(jumpCount)) * 0.04
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 25
    if y>500-height:
        y=500-height
    if x>500-width:
        x = 500-width
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.draw.rect(win,(0,255,255),(a,b,c_width,c_width))
    pygame.display.update()
pygame.quit()
print(str(a) +  " " +str(b))