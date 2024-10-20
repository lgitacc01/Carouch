import pygame
import random
x=0
y=900
v=3
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
    global v
    print (v)
    if y<= 800:
        y=y+v
        return y
    

def spam_ct():
    global x
    global y
    global v
    listx=[420,300,540]
    rd=random.choice(listx)
    if y>=800:
        x=rd
        y=0
        if v<30:
            v+=0.5
    return x

def respawn():
    global x
    global y
    global v
    listx=[420,300,540]
    rd=random.choice(listx)
    x= rd
    y=900
    v=3
