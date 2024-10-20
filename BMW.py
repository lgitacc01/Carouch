import pygame
import random
import os
clock=pygame.time.Clock()
current_dir = os.path.dirname(os.path.abspath(__file__))
BMW_path = os.path.join(current_dir, 'picture', 'BMW.png')
x=300
y=0
v=40
rdc=0
rd=0
spam=0
dung=0


def BMW():
    bmw=pygame.image.load(BMW_path)
    return bmw

def BMW_rect(char):
    bmw_hcn=char.get_rect(center=(x,y))
    return bmw_hcn

def BMW_run():
    global y
    global dung
    global dem_diem
    
    if y<850:
        y+=v
    else: 
        dung=1
        y=0
    
   
    return y

def spam_BMW(BMW,diem,charx):
    listx=[420,300,540]
    global x
    global dung
    global y
    global spam
    if y<0:
        x=charx
    if int(diem)%5==0 and dung==0 and diem>5:
        BMW_run()
    else: x=charx
    if int(diem)%5!=0 and dung==1:
        dung =0

