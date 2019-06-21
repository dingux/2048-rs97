import pygame
from time import *
from pygame.locals import *
from random import *


#just some init stuff
pygame.init()
pygame.mouse.set_visible(False)

new_game = True

exit = False
up = False
down = False
left = False
right = False

tiles_on_screen = 0

score = 0

real_screen = pygame.display.set_mode((200, 240),0,16)

square_row_1 = [0,0,0,0]
square_row_2 = [0,0,0,0]
square_row_3 = [0,0,0,0]
square_row_4 = [0,0,0,0]


# okay so the square_coords is kinda weird the way i set it up
# basically, the format is this, square_coords_rownum_rectargumentnum
# ex: square1's coords are (square_coords_1[0], square_coords_1_2[0], square_coords_1_3[0], square_coords_1_4[0])

square_coords_1   = [0,50,100,150]
square_coords_1_2 = [0,0,0,0]
square_coords_1_3 = [48,48,48,48]
square_coords_1_4 = [48,48,48,48]

square_coords_2   = [0,50,100,150]
square_coords_2_2 = [50,50,50,50]
square_coords_2_3 = [48,48,48,48]
square_coords_2_4 = [48,48,48,48]

square_coords_3   = [0,50,100,150]
square_coords_3_2 = [100,100,100,100]
square_coords_3_3 = [48,48,48,48]
square_coords_3_4 = [48,48,48,48]

square_coords_4   = [0,50,100,150]
square_coords_4_2 = [150,150,150,150]
square_coords_4_3 = [48,48,48,48]
square_coords_4_4 = [48,48,48,48]

see_keys = True

pygame.font.init()

font = pygame.font.SysFont('Arial', 20)

gray_color = (220,220,220)

yellow_color = (255,255,224)

real_screen.fill((255,255,255))

pygame.display.update()

#one of the not fun parts

def logic():
    global up
    global down
    global left
    global right
    global score
    x = 0
    while up == True:
        while x < 4:
            if square_row_1[x] == square_row_2[x] and square_row_1[x] > 0:
                square_row_1[x] = square_row_1[x] * 2
                square_row_2[x] = 0
            if square_row_1[x] == square_row_3[x] and square_row_1[x] > 0 and square_row_2[x] < 1:
                square_row_1[x] = square_row_1[x] * 2
                square_row_3[x] = 0
            if square_row_1[x] == square_row_4[x] and square_row_1[x] > 0 and square_row_2[x] < 1 and square_row_3[x] < 1:
                square_row_1[x] = square_row_1[x] * 2
                square_row_4[x] = 0
            if square_row_2[x] == square_row_3[x] and square_row_2[x] > 0:
                square_row_2[x] = square_row_2[x] * 2
                square_row_3[x] = 0
            if square_row_2[x] == square_row_4[x] and square_row_2[x] > 0 and square_row_3[x] < 1:
                square_row_2[x] = square_row_2[x] * 2
                square_row_4[x] = 0
            if square_row_3[x] == square_row_4[x] and square_row_3[x] > 0:
                square_row_3[x] = square_row_3[x] * 2
                square_row_4[x] = 0
            if square_row_2[x] > 0 and square_row_1[x] == 0:
                square_row_1[x] = square_row_2[x]
                square_row_2[x] = 0
            if square_row_3[x] > 0 and square_row_2[x] == 0 and square_row_1[x] == 0:
                square_row_1[x] = square_row_3[x]
                square_row_3[x] = 0
            if square_row_3[x] > 0 and square_row_2[x] == 0 and square_row_1[x] > 0:
                square_row_2[x] = square_row_3[x]
                square_row_3[x] = 0
            if square_row_4[x] > 0 and square_row_3[x] == 0 and square_row_2[x] == 0 and square_row_1[x] == 0:
                square_row_1[x] = square_row_4[x]
                square_row_4[x] = 0
            if square_row_4[x] > 0 and square_row_3[x] == 0 and square_row_2[x] == 0 and square_row_1[x] > 0:
                square_row_2[x] = square_row_4[x]
                square_row_4[x] = 0
            if square_row_4[x] > 0 and square_row_3[x] == 0 and square_row_2[x] > 0 and square_row_1[x] > 0:
                square_row_3[x] = square_row_4[x]
                square_row_4[x] = 0
            x = x + 1
        
        break
    if down == True:
        pass
    if right == True:
        pass
    if left == True: 
        pass
    text = font.render("Score: " + str(score), False, (0,0,0))
    real_screen.blit(text,(0,210))
    

def draw_squares():
    x = 0
    x2 = x
    tiles_on_screen = 0
    while x < 16:
        if x < 4:
            if square_row_1[x] > 0:
                pygame.draw.rect(real_screen, yellow_color,( square_coords_1[x],square_coords_1_2[x],square_coords_1_3[x],square_coords_1_4[x]))
                text = font.render(str(square_row_1[x]), False, (0,0,0))
                real_screen.blit(text,(square_coords_1[x],square_coords_1_2[x]))
                tiles_on_screen = tiles_on_screen + 1
        if x < 8 and x > 3:
            x2 = x - 4
            if square_row_2[x2] != 0:
                pygame.draw.rect(real_screen, yellow_color,( square_coords_2[x2],square_coords_2_2[x2],square_coords_2_3[x2],square_coords_2_4[x2]))
                text = font.render(str(square_row_2[x2]), False, (0,0,0))
                real_screen.blit(text,(square_coords_2[x2],square_coords_2_2[x2]))
                tiles_on_screen = tiles_on_screen + 1
        if x < 12 and x > 7:
            x2 = x - 8
            if square_row_3[x2] != 0:
                pygame.draw.rect(real_screen, yellow_color, (square_coords_3[x2],square_coords_3_2[x2],square_coords_3_3[x2],square_coords_3_4[x2]))
                text = font.render(str(square_row_3[x2]), False, (0,0,0))
                real_screen.blit(text,(square_coords_3[x2],square_coords_3_2[x2]))
                tiles_on_screen = tiles_on_screen + 1
        if x < 16 and x > 11:
            x2 = x - 12
            if square_row_4[x2] != 0:
                pygame.draw.rect(real_screen, yellow_color, (square_coords_4[x2],square_coords_4_2[x2],square_coords_4_3[x2],square_coords_4_4[x2]))
                text = font.render(str(square_row_4[x2]), False, (0,0,0))
                real_screen.blit(text,(square_coords_4[x2],square_coords_4_2[x2]))
                tiles_on_screen = tiles_on_screen + 1
        x = x + 1
def game():
    global tiles_on_screen
    pygame.draw.rect(real_screen, gray_color, (0,0,200,200))
    draw_squares()
    global new_game
    if new_game == True:
        new_game = False
        if square_row_1[0] == 0 and square_row_1[1] == 0 and square_row_1[2] == 0 and square_row_1[3] == 0 and square_row_2[0] == 0 and square_row_2[1] == 0 and square_row_2[2] == 0 and square_row_2[3] == 0 and square_row_3[0] == 0 and square_row_3[1] == 0 and square_row_3[2] == 0 and square_row_3[3] == 0 and square_row_4[0] == 0 and square_row_4[1] == 0 and square_row_4[2] == 0 and square_row_4[3] == 0:
            tmp = randint(0,16)
            tmp2 = randint(0,4)
            if tmp < 4:
                if tmp2 == 4:
                    square_row_1[tmp] = 4
                else:
                    square_row_1[tmp] = 2
            if tmp < 8 and tmp > 3:
                if tmp2 == 4:
                    square_row_2[tmp - 4] = 4
                else:
                    square_row_2[tmp - 4] = 2
            if tmp < 12 and tmp > 7:
                if tmp2 == 4:
                    square_row_3[tmp - 8] = 4
                else:
                    square_row_3[tmp - 8] = 2
            if tmp < 16 and tmp > 11:
                if tmp2 == 4:
                    square_row_2[tmp - 12] = 4
                else:
                    square_row_2[tmp - 12] = 2
            tmp_2 = randint(0,16)
            tmp2_2 = randint(0,4)
            if tmp == tmp_2:
                tmp_2 = randint(0,16)
                if tmp == tmp_2:
                    tmp_2 = randint(0,16)
                    if tmp == tmp_2:
                        tmp_2 = randint(0,16)
            tmp = tmp_2
            tmp2 = tmp2_2
            if tmp < 4:
                if tmp2 == 4:
                    square_row_1[tmp] = 4
                else:
                    square_row_1[tmp] = 2
            if tmp < 8 and tmp > 3:
                if tmp2 == 4:
                    square_row_2[tmp - 4] = 4
                else:
                    square_row_2[tmp - 4] = 2
            if tmp < 12 and tmp > 7:
                if tmp2 == 4:
                    square_row_3[tmp - 8] = 4
                else:
                    square_row_3[tmp - 8] = 2
            if tmp < 16 and tmp > 11:
                if tmp2 == 4:
                    square_row_2[tmp - 12] = 4
                else:
                    square_row_2[tmp - 12] = 2
    logic()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if see_keys == True:
            print(event)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_END:
                exit = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_END:
                exit = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

    game()
    pygame.display.update()
    if exit == True:
        pygame.quit()
        quit()
