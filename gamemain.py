#library
import pygame 
import char
import cetruck
import BMW
import os

#innit
pygame.init()
current_dir = os.path.dirname(os.path.abspath(__file__))
maintruck_path = os.path.join(current_dir, 'picture', 'maintruck.png')
background_path = os.path.join(current_dir, 'picture', 'background.png')
clock=pygame.time.Clock()
diem=0
font=pygame.font.Font(None, 36)
pygame.mixer.music.load(r'audio\y2mate.com - Minoru 187 Gaming Background Music HD.mp3')
pygame.mixer.music.play()
#screen
screen=pygame.display.set_mode((720,725))
sc_y=725
#game caption
pygame.display.set_caption('Carouch')

#game icon
icon=pygame.image.load(maintruck_path)
pygame.display.set_icon(icon)

#backgound game
bg=pygame.image.load(background_path)
bg=pygame.transform.scale_by(bg,(1,1.45))
bg_y=0
#diem
def hien_thi_diem():
    diem_text = font.render(str(int(diem)), True, (255, 255, 255))
    diem_hcn=diem_text.get_rect(center=(150,50))
    screen.blit(diem_text, diem_hcn) 

gameplay=True
#running
running=True
while running:
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
                 char.turn(event)
    if gameplay:
        #pygame.mixer.music.pause()
        pygame.mixer.music.play()  
        screen.blit(bg,(0,bg_y))
        bg_y=bg_y+0.10
        screen.blit(bg,(0,bg_y))
        screen.blit(bg,(0,bg_y-725))
        #main char
        mainc=char.char_n()
        maincr=char.char_rect(mainc)
        screen.blit(mainc,maincr)
        #cetruck
        ctx=cetruck.spam_ct()
        ct=cetruck.ceTruck()
        ctr=cetruck.ct_rect(ct)
        screen.blit(ct,ctr)
        cetruck.ctRun()
        #BMW
        bmw=BMW.BMW()
        bmwr=BMW.BMW_rect(bmw)
        screen.blit(bmw,bmwr)
        BMW.BMWRun()    
        BMW.spam_BMW(ctx)
        #vacham
        #print (char.x)
        if ((BMW.x==char.x and BMW.y>=char.y)or(cetruck.x==char.x and cetruck.y>=char.y) ):
            gameplay=False
            #running=False
                
        #reset bg
        if bg_y>=725:
            bg_y=0    
        clock.tick(50)
        diem+=0.01
        hien_thi_diem()
        
        pygame.display.update()
