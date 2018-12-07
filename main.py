import pygame, sys, random
from math import sqrt
from pygame.locals import *

pygame.init()

#setup the window display
size=(1024, 768)
windowSurface = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('Find the key!')

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

#set colors R,G,B code
BLACK = (0, 0, 0)
ORANGE = (255,140,0)

#Find key in 6 turns
def SEARCH():
    KEYPIC=pygame.image.load('Images/THE KEY.jpg')
    BG=pygame.image.load('Images/jail background.jpg')
    therm=pygame.image.load('Images/thermoLightBlu.jpg')

    rects=[0 for i in range(25)] #list for boxes in the game
    blacklist=[] #stores numbers of the boxes clicked (already)
    key_idx=random.randint(1,25) #randomize box with key
    turncount=0 #to check turn count
    haswon=False #to check if successfully selected the key

    done=False #loop variable
 # turn=int(input("ENTER THE NUMBER OF TURNS"))

    clickedbox=0 #to set default value
    while not done:
        right=50
        down=50
        horizontal=100
        vertical=100
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                for rec in rects:
                    if rec.collidepoint(pos):
                        distance=sqrt((rec.center[0]-rects[key_idx-1].center[0])**2 + (rec.center[1]-rects[key_idx-1].center[1])**2)
                        # distance to hot/cold
                        if distance<=100:
                            therm=pygame.image.load('Images/thermo+12Red.jpg')
                        if 100<distance<=142:
                            therm=pygame.image.load('Images/thermo+11VermRed.jpg')
                        if 142<distance<=200:
                            therm=pygame.image.load('Images/thermo+10Vermillion.jpg')
                        if 200<distance<=224:
                            therm=pygame.image.load('Images/thermo+9DOrange.jpg')
                        if 224<distance<=283:
                            therm=pygame.image.load('Images/thermo+8Orange.jpg')
                        if 283<distance<=300:
                            therm=pygame.image.load('Images/thermo+7Orangyish.jpg')
                        if 300<distance<=317:
                            therm=pygame.image.load('Images/thermo+6Yellow.jpg')
                        if 317<distance<=361:
                            therm=pygame.image.load('Images/thermo+5Yellow.jpg')
                        if 361<distance<=400:
                            therm=pygame.image.load('Images/thermo+4Yellow.jpg')
                        if 400<distance<=413:
                            therm=pygame.image.load('Images/thermo+3Yellow.jpg')
                        if 413<distance<=425:
                            therm=pygame.image.load('Images/thermo+2Yellow.jpg')
                        if 425<distance<=448:
                            therm=pygame.image.load('Images/thermo+1PaleYellow.jpg')
                        if 448<distance<=500:
                            therm=pygame.image.load('Images/thermoPaleYellow.jpg')
                        if 500<distance<=566:
                            therm=pygame.image.load('Images/thermoLightBlu.jpg')

                        windowSurface.blit(therm,therm.get_rect(center=(8*size[0]/10,size[1]/2)))
                        clicked=rec
                        clickedbox=rects.index(rec)+1
                        if clickedbox not in blacklist:
                            blacklist.append(clickedbox)
                        else:
                            #'clicked already'
                            clickedbox=-1
                            break
                        turncount+=1
                        break

                if clickedbox==0: #i.e. clicked outside the boxes
                    break
                if clickedbox==-1:
                    #'this is clicked already'
                    pass
                else:
                    #black rectangle background
                    blackrect=pygame.draw.rect(windowSurface,BLACK,(clicked.left,clicked.top,clicked.width,clicked.height))
                    if clickedbox==key_idx:
                        text=basicFont.render('BING!',True,ORANGE,BLACK)
                        haswon=True
                    else:
                        text=basicFont.render(str(clickedbox),True,ORANGE,BLACK)
                    textbox=text.get_rect(center=(clicked.centerx,clicked.centery))
                    windowSurface.blit(text,textbox)
                    pygame.display.flip()
                    pygame.time.delay(500)
                    clickedbox=0 #reset value
                    if turncount==6:
                        if haswon:
                            continue
                        else:
                            if not haswon:
                                #'you are out of turns!'
                                done=True
                                text=basicFont.render('GAME OVER', True, BLACK)
                                textbox=text.get_rect(center=(700,100))
                                windowSurface.blit(text,textbox)
                                pygame.display.flip()
                                pygame.time.delay(1500)

        windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0))
        for i in range(25):
            if i+1 in blacklist:
                if i+1==key_idx:
                    black_rec=pygame.draw.rect(windowSurface, BLACK, (right,down,horizontal,vertical),2)
                    picture=KEYPIC
                    box=picture.get_rect(center=(rects[i].centerx,rects[i].centery))
                    windowSurface.blit(pygame.transform.scale(picture, (100,100)), (right,down,horizontal,vertical))
                else:
                    black_rec=pygame.draw.rect(windowSurface, BLACK, (right,down,horizontal,vertical))
            else:
                black_rec=pygame.draw.rect(windowSurface, BLACK, (right,down,horizontal,vertical),2)
            rects[i]=black_rec
            right+=100
            if right==(50+100*(6-1)):
                down+=100
                right=50
        windowSurface.blit(therm,therm.get_rect(center=(8*size[0]/10,size[1]/2)))
        if haswon:
            pygame.time.delay(500)
            #'you win!'
            done=1
            text=basicFont.render('YOU WIN!', True, BLACK)
            textbox=text.get_rect(center=(700,100))
            windowSurface.blit(text,textbox)
            pygame.display.flip()
            pygame.time.delay(1000)
        pygame.display.flip()

if __name__=='__main__':
    SEARCH()
