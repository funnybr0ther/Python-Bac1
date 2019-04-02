import pygame

from parametters import *


class HitBox(pygame.sprite.Sprite):

    def __init__(self, rect, is_rect=True):
        super().__init__()
        self.rect = rect
        self.radius = (rect.x / 2) ** 2 + (rect.y / 2) ** 2  # (x/2) ^2 + (y/2) ^2
        self.is_rect = is_rect
        self.is_active = False
        self.spawned = False
        self.collision_listeners = []
        self.type = ENNEMY_TYPE

    def touched(self, other_hitbox, ratio=0.9):
        """
        Returns true if there is an intersection between the two objects
        :param other_hitbox:
        :return:
        """

        intersection = self.rect.clip(other_hitbox.rect)
        return intersection.width != 0 or intersection.height != 0
        # return
        #   pygame.sprite.collide_rect(self, other_hitbox) if self.is_rect else pygame.sprite.collide_circle(self,
        #                                                                                                   other_hitbox)

    def ontouch(self):
        if self.is_active:
            if VERBOSE:
                print("Object touched")

    def add_collision_listenr(self, collision_listener):
        self.collision_listeners.append(collision_listener)

    def hitbox_update(self):
        # Checks all the collisions
        for collision_listener in self.collision_listeners:
            if collision_listener.is_active:
                if self.touched(collision_listener):
                    self.ontouch()


class Character(HitBox):

    def __init__(self, screen, name="Paladin", is_forward=False, dimensions=CHARACTER_DIMENSIONS):
        self.screen = screen
        self.is_forward = is_forward
        self.image = pygame.image.load(
            IMAGE_RESOURCES + name.lower() + "_" + ("bw" if not is_forward else "fw") + ".png")
        self.image = pygame.transform.scale(self.image, dimensions)
        if not is_forward:
            self.image = pygame.transform.flip(self.image, True, False)
        self.name = name
        self.rect = self.image.get_rect()
        super().__init__(self.rect)
        self.screen_rect = screen.get_rect()

        # Start the character at the bottom center of the screen.
        self.rect.centerx = 0 + width
        self.rect.bottom = self.screen_rect.bottom - int(ground_width * 89 / 100)

        # Speed of the character
        self.speed = 6
        self.min_speed = self.speed
        self.center = float(self.speed)

        # Set a variable for each movement.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.is_attacking = False

        self.direction = [RIGHT, LEFT]  # if is_forward else [LEFT, RIGHT]
        self.orientation = self.direction[0]
        self.animation = pygame.image.load("/home/guillaume/Documents/python/Pygame/GameJam/resources/images/slash.png")
        self.rigid_bodies = []
        self.type = ENNEMY_TYPE


    def __str__(self):
        return str(self.name)

    def attack(self):
        animation_rect = self.animation.get_rect()
        animation_rect.bottom = self.rect.bottom

        animation_rect.centerx = self.rect.centerx

        if self.orientation == RIGHT:
            animation_rect.centerx += self.speed
        elif self.orientation == LEFT:
            animation_rect.centerx -= self.speed

        self.animation_rect = animation_rect

    def campled_movement(self, offset, isX=True):
        """
        Returns the closets version of the offest which doesn't collide with a wall
        :param offset:
        :param isX:
        :return:
        """
        sol = offset
        for i in range(0, abs(offset) + 1):
            ok_i = True
            for rigid_body in self.rigid_bodies:
                # Tries to predict a collision
                intersection = self.rect.move(sol if isX else 0, sol if not isX else 0).clip(rigid_body.rect)
                if intersection:
                    # If a wall collision was predicted
                    ok_i = False
                    break
            if ok_i:
                break
            else:
                sol += -1 if offset > 0 else 1
        return sol

    def update(self):
        if not self.is_active:
            return
        if self.rect.right <= self.screen_rect.right:
            if self.moving_right:
                self.orientation = self.direction[0]
                self.rect.centerx += self.campled_movement(self.speed, isX=True)

        if self.rect.left > 0:
            if self.moving_left:
                self.orientation = self.direction[1]
                self.rect.centerx += self.campled_movement(-self.speed, isX=True)

        if self.rect.top > 0:
            if self.moving_up:
                self.rect.bottom += self.campled_movement(-self.speed, isX=False)

        if self.rect.bottom <= self.screen_rect.bottom:
            if self.moving_down:
                self.rect.bottom += self.campled_movement(self.speed, isX=False)

        if self.is_attacking:
            self.attack()

        #if self.type == ENNEMY_TYPE:


        self.hitbox_update()

    def orient(self, image, rect, orientation=RIGHT):
        self.screen.blit(image if orientation == RIGHT else pygame.transform.flip(image, True, False), rect)

    def blitme(self):
        self.orient(self.image, self.rect, self.orientation)
        if self.is_attacking and self.animation is not None:
            self.orient(self.animation, self.animation_rect, self.orientation)


class RigidBody(Character):

    def __init__(self, screen, x, y, filename="ground", dimension=RIGID_BODY_DIMENSIONS):
        super().__init__(screen, filename, True, dimension)
        self.screen = screen

        self.rect.x = x
        self.rect.y = y - dimension[1]
        self.is_active = True
        self.type = RIGID_BODY

    def update(self):
        # Checks all the collisions
        for collision_listener in self.collision_listeners:
            if collision_listener.is_active:
                if self.touched(collision_listener):
                    self.ontouch()

class Spawn(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, orientation=RIGHT, mask=None, type=ENNEMY_TYPE):
        super().__init__()

        self.screen = screen
        self.x = x
        self.y = y
        self.mask = mask
        self.image = pygame.image.load("/home/guillaume/Documents/python/Pygame/GameJam/resources/images/spawn.png")
        self.rect = self.image.get_rect()
        self.type = type
        self.screen_rect = screen.get_rect()
        # Start the character at the bottom center of the screen.
        self.rect.centerx = 0 + width / 2
        self.rect.bottom = self.screen_rect.bottom - int(ground_width * 89 / 100)

    def spawn(self, item):
        """
        Spawn an item if it can be spawned
        :return:
        """
        if self.can_spawn(item):
            item.is_active = True
            item.rect.centerx = self.rect.centerx
            item.rect.centery = self.rect.centery
            item.spawned = True
            item.blitme()
            self.blitme()

    def can_spawn(self, item):
        """
        Tells if an item is allowed to spawn somewhere
        TODO : Use byte masks ( since they can be added etc... ) instead of constants
        :param item:
        :return:
        """
        return self.type == item.type

    def orient(self, image, rect, orientation=RIGHT):
        self.screen.blit(image, rect)

    def blitme(self):
        self.orient(self.image, self.rect, RIGHT)
