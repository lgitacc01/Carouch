import pygame 
mcx_m,mcy_m=0,0
name_player=''
i=0
DARK_GRAY=(50,50,50)
DARK_BLUE = (0, 0, 128)
YELLOW = (255, 255, 0)
WHITE =(255,255,255)
Rect_menu=(100,150,520,400)
Rect_name=(280,250,200,50)
Rect_start=(280,310,200,50)
Rect_record=(280,370,200,50)

def Menu(screen,mx,my,font,font_l):
    pygame.draw.rect(screen,DARK_BLUE,Rect_menu,0,1)
    pygame.draw.rect(screen,WHITE,Rect_menu,5,5)
    pygame.draw.rect(screen,WHITE,Rect_name,3,5)
    pygame.draw.rect(screen,WHITE,Rect_start,3,5)
    #print(mx,my)
    if name_player =='':
        text_start=font.render('NAME',True,DARK_GRAY)
        screen.blit(text_start,(315,260))
    else:
        text_start=font.render(name_player,True,YELLOW)
        screen.blit(text_start,(315,260))
        

    text_start=font.render('START',True,WHITE)
    screen.blit(text_start,(315,320))
    if((280 < mx < 480) and (310 < my < 360)):
        pygame.draw.rect(screen,DARK_BLUE,Rect_start,0,5)
        pygame.draw.rect(screen,WHITE,Rect_start,3,5)
        text_start=font_l.render('START',True,WHITE)
        screen.blit(text_start,(315,320))
    


def read_name(event):
    global name_player
    global i
    if event.type == pygame.KEYDOWN :
        if event.key== pygame.K_BACKSPACE:
            if ((280<mcx_m<480) and (250<mcy_m<300)):
                if i>0:
                    i=i-1
                    name_player=name_player[0:-1]
                    
        else:
            if ((280<mcx_m<480) and (250<mcy_m<300)):
                 if event.key != pygame.K_SPACE:
                    if i<5:
                        i=i+1
                        name_player+= event.unicode.lower()
                       
    return name_player
        
                
def start_game():
    global name_player
    global mcx_m
    global mcy_m
    if name_player !='':
        if 280<mcx_m<480 and 310<mcy_m<360:
           mcx_m=0
           mcy_m=0
           return True
            



def read_mc(mcx,mcy):
    global mcx_m
    global mcy_m 
    mcx_m=mcx
    mcy_m=mcy