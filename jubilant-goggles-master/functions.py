import pygame
import pygame.font as font
import random as r
import math, classes
import ressources
import os

def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0],
            pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

def testColide(player, enemies, blyat, e_blyat, win):
    for e in enemies:
        for b in blyat:
            if collide(e,b):
                e.hit()
                b.exist = False
                ressources.hitEnemyE.play()
        if collide(player, e):
            if isinstance(e, classes.Boss):
                player.hit(4)
            else:
                e.hp -= 3
                player.hit()

    for eb in e_blyat:
        if collide(player, eb):
            eb.exist = False
            player.hit()
            ressources.hitPlayerE.play()


def collide(e, b):
    #Process collisions
    self_x_min = e.x - e.width
    self_x_max = e.x
    self_y_min = e.y - e.height
    self_y_max = e.y

    other_x_min = b.x - b.width
    other_x_max = b.x
    other_y_min = b.y - b.height
    other_y_max = b.y

    cond_x_1 = self_x_min < other_x_max
    cond_x_2 = self_x_max > other_x_min
    cond_y_1 = self_y_max > other_y_min
    cond_y_2 = self_y_min < other_y_max

    return cond_x_1 and cond_x_2 and cond_y_1 and cond_y_2

def generateEnemy(w,h,enemies,target, type):
    #Create an "Enemy" or "Enemy "object that will chase the target.
    side = r.randint(0,3)
    if side == 0:
        x = -20
        y = r.randint(0,h)
    elif side == 1:
        x = w + 20
        y = r.randint(0,h)
    elif side == 2:
        y = -20
        x = r.randint(0,w)
    elif side == 3:
        y = h + 20
        x = r.randint(0,w)
    if type == 0:
        enemies.append(classes.Enemy(x,y,target))
    elif type == 1:
        enemies.append(classes.EnemyShooter(x,y,target))

def generateBoss(wave,w,h,target,win,enemies, gameManager):
    #Create a "Boss" object that will chase a target
    ressources.spawnBossE.play()
    side = r.randint(0,3)
    if side == 0:
        x = -20
        y = r.randint(0,h)
    elif side == 1:
        x = w + 20
        y = r.randint(0,h)
    elif side == 2:
        y = -20
        x = r.randint(0,w)
    elif side == 3:
        y = h + 20
        x = r.randint(0,w)
    gameManager.isWarning = True
    gameManager.counter_w = 0
    boss = classes.Boss(x,y,target,wave)
    enemies.append(boss)


def texts(txt,Xpos,Ypos,win,fontSize,w=0,h=0,milieu = False):
#Locate txt on pos in win with the asked font size
   Pol = font.Font(os.path.join("/home/guillaume/Documents/python/jubilant-goggles-master/Ressources","impact.ttf"),fontSize)
   scoretext = Pol.render(str(txt), 1,(0,0,0))
   text_width = scoretext.get_width()
   if milieu == True:
       win.blit(scoretext, ((w-text_width)//2, h*2//3))
   else: win.blit(scoretext, (Xpos, Ypos))
