import pygame
from time import *
from pygame.locals import *

#just some init stuff
pygame.init()
pygame.mouse.set_visible(False)

real_screen = pygame.display.set_mode((200, 200),0,16)

square_row_1 = [0, 0, 0, 0]
square_row_2 = [0, 0, 0, 0]
square_row_3 = [0, 0, 0, 0]
square_row_4 = [0, 0, 0, 0]

square_coords_1 = []
square_coords_2 = []
square_coords_3 = []
square_coords_4 = []
square_coords_1_2 = []
square_coords_2_2 = []
square_coords_3_2 = []
square_coords_4_2 = []
square_coords_1_3 = []
square_coords_2_3 = []
square_coords_3_3 = []
square_coords_4_3 = []
square_coords_1_4 = []
square_coords_2_4 = []
square_coords_3_4 = []
square_coords_4_4 = []

debug_on = True

pygame.font.init()

font = pygame.font.SysFont('Arial', 10)

gray_color = (220,220,220)

yellow_color = (255,255,224)

real_screen.fill((255,255,255))

pygame.display.update()

#one of the not fun parts

def draw_squares():
    x = 0
    while x < 16:
        if x < 4:
            pygame.draw.rect(real_screen, yellow_color, square_coords_1[x],square_coords_1_2[x],square_coords_1_3[x],square_coords_1_4[x])
        if x < 8:
            pygame.draw.rect(real_screen, yellow_color, square_coords_2[x],square_coords_2_2[x],square_coords_2_3[x],square_coords_2_4[x])
        if x < 12:
            pygame.draw.rect(real_screen, yellow_color, square_coords_3[x],square_coords_3_2[x],square_coords_3_3[x],square_coords_3_4[x])
        if x < 16:
            pygame.draw.rect(real_screen, yellow_color, square_coords_4[x],square_coords_4_2[x],square_coords_4_3[x],square_coords_4_4[x])
        else:
            print("error")
    
    
    
def game():
    pygame.draw.rect(real_screen, gray_color, (0,0,200,200))
    draw_squares()




while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if debug_on == True:
            print(event)
    game()
    pygame.display.update()
    
