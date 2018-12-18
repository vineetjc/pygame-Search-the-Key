import pygame
import sys
import random

from math import sqrt
from pygame.locals import *

pygame.init()
pygame.mixer.init()

#setup the window display
size=(1024, 768)
width=size[0]
height=size[1]
windowSurface = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('Find the key!')

# set up fonts
basicFont = pygame.font.SysFont("symbola", 30)

#set colors R,G,B code
BLACK = (0, 0, 0)
ORANGE = (255,140,0)
GREEN = (0,225,0)
GOLD = (255,223,0)
WHITE = (255,255,255)
LIMEGREEN = (50,205,50)
LIGHTBLUE = (180,216,231)
LIGHTYELLOW = (250,250,204)
LIGHTRED = (255,153,153)

instructionSet = ["1. There exists a 5x5 grid, one of which holds the key",
                  "2. You have 6 tries to find the key",
                  "3. As you go closer to the key, the temperature increases",
                  "   and as you go away from the key, it decreases",
                  "4. If you find the key in the selected nubmer of turns, you win, else you lose"]

#Start Button
startRect = pygame.Rect((392,509,240,50))
#Instruction Button
howtoRect = pygame.Rect((392,584,240,50))
#Back Button
backRect = pygame.Rect((392,584,240,50))
#decrement number of turns
decTurnsRect = pygame.Rect((360,390,60,60))
#increment number of turns
incTurnsRect = pygame.Rect((604,390,60,60))
#number of turns
numTurnsRect = pygame.Rect((442,390,142,60))
#number of turns left
numTurnsLeftRect = pygame.Rect((230,600,140,50))

#Function for rendering text
def text_objects(text, font):
  textSurface = font.render(text, True, BLACK)
  return textSurface, textSurface.get_rect()

#Find key in selected number of turns
def search_key():

    #Co-ordinates for tracking mouse movement
    x = y = 0

    STARTGOLDKEY=pygame.image.load('./Images/goldkey.png')
    KEYPIC=pygame.image.load('Images/THE KEY.png')
    BG=pygame.image.load('Images/jail2.png')
    therm=pygame.image.load('Images/thermoLightBlu.png')

    rects=[0 for i in range(25)] #list for boxes in the game
    blacklist=[] #stores numbers of the boxes clicked (already)
    key_idx=random.randint(1,25) #randomize box with key
    turncount=0 #to check turn count
    maxturns = 6 #default number of turns allowed
    haswon=False #to check if successfully selected the key
    buttonWidth=240
    buttonHeight=50
    buttonLeft=width/2-(buttonWidth/2)
    buttonRight=width/2+(buttonWidth/2)

    done=False #loop variable

    howto = False #Instruction Menu
    start = False #Game Started

    #Initialise fonts
    pygame.font.init()

    clickedbox=0 #to set default value

    #Initial Event
    event = pygame.event.poll()

    while event.type != pygame.QUIT:

        windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0))

        event = pygame.event.poll()

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

        if start == False and howto == False:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if howtoRect.collidepoint(event.pos):
                    howto = True

                elif startRect.collidepoint(event.pos):
                    start = True
                    break

                elif incTurnsRect.collidepoint(event.pos):
                    if maxturns<8:
                        maxturns=maxturns+1

                elif decTurnsRect.collidepoint(event.pos):
                    if maxturns>4:
                        maxturns=maxturns-1

            title = pygame.font.SysFont("symbola",100)
            textSurf1, textRect1 = text_objects("Find The Key!", title)
            textRect1.center = ( (width/2), (height/2) - 100)

            findkey = pygame.font.SysFont("liberationserif",20)
            textSurf2, textRect2 = text_objects("LET'S FIND THE KEY!", findkey)
            textRect2.center = ( (width/2), (height/2) + 150)

            howtotext = pygame.font.SysFont("liberationserif",20)
            textSurf3, textRect3 = text_objects("HOW-TO-PLAY", howtotext)
            textRect3.center = ( (width/2), (height/2) + 225)

            decTurnText = pygame.font.SysFont("liberationserif",40)
            textSurf4, textRect4 = text_objects("-", decTurnText)
            textRect4.center = ( 390, 420)

            incTurnText = pygame.font.SysFont("liberationserif",40)
            textSurf5, textRect5 = text_objects("+", incTurnText)
            textRect5.center = ( 634, 420)

            numTurnText = pygame.font.SysFont("liberationserif",30)
            textSurf6, textRect6 = text_objects(str(maxturns) + " turns", numTurnText)
            textRect6.center = ( 512, 420)

            windowSurface.blit(pygame.transform.scale(KEYPIC,(200,100)),(412,70))

            if x>=buttonLeft and x<=buttonRight and y>=height/2+125 and y<=height/2+125+buttonHeight:
                pygame.draw.rect(windowSurface, GOLD, startRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, startRect)


            if x>=buttonLeft and x<=buttonRight and y>=height/2+200 and y<=height/2+200+buttonHeight:
                pygame.draw.rect(windowSurface, GOLD, howtoRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, howtoRect)

            if x>=360 and x<=420 and y>=390 and y<=450:
                pygame.draw.rect(windowSurface, GOLD, decTurnsRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, decTurnsRect)

            if x>=604 and x<=664 and y>=390 and y<=450:
                pygame.draw.rect(windowSurface, GOLD, incTurnsRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, incTurnsRect)


            pygame.draw.rect(windowSurface, WHITE, numTurnsRect)

            windowSurface.blit(textSurf1, textRect1)
            windowSurface.blit(textSurf2, textRect2)
            windowSurface.blit(textSurf3, textRect3)
            windowSurface.blit(textSurf4, textRect4)
            windowSurface.blit(textSurf5, textRect5)
            windowSurface.blit(textSurf6, textRect6)


        elif howto == True:
            startmenu = pygame.font.SysFont("liberationserif",20)
            textSurf7, textRect7 = text_objects("BACK TO START MENU", startmenu)
            textRect7.center = ( (width/2), (height/2) + 150)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                xpress, ypress = event.pos
                if backRect.collidepoint(event.pos):
                    howto = 0

            instructions = pygame.font.SysFont("symbola",50)
            textSurf7, textRect7 = text_objects("Instructions", instructions)
            textRect7.center = ( (width/2), (height/2) - 200)

            lenInstructions = len(instructionSet)

            instFont = []
            instSurfRect = []

            for i in range(lenInstructions):
                instFont.append(pygame.font.SysFont("liberationserif",20))
                instSurfRect.append(text_objects(instructionSet[i], instFont[i]))
                instSurfRect[i][1].center = ( (width/2), (height/2) - 100 + i * 50)

            backtext = pygame.font.SysFont("liberationserif",20)
            textSurf8, textRect8 = text_objects("BACK TO MENU", backtext)
            textRect8.center = ( (width/2), (height/2) + 225)

            if x>=buttonLeft and x<=buttonRight and y>=height/2+200 and y<=height/2+200+buttonHeight:
                pygame.draw.rect(windowSurface, GOLD, backRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, backRect)

            windowSurface.blit(textSurf7, textRect7)
            windowSurface.blit(textSurf8, textRect8)

            for i in range(lenInstructions):
                windowSurface.blit(instSurfRect[i][0],instSurfRect[i][1])

        pygame.display.flip()

    while not done and start == True:
        right=50
        down=50
        horizontal=100
        vertical=100
        turnsleft = maxturns-turncount

        for event in pygame.event.get():

            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type==MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos

                for rec in rects:
                    #print(rec," ",pos)
                    if rec.collidepoint(pos):
                        distance=sqrt((rec.center[0]-rects[key_idx-1].center[0])**2 + (rec.center[1]-rects[key_idx-1].center[1])**2)
                        # distance to hot/cold
                        if distance<=100:
                            therm=pygame.image.load('Images/thermo+12Red.png')
                        if 100<distance<=142:
                            therm=pygame.image.load('Images/thermo+11VermRed.png')
                        if 142<distance<=200:
                            therm=pygame.image.load('Images/thermo+10Vermillion.png')
                        if 200<distance<=224:
                            therm=pygame.image.load('Images/thermo+9DOrange.png')
                        if 224<distance<=283:
                            therm=pygame.image.load('Images/thermo+8Orange.png')
                        if 283<distance<=300:
                            therm=pygame.image.load('Images/thermo+7Orangyish.png')
                        if 300<distance<=317:
                            therm=pygame.image.load('Images/thermo+6Yellow.png')
                        if 317<distance<=361:
                            therm=pygame.image.load('Images/thermo+5Yellow.png')
                        if 361<distance<=400:
                            therm=pygame.image.load('Images/thermo+4Yellow.png')
                        if 400<distance<=413:
                            therm=pygame.image.load('Images/thermo+3Yellow.png')
                        if 413<distance<=425:
                            therm=pygame.image.load('Images/thermo+2Yellow.png')
                        if 425<distance<=448:
                            therm=pygame.image.load('Images/thermo+1PaleYellow.png')
                        if 448<distance<=500:
                            therm=pygame.image.load('Images/thermoPaleYellow.png')
                        if 500<distance<=566:
                            therm=pygame.image.load('Images/thermoLightBlu.png')

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
                        pygame.mixer.music.load('./sounds/win.mp3')
                        pygame.mixer.music.play(0)
                        haswon=True
                    else:
                        text=basicFont.render(str(clickedbox),True,ORANGE,BLACK)
                    textbox=text.get_rect(center=(clicked.centerx,clicked.centery))
                    windowSurface.blit(text,textbox)
                    pygame.display.flip()
                    pygame.time.delay(500)
                    clickedbox=0 #reset value
                    if turncount==maxturns:
                        if haswon:
                            continue
                        else:
                            if not haswon:
                                #'you are out of turns!'
                                done=True
                                numTurnsLeft = pygame.font.SysFont("liberationserif",30)
                                textSurf9, textRect9 = text_objects("GAME OVER", numTurnsLeft)
                                pygame.draw.rect(windowSurface, LIGHTRED, numTurnsLeftRect)
                                textRect9.center = (300, 625)
                                windowSurface.blit(textSurf9, textRect9)
                                pygame.mixer.music.load('./sounds/lose.mp3')
                                pygame.mixer.music.play(0)
                                pygame.display.flip()
                                pygame.time.delay(1500)
                                show_end_screen()

        windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0))

        if turnsleft<=8 and turnsleft>5:
            numTurnsLeft = pygame.font.SysFont("liberationserif",30)
            textSurf9, textRect9 = text_objects(str(turnsleft) + " turns left", numTurnsLeft)
            textRect9.center = (300, 625)
            pygame.draw.rect(windowSurface, LIMEGREEN, numTurnsLeftRect)

        elif turnsleft<=5 and turnsleft>3:
            numTurnsLeft = pygame.font.SysFont("liberationserif",30)
            textSurf9, textRect9 = text_objects(str(turnsleft) + " turns left", numTurnsLeft)
            textRect9.center = (300, 625)
            pygame.draw.rect(windowSurface, LIGHTBLUE, numTurnsLeftRect)

        if turnsleft<=3 and turnsleft>1:
            numTurnsLeft = pygame.font.SysFont("liberationserif",30)
            textSurf9, textRect9 = text_objects(str(turnsleft) + " turns left", numTurnsLeft)
            textRect9.center = (300, 625)
            pygame.draw.rect(windowSurface, LIGHTYELLOW, numTurnsLeftRect)
          
        elif turnsleft==1:
            textSurf9, textRect9 = text_objects(str(turnsleft) + " turn left", numTurnsLeft)
            textRect9.center = (300, 625)
            pygame.draw.rect(windowSurface, LIGHTYELLOW, numTurnsLeftRect)

        windowSurface.blit(textSurf9, textRect9)
        
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
            done=True
            numTurnsLeft = pygame.font.SysFont("liberationserif",30)
            textSurf9, textRect9 = text_objects("YOU WIN", numTurnsLeft)
            pygame.draw.rect(windowSurface, LIMEGREEN, numTurnsLeftRect)
            textRect9.center = (300, 625)
            windowSurface.blit(textSurf9, textRect9)
            pygame.display.flip()
            pygame.time.delay(1000)
            show_end_screen()

        pygame.display.flip()

def show_end_screen():
    BG=pygame.image.load('Images/jail background.jpg')
    x= y =0 #to track mouse movement
    buttonWidth=240
    buttonHeight=50
    buttonLeft=width/2-(buttonWidth/2)
    buttonRight=width/2+(buttonWidth/2)
    #Retart Button
    restartRect = pygame.Rect((392,509,240,50))
    #Quit Button
    quitRect = pygame.Rect((392,584,240,50))
    event=pygame.event.poll()
    restart=False #Restart option

    while event.type != pygame.QUIT:

        windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0))

        event = pygame.event.poll()

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

        playagaintext = pygame.font.SysFont("liberationserif",20)
        textSurf1, textRect1 = text_objects("PLAY AGAIN", playagaintext)
        textRect1.center = ( (width/2), (height/2) + 150)

        quittext = pygame.font.SysFont("liberationserif",20)
        textSurf2, textRect2 = text_objects("QUIT", quittext)
        textRect2.center = ( (width/2), (height/2) + 225)

        if x>=buttonLeft and x<=buttonRight and y>=height/2+125 and y<=height/2+125+buttonHeight:
            pygame.draw.rect(windowSurface, GOLD, restartRect)

        else:
            pygame.draw.rect(windowSurface, GREEN, restartRect)

        if x>=buttonLeft and x<=buttonRight and y>=height/2+200 and y<=height/2+200+buttonHeight:
            pygame.draw.rect(windowSurface, GOLD, quitRect)

        else:
            pygame.draw.rect(windowSurface, GREEN, quitRect)


        windowSurface.blit(textSurf1, textRect1)
        windowSurface.blit(textSurf2, textRect2)
        pygame.display.flip()

        if restart == False:
             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restartRect.collidepoint(event.pos):
                    restart = True

                elif quitRect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        if restart == True:
            search_key()



if __name__=='__main__':
    search_key()
