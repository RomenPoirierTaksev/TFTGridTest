import pygame
from unit import unit
from helpers import *

pygame.init()


screen_size = [1200,680]
screen = pygame.display.set_mode(screen_size)

running = True

square_size = 80

moved = False

upper_grid = []
lower_grid = []

unit1 = unit(pygame.image.load("ship.png"), 5, 5, 100, 100, 100)
unit2 = unit(pygame.image.load("ufo.png"), 5, 5, 200, 100, 200)

units = [unit1, unit2]

def champs(x,y, img):
    screen.blit(img, (x,y))


while running:

    mouse_pos = pygame.mouse.get_pos()
    mouse_state = pygame.mouse.get_pressed(3)[0]

    for champ in units:
        screen.fill((0,0,0))
        
        if champ.hitbox.collidepoint(mouse_pos[0], mouse_pos[1]) and mouse_state:
            champ.selected = True
            
            hitbox_check_result = checkHitBox(champ, units)
            if hitbox_check_result == True:
                champs(mouse_pos[0] - champ.img.get_width()/2, mouse_pos[1] - champ.img.get_height()/2, champ.img)
                champ.x = mouse_pos[0] - champ.img.get_width()/2
                champ.y = mouse_pos[1] - champ.img.get_height()/2
                champ.hitbox = pygame.Rect(mouse_pos[0] - champ.img.get_width()/2, mouse_pos[1] - champ.img.get_height()/2, champ.img.get_width(), champ.img.get_height())
                drawHitBox(champ, screen)
            else:
                swap(champ, hitbox_check_result)
                champ.hitbox = pygame.Rect(champ.x, champ.y, champ.img.get_width(), champ.img.get_height())
                champs(champ.x, champ.y, champ.img)
                drawHitBox(champ, screen)
        
        if not mouse_state:
            champ.selected = False

        center = champ.y + champ.img.get_height()/2
        #print(center)
        if center  >= 320 and center <= 480:
            checkGrid(champ, upper_grid)
            #print("yo")
        elif center >= 560:
            checkGrid(champ, lower_grid)
            #print("hey")

        for i in range(int(screen_size[0]/square_size)):
            for j in range(int(screen_size[1]/square_size)):
                if j >= 4 and j != 6:
                    if j > 6:
                        lower_grid.append(pygame.draw.rect(screen, (255,0,0), pygame.Rect(square_size * i, square_size * j, square_size, square_size), 1))
                    else:
                        upper_grid.append(pygame.draw.rect(screen, (255,0,0), pygame.Rect(square_size * i, square_size * j, square_size, square_size), 1))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for champ in units:
        drawHitBox(champ, screen)
        champs(champ.x, champ.y, champ.img)

    pygame.display.update()

