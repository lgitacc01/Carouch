import pygame
import random
x=420
y=800
v=7
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
ceTruck_path = os.path.join(current_dir, 'picture', 'cetruck.png')
def ceTruck():
    ct=pygame.image.load(ceTruck_path)
    return ct

def ct_rect(char):
    ct_hcn=char.get_rect(center=(x,y))
    return ct_hcn

def ctRun():    
    global y
    if y<= 800:
        y=y+v
        return y

def spam_ct():
    global x
    global y
    listx=[420,300,540]
    rd=random.choice(listx)
    if y>=800:
        x=rd
        y=0
    return x
