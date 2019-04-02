import pygame
import math
import ressources
import functions as f
import random

#====================GameObject======================
class GameObjet:
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x,y,self.width, self.height)
        self.original_image = image.convert_alpha()
        self.image = self.original_image
        self.exist = True

    def lookAt(self,x,y):
        #Turn the object toward a point located in x,y
        deltaX = x - self.x
        deltaY = y - self.y
        self.angle = -math.atan2(deltaY, deltaX)
        self.angle_deg = (180 / math.pi) * self.angle

#===================Player===================
class Player(GameObjet):
    def __init__(self, x, y, w, h):
        super().__init__(x,y,40,40,ressources.playerI)
        self.fireRate = 0.1
        self.vel_x = 0
        self.vel_y = 0
        self.s_w = w
        self.s_h = h
        self.angle = 0
        self.angle_deg = 0
        self.vel_x_max = 7
        self.vel_y_max = 7
        self.hp = 10
        self.image = pygame.transform.scale(self.original_image,[self.width,self.height])
        self.invinsible = False
        self.timer_invinsible = 0

    def addForce(self, x, y):
        # ajoute de la force aux player et calcule si il peut avancer dans cette direction
        new_vel_x = self.vel_x + x
        new_vel_y = self.vel_y + y
        if new_vel_x < -self.vel_x_max:
            self.vel_x = -self.vel_x_max
        elif new_vel_x > self.vel_x_max:
            self.vel_x = self.vel_x_max
        else:
            self.vel_x = new_vel_x

        if new_vel_y < -self.vel_y_max:
            self.vel_y = -self.vel_y_max
        elif new_vel_y > self.vel_y_max:
            self.vel_y = self.vel_y_max
        else:
            self.vel_y = new_vel_y

    def decelerete_x(self):
        # freine en x
        self.vel_x = int(self.vel_x/1.1)

    def decelerete_y(self):
        # freine en y
        self.vel_y = int(self.vel_y/1.1)

    def shoot(self):
        # lance une bullet
        ressources.shootE.play()
        return Bullet(self.x, self.y
                ,self.angle, self.angle_deg)

    def dead(self):
        if self.hp <= 0:
            self.exist = False
            return True
        return False

    def hit(self, n=1):
        if not self.invinsible:
            self.invinsible = True
            self.hp -= n

    def draw(self, win):
        f.blitRotate(win, self.image, (self.x, self.y)
                        , (self.width/2, self.height/2), self.angle_deg)
        #pygame.draw.rect(win, (255,255,255), (self.x, self.y, 5,5))


    def update(self):
        keys = pygame.key.get_pressed()
        x = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
        y = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
        self.addForce(x, y)
        if not x:
            self.decelerete_x()
        if not y:
            self.decelerete_y()
        if self.invinsible:
            self.timer_invinsible += 1
            if self.timer_invinsible >= 30:
                self.invinsible = False
                self.timer_invinsible = 0

        self.x += self.vel_x
        self.y += self.vel_y
        if self.x < 20:
            self.x = 20
            self.vel_x *= -0.5
        elif self.x > self.s_w-20:
            self.x = self.s_w-20
            self.vel_x *= -0.5
        if self.y < 20:
            self.y = 20
            self.vel_y *= -0.5
        elif self.y > self.s_h-20:
            self.y = self.s_h-20
            self.vel_y *= -0.5
        if self.hp<=0:
            self.exist = False
        self.lookAt(*pygame.mouse.get_pos())

#====================Enemy======================================
class Enemy(GameObjet):
    def __init__(self, x, y, target):
        super().__init__(x,y,10,10,ressources.enemyI)
        self.target = target
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.angle = 0
        self.speed = 3
        self.hp = 3

    def update(self):
        #Update the positio & the angle of the object. Also check if the object is still alive
        self.lookAt(self.target.x,self.target.y)
        x = self.speed*math.cos(self.angle)
        y = -self.speed*math.sin(self.angle)
        self.x += x
        self.y += y
        if self.hp <= 0:
            self.exist = False
            ressources.enemyDieE.play()

    def draw(self, win):

        f.blitRotate(win, self.image, (self.x, self.y),
                (self.width/2, self.height/2), 0)

    def hit(self):
        self.hp -= 1


class EnemyShooter(Enemy):
    def __init__(self, x, y, target):
        super().__init__(x, y, target)
        self.image = ressources.enemyShooterI.convert_alpha()
        self.original_image = ressources.enemyShooterI.convert_alpha()
        self.hp = 2
        self.speed = 2
        self.bullets = []
        self.counter = 0

    def shoot(self):
        bull = EnemyBullet(self.x, self.y
                ,self.angle, self.angle_deg)
        self.bullets.append(bull)

    def update(self):
        super().update()
        to_remove = []
        self.counter += 1
        if self.counter == 80:
            self.shoot()
            self.counter = 0
        for b in self.bullets:
            b.update()
            if not b.exist:
                to_remove.append(b)

        for t in to_remove:
            self.bullets.remove(t)

    def draw(self, win):
        super().draw(win)
        for b in self.bullets:
            b.draw(win)

class Boss(EnemyShooter):
    def __init__(self,x, y, target,wave):
        super().__init__(x, y, target)
        self.image = ressources.bossI.convert_alpha()
        self.hp = wave*2
        self.start_hp = self.hp
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x += self.width/2
        self.y += self.height/2
        self.behavior = 0
        self.timer = 60
        self.fact = 0

    def octoShoot(self):
        # tir dans 8 direction
        fact = (math.pi/360) * random.randint(0,90)
        for i in range(8):
            bull = EnemyBullet(self.x - self.width/2, self.y-self.height/2
                    ,fact + i*math.pi/4, fact + i*45)
            self.bullets.append(bull)

    def draw(self, win):
        # dessine
        for b in self.bullets:
            b.draw(win)
        f.blitRotate(win, self.image, (self.x - self.width/2, self.y-self.height/2),
                (self.width/2, self.height/2), 0)

    def spine(self, i):
        # tir en cercle
        bull = EnemyBullet(self.x - self.width/2, self.y-self.height/2
                ,self.fact + i*math.pi/4, self.fact + i*45)
        self.bullets.append(bull)

    def update(self):
        #met a jour le position , les attaques, et les bullets.
        self.lookAt(self.target.x,self.target.y)
        x = self.speed*math.cos(self.angle)
        y = -self.speed*math.sin(self.angle)
        self.x += x
        self.y += y
        if self.hp <= 0:
            self.exist = False
            ressources.enemyDieE.play()

        if self.start_hp*2/3 >= self.hp and self.behavior < 1:
            self.timer = 20
            self.behavior = 1

        elif self.start_hp/2 >= self.hp and self.behavior < 2:
            self.timer = 30
            self.behavior = 2

        self.counter += 1
        if self.counter >= self.timer and self.behavior < 2:
            self.octoShoot()
            self.counter = 0

        if self.behavior == 2:
            if self.counter <= 20:
                self.spine(self.counter/2)
            if self.counter >= self.timer:
                self.counter = 0
                self.fact = (math.pi/360) * random.randint(0,90)

        to_remove = []
        for b in self.bullets:
            b.update()
            if not b.exist:
                to_remove.append(b)

#=================Bullet======================================================
class Bullet(GameObjet):
    def __init__(self, x, y, angle, deg):
        super().__init__(x,y,10,10, ressources.r_arrowI)
        self.speed = 15
        self.angle_deg = deg
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.vel_x = math.cos(-angle) * self.speed
        self.vel_y = math.sin(-angle) * self.speed

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self,win):
        f.blitRotate(win, self.image, (self.x, self.y),
                (self.width/2, self.height/2), self.angle_deg)


class EnemyBullet(Bullet):
    def __init__(self, x, y, angle, deg):
        super().__init__(x, y, angle, deg)
        self.image = ressources.pouceI.convert_alpha()
        self.speed = 12

    def draw(self, win):
        f.blitRotate(win, self.image, (self.x, self.y),
                (self.width/2, self.height/2), 0)

#=================Sort==================================================
class Sort:
    def __init__(self, cld):
        self.cooldown = cld
        self.wait = 0

class OMG(Sort):
    def __init__(self):
        super().__init__(2700)
        self.omgTime = 0

    def effet(self, player, win):
        if self.wait != 0:
            self.wait -= 1
        self.omgTime -= 1
        player.fireRate = 10
        if self.omgTime <= 0:
            player.fireRate = 0.1
        else: f.texts("OMG!",player.x-43,player.y-50,win,50)

class Circle(Sort):
    def __init__(self):
        super().__init__(1800)
        self.csize = 0

    def effet(self, enemies, win,w,h):
        if self.wait != 0:
            self.wait -= 1
        if self.csize != 0:
            self.csize+=30
            win.blit(pygame.transform.scale(ressources.r_circleI,(self.csize,self.csize)),(w/2-self.csize/2,h/2-self.csize/2))
            if self.csize >= 1200:
                self.csize = 0
                circle = False
            for e in enemies:
                if math.sqrt((w/2-e.x)**2+(h/2-e.y)**2) < self.csize/2:
                    e.hp -= 3

class ScaredSmiley(Sort):
    def __init__(self):
        super().__init__(600)
        self.scaredTime = 0

    def effet(self,target,win):
        if self.wait != 0:
            self.wait -= 1
        self.scaredTime -= 1
        for e in target:
            e.speed = 0
            if self.scaredTime <= 0:
                e.speed = 3
            else:
                win.blit(ressources.scared_smileyI,(e.x-50,e.y-50))

#=========GameManager=======================================================
class GameManager:
    def __init__(self):
        # Controller des timers
        self.isWarning = False
        self.counter_w = 0
        self.waveClear = False
        self.counter_wc = 0
