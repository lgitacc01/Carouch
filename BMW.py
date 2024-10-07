import pygame
import random
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
BMW_path = os.path.join(current_dir, 'picture', 'BMW.png')
x=420
y=800
v=20
rdc=0


def BMW():
    bmw=pygame.image.load(BMW_path)
    return bmw

def BMW_rect(char):
    bmw_hcn=char.get_rect(center=(x,y))
    return bmw_hcn

def BMWRun():
    global y
    if y<800:
     y=y+v
     return y

def spam_BMW(ctx):
    listx=[420,300,540]
    global x
    global y
    global rdc
    rd=420
    
    while ctx==rd :
        rd=random.choice(listx)
    

    if y>=800 :
        x=rd
        y=0
    return x
