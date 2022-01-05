import pygame

pygame.init()

def drawHitBox(obj,screen):
    rect = obj.hitbox
    pygame.draw.rect(screen, (255,0,0), rect, 2)

def checkHitBox(obj, hitboxes):
    for champ in hitboxes:
        if champ is not obj:
            if obj.hitbox.colliderect(champ.hitbox) == 1:
                return champ
            else:
                return True

def swap(obj, oobj):
    tempx = obj.x
    tempy = obj.y
    obj.x = oobj.x + 5
    obj.y = oobj.y
    oobj.x = tempx - 5
    oobj.y = tempy
    oobj.hitbox = pygame.Rect(oobj.x, oobj.y, oobj.img.get_width(), oobj.img.get_height())

def checkGrid(champ, grid):
    if not champ.selected:
            for square in grid:
                        if square.collidepoint(champ.hitbox.center):
                            champ.x = square.center[0] - champ.img.get_width()/2
                            champ.y = square.center[1] - champ.img.get_height()/2
                            champ.hitbox = pygame.Rect(champ.x, champ.y, champ.img.get_width(), champ.img.get_height())
