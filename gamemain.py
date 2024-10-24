#library
import pygame 
import char
import cetruck
import BMW
import menu
import os


#variable
diem_cu=0
ten_cu=''
RED=(255,0,0)
WHITE=(255,255,255)
xChar_cu=0
diem=0
#innit
pygame.init()
current_dir = os.path.dirname(os.path.abspath(__file__))
maintruck_path = os.path.join(current_dir, 'picture', 'maintruck.png')
background_path = os.path.join(current_dir, 'picture', 'background.png')
clock=pygame.time.Clock()
font=pygame.font.Font(None, 36)
pygame.mixer.music.load(r'audio\videogamemusic.mp3')
tong_xe=pygame.mixer.Sound(r'audio\tongxe.mp3')
pygame.mixer.music.play()
#screen
screen=pygame.display.set_mode((720,725))
sc_y=725
#game caption
pygame.display.set_caption('Carouch')
#font
font= pygame.font.Font('font\SuperMario256.ttf',36)
font_l= pygame.font.Font('font\SuperMario256.ttf',40)

#game icon
icon=pygame.image.load(maintruck_path)
pygame.display.set_icon(icon)

#backgound game
bg=pygame.image.load(background_path)
bg=pygame.transform.scale_by(bg,(1,1.45))
bg_y=0
#diem
def hien_thi_diem():
    diem_text = font.render(str(int(diem)), True, WHITE)
    diem_hcn=diem_text.get_rect(center=(170,50))
    screen.blit(diem_text, diem_hcn) 
#hien thi diem cu
def hien_thi_diem_cu(diem_cu):
    diem1_text = font.render(str(int(diem_cu)), True, WHITE)
    diem1_hcn=diem1_text.get_rect(center=(170,100))
    screen.blit(diem1_text, diem1_hcn) 
 #ten   
def hien_thi_ten(name):
    ten_text = font.render((name), True, WHITE)
    ten_hcn=ten_text.get_rect(center=(60,50))
    screen.blit(ten_text, ten_hcn) 
#ten cu
def hien_thi_ten_cu(old_name):
    ten_cu_text = font.render((old_name), True, WHITE)
    ten_cu_hcn=ten_cu_text.get_rect(center=(60,100))
    screen.blit(ten_cu_text, ten_cu_hcn) 

gameplay=False
#running
running=True
while running:
    
    #set up menu
    if gameplay==False:
        screen.blit(bg,(0,bg_y))
        bg_y=bg_y+0.10
        screen.blit(bg,(0,bg_y))
        screen.blit(bg,(0,bg_y-725))
        if bg_y>=725:
                bg_y=0
        mx,my=pygame.mouse.get_pos()        
        menu.Menu(screen,mx,my,font,font_l)
        pygame.display.update()
        check=menu.start_game()   
        if check:
            gameplay=True
    #key press
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                mcx,mcy=event.pos
                menu.read_mc(mcx,mcy)
        if event.type==pygame.KEYDOWN:
            xChar_cu=char.x
            char.turn(event)
            name=menu.read_name(event)
    if gameplay:
        screen.blit(bg,(0,bg_y))
        bg_y=bg_y+1
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
        BMW.spam_BMW(bmw,diem,char.x)
        screen.blit(bmw,bmwr)
        
        #vacham
        if ((BMW.x==char.x and BMW.y>=char.y)or(cetruck.x==char.x and cetruck.y>=char.y) ):
            gameplay=False
            if diem_cu<diem:
                diem_cu=diem
                ten_cu=name
            diem=0
            cetruck.respawn()
            BMW.y=0
            pygame.mixer.music.pause()
            tong_xe.play()
            pygame.time.delay(2300)
            pygame.mixer.music.play()
                
        #reset bg
        if bg_y>=725:
            bg_y=0    
        clock.tick(50)
        diem+=0.01
        hien_thi_diem()
        hien_thi_ten(name)
        if diem_cu>0:
            hien_thi_diem_cu(diem_cu)
            hien_thi_ten_cu(ten_cu)
        pygame.display.update()
