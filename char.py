import pygame
x=420
y=700
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
char_path = os.path.join(current_dir, 'picture', 'maincharacter.png')

def char_n():
    char=pygame.image.load(char_path)
    return char

def char_rect(char):
    char_hcn=char.get_rect(center=(x,y))
    return char_hcn

def rCharX():
    return x


def turn (event):
    global x
    if event.key== pygame.K_RIGHT:
        if x<540:
            x=x+120
           
    if event.key== pygame.K_LEFT:
        if x>300:
            x=x-120
            


 