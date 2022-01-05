import pygame

pygame.init()

class unit:
    def __init__(self, img, atk, hp, x, y, new_x, locked = False, selected = False):
        self.img = img
        self.atk = atk
        self.hp = hp
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, self.img.get_width(), self.img.get_height())
        self.new_x = new_x
        self.locked = locked
        self.selected = selected
        

    