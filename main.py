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
pygame.mixer.music.load('./sounds/BackgroundMusic.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

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
                  "2. As you go closer to the key, the temperature increases",
                  "   and as you go away from the key, it decreases",
                  "3. You can vary the allowed number of turns between 4 and 8",
                  "4. You can choose any grid length between 4 to 6",
                  "5. If you find the key in the selected number of turns, you win!"]

#Start Button
startRect = pygame.Rect((392,509,240,50))
#Instruction Button
howtoRect = pygame.Rect((392,584,240,50))
#Back Button
backRect = pygame.Rect((392,584,240,50))
#decrement number of turns
decTurnsRect = pygame.Rect((360,410,60,60))
#increment number of turns
incTurnsRect = pygame.Rect((604,410,60,60))
#number of turns
numTurnsRect = pygame.Rect((442,410,142,60))
#number of turns left
numTurnsLeftRect = pygame.Rect((730,50,140,50))
#decrement grid size
decGridSizeRect = pygame.Rect((360,330,60,60))
#increment grid size
incGridSizeRect = pygame.Rect((604,330,60,60))
#grid size
gridSizeRect = pygame.Rect((442,330,142,60))
#exit
exitRect=pygame.Rect((392,659,240,50))

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

    blacklist=[] #stores numbers of the boxes clicked (already)
    turncount=0 #to check turn count
    maxturns = 6 #default number of turns allowed
    haswon=False #to check if successfully selected the key
    buttonWidth=240
    buttonHeight=50
    buttonLeft=width/2-(buttonWidth/2)
    buttonRight=width/2+(buttonWidth/2)
    gridLength = 5 #default grid length
    gridSize = gridLength ** 2 #number of squares
    upperLimitTurnCount=7
    lowerLimitTurnCount=5

    done=False #loop variable

    howto = False #Instruction Menu
    start = False #Game Start

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

        #main menu
        if start == False and howto == False:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if howtoRect.collidepoint(event.pos):
                    howto = True

                elif startRect.collidepoint(event.pos):
                    start = True
                    break


                elif incTurnsRect.collidepoint(event.pos):
                    if maxturns<upperLimitTurnCount:
                        maxturns=maxturns+1

                elif decTurnsRect.collidepoint(event.pos):
                    if maxturns>lowerLimitTurnCount:
                        maxturns=maxturns-1

                elif incGridSizeRect.collidepoint(event.pos):
                    if gridLength<6:
                        gridLength=gridLength+1

                        upperLimitTurnCount, lowerLimitTurnCount = getLimits(gridLength)

                        if maxturns > upperLimitTurnCount or maxturns < lowerLimitTurnCount:
                            maxturns = upperLimitTurnCount

                elif decGridSizeRect.collidepoint(event.pos):
                    if gridLength>4:
                        gridLength=gridLength-1

                        upperLimitTurnCount, lowerLimitTurnCount = getLimits(gridLength)

                        if maxturns > upperLimitTurnCount or maxturns < lowerLimitTurnCount:
                            maxturns = upperLimitTurnCount

                elif exitRect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            title = pygame.font.SysFont("symbola",100)
            textSurf1, textRect1 = text_objects("Find The Key!", title)
            textRect1.center = ( (width/2), (height/2) - 150)

            findkey = pygame.font.SysFont("liberationserif",20)
            textSurf2, textRect2 = text_objects("LET'S FIND THE KEY!", findkey)
            textRect2.center = ( (width/2), (height/2) + 150)

            howtotext = pygame.font.SysFont("liberationserif",20)
            textSurf3, textRect3 = text_objects("HOW-TO-PLAY", howtotext)
            textRect3.center = ( (width/2), (height/2) + 225)

            decTurnText = pygame.font.SysFont("liberationserif",40)
            textSurf4, textRect4 = text_objects("-", decTurnText)
            textRect4.center = ( 390, 440)

            incTurnText = pygame.font.SysFont("liberationserif",40)
            textSurf5, textRect5 = text_objects("+", incTurnText)
            textRect5.center = ( 634, 440)

            numTurnText = pygame.font.SysFont("liberationserif",30)
            textSurf6, textRect6 = text_objects(str(maxturns) + " turns", numTurnText)
            textRect6.center = ( 512, 440)

            decGridText = pygame.font.SysFont("liberationserif",40)
            textSurf7, textRect7 = text_objects("-", decGridText)
            textRect7.center = ( 390, 360)

            incGridText = pygame.font.SysFont("liberationserif",40)
            textSurf8, textRect8 = text_objects("+", incGridText)
            textRect8.center = ( 634, 360)

            gridSizeText = pygame.font.SysFont("liberationserif",30)
            textSurf9, textRect9 = text_objects(str(gridLength) + " x " + str(gridLength), gridSizeText)
            textRect9.center = ( 512, 360)

            exittext = pygame.font.SysFont("liberationserif",20)
            textSurf10, textRect10 = text_objects("EXIT", exittext)
            textRect10.center = ( (width/2), (height/2) + 300)

            windowSurface.blit(pygame.transform.scale(KEYPIC,(200,100)),(412,70))

            if x>=buttonLeft and x<=buttonRight and y>=height/2+125 and y<=height/2+125+buttonHeight:
                pygame.draw.rect(windowSurface, GOLD, startRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, startRect)

            if x>=buttonLeft and x<=buttonRight and y>=height/2+200 and y<=height/2+200+buttonHeight:
                pygame.draw.rect(windowSurface, GOLD, howtoRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, howtoRect)

            if x>=buttonLeft and x<=buttonRight and y>=height/2+275 and y<=height/2+275+buttonHeight:
                pygame.draw.rect(windowSurface, GOLD, exitRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, exitRect)

            if x>=360 and x<=420 and y>=410 and y<=470:
                pygame.draw.rect(windowSurface, GOLD, decTurnsRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, decTurnsRect)

            if x>=604 and x<=664 and y>=410 and y<=470:
                pygame.draw.rect(windowSurface, GOLD, incTurnsRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, incTurnsRect)

            if x>=360 and x<=420 and y>=330 and y<=390:
                pygame.draw.rect(windowSurface, GOLD, decGridSizeRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, decGridSizeRect)

            if x>=604 and x<=664 and y>=330 and y<=390:
                pygame.draw.rect(windowSurface, GOLD, incGridSizeRect)

            else:
                pygame.draw.rect(windowSurface, GREEN, incGridSizeRect)


            pygame.draw.rect(windowSurface, WHITE, numTurnsRect)
            pygame.draw.rect(windowSurface, WHITE, gridSizeRect)

            windowSurface.blit(textSurf1, textRect1)
            windowSurface.blit(textSurf2, textRect2)
            windowSurface.blit(textSurf3, textRect3)
            windowSurface.blit(textSurf4, textRect4)
            windowSurface.blit(textSurf5, textRect5)
            windowSurface.blit(textSurf6, textRect6)
            windowSurface.blit(textSurf7, textRect7)
            windowSurface.blit(textSurf8, textRect8)
            windowSurface.blit(textSurf9, textRect9)
            windowSurface.blit(textSurf10, textRect10)

        #how to screen
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

    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    gridSize = gridLength ** 2
    rects=[0 for i in range(gridSize)] #list for boxes in the game
    key_idx=random.randint(1,gridSize) #randomize box with key

    #start game
    while not done and start == True:
        right=50
        down=50
        horizontal=100
        vertical=100
        turnsleft = maxturns-turncount
        numTurnsLeft = pygame.font.SysFont("liberationserif",30)
        gameOverText = pygame.font.SysFont("liberationserif",25)

        for event in pygame.event.get():

            if event.type==QUIT:
                pygame.quit()
                sys.exit()

            if event.type==MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos

                for rec in rects:
                    if rec.collidepoint(pos):
                        distance=sqrt((rec.center[0]-rects[key_idx-1].center[0])**2 + (rec.center[1]-rects[key_idx-1].center[1])**2)
                        # distance to hot/cold measure
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
                        pygame.time.delay(3200)
                        pygame.mixer.music.load('./sounds/BackgroundMusic.mp3')
                        pygame.mixer.music.set_volume(0.4)
                        pygame.mixer.music.play(-1)
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
                                textSurf9, textRect9 = text_objects("GAME OVER", gameOverText)
                                pygame.draw.rect(windowSurface, LIGHTRED, numTurnsLeftRect)
                                textRect9.center = (800, 75)
                                windowSurface.blit(textSurf9, textRect9)
                                pygame.mixer.music.load('./sounds/lose.mp3')
                                pygame.mixer.music.play(0)
                                pygame.display.flip()
                                pygame.time.delay(3200)
                                pygame.mixer.music.load('./sounds/BackgroundMusic.mp3')
                                pygame.mixer.music.set_volume(0.4)
                                pygame.mixer.music.play(-1)
                                pygame.time.delay(1500)
                                show_end_screen()

        windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0))

        if turnsleft<=8 and turnsleft>5:
            textSurf11, textRect11 = text_objects(str(turnsleft) + " turns left", numTurnsLeft)
            textRect11.center = (800, 75)
            pygame.draw.rect(windowSurface, LIMEGREEN, numTurnsLeftRect)

        elif turnsleft<=5 and turnsleft>3:
            textSurf11, textRect11 = text_objects(str(turnsleft) + " turns left", numTurnsLeft)
            textRect11.center = (800, 75)
            pygame.draw.rect(windowSurface, LIGHTBLUE, numTurnsLeftRect)

        elif turnsleft<=3 and turnsleft>1:
            textSurf11, textRect11 = text_objects(str(turnsleft) + " turns left", numTurnsLeft)
            textRect11.center = (800, 75)
            pygame.draw.rect(windowSurface, LIGHTYELLOW, numTurnsLeftRect)

        elif turnsleft==1:
            textSurf11, textRect11 = text_objects(str(turnsleft) + " turn left", numTurnsLeft)
            textRect11.center = (800, 75)
            pygame.draw.rect(windowSurface, LIGHTYELLOW, numTurnsLeftRect)

        windowSurface.blit(textSurf11, textRect11)

        for i in range(gridSize):
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
            if right==(50+100*(gridLength)):
                down+=100
                right=50
        windowSurface.blit(therm,therm.get_rect(center=(8*size[0]/10,size[1]/2)))
        if haswon:
            pygame.time.delay(500)
            #'you win!'
            done=True
            textSurf11, textRect11 = text_objects("YOU WIN", numTurnsLeft)
            pygame.draw.rect(windowSurface, LIMEGREEN, numTurnsLeftRect)
            textRect11.center = (800, 75)
            windowSurface.blit(textSurf11, textRect11)
            pygame.display.flip()
            pygame.time.delay(1000)
            show_end_screen()

        pygame.display.flip()

def show_end_screen():
    BG=pygame.image.load('Images/jail2.png')
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

            elif event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if restart == True:
            search_key()


def getLimits(gridLength):

    if gridLength == 4:
        return 5,4

    elif gridLength == 5:
        return 7,5

    else:
        return 8,7

if __name__=='__main__':
    search_key()
