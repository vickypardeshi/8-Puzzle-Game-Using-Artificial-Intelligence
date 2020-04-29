import pygame, sys, time
from pygame.locals import *
from TilesPuzzleSolver import *

puzzle = puzzle()

pygame.init()
WindowWidth = 700
WindowHeight = 700
BasicFont = pygame.font.Font('freesansbold.ttf',50)
WindowSurface = pygame.display.set_mode((WindowWidth, WindowHeight))
pygame.display.set_caption('9 Tiles Puzzle')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
Text = (0,0,0)

StartButton = pygame.draw.rect(WindowSurface,(0,255,0),(220,600,100,50));
QuitButton = pygame.draw.rect(WindowSurface,(0,0,255),(380,600,100,50));

TileTop = 200;
TileLeft = 200;
Tiles = []
Row = 0

tileNumbers = ['1','2','3','4','5','6','7','8','-']

# Set up the tiles data structure.
for i in tileNumbers:
    if i == '-':
        Tiles.append({'rect':pygame.Rect(TileLeft,TileTop,99,99),'color':BLACK,'block':str(i)})
    else:
        Tiles.append({'rect':pygame.Rect(TileLeft,TileTop,99,99),'color':RED,'block':str(i)})

    Row += 1
    TileLeft += 100
    if Row == 3:
        TileTop += 100
        TileLeft = 200
        Row = 0


for i in Tiles:        
        pygame.draw.rect(WindowSurface, i['color'], i['rect'])
        textSurf = BasicFont.render(i['block'], True, Text)
        textRect = textSurf.get_rect()
        textRect.center = i['rect'].left+50, i['rect'].top+50
        WindowSurface.blit(textSurf, textRect)
        
pygame.display.update()


numberOfShuffles = 50
gameStart = False

while True :
    #check for GAME START or QUIT
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            #game start
            if pygame.mouse.get_pos()[0] >= 220 and pygame.mouse.get_pos()[1] >= 600:
                if pygame.mouse.get_pos()[0] <= 320 and pygame.mouse.get_pos()[1] <= 650:
                    gameStart = True
                    
            #game quit    
            if pygame.mouse.get_pos()[0] >= 380 and pygame.mouse.get_pos()[1] >= 600:
                if pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] <= 650:
                    pygame.quit()
                    sys.exit()


    while numberOfShuffles > 0:
        puzzle.shuffler()
        puzzle.PreviousStates.extend(puzzle.InitialState)

        block = 0
        for tile in Tiles:
            tile['block'] = str(puzzle.InitialState[block])
            block += 1

            if tile['block'] == '-':
                tile['color'] = BLACK

            else:
                tile['color'] = RED

            pygame.draw.rect(WindowSurface, tile['color'], tile['rect'])
            textSurf = BasicFont.render(tile['block'], True, Text)
            textRect = textSurf.get_rect()
            textRect.center = tile['rect'].left+50, tile['rect'].top+50
            WindowSurface.blit(textSurf, textRect)

        pygame.display.update()
        time.sleep(0.04)
        numberOfShuffles -= 1


    if gameStart == True:
        puzzle.puzzleSolver(puzzle.InitialState)
        nextState = puzzle.getNextState()

        block = 0
        for tile in Tiles:
            tile['block'] = str(nextState[block])
            block += 1

            if tile['block'] == '-':
                tile['color'] = BLACK

            else:
                tile['color'] = RED

            pygame.draw.rect(WindowSurface, tile['color'], tile['rect'])
            textSurf = BasicFont.render(tile['block'], True, Text)
            textRect = textSurf.get_rect()
            textRect.center = tile['rect'].left+50, tile['rect'].top+50
            WindowSurface.blit(textSurf, textRect)

        pygame.display.update()
        time.sleep(0.4)
        NoOfMove= 1

        while nextState != puzzle.GoalState :
            NoOfMove += 1

            puzzle.puzzleSolver(nextState)
            nextState = puzzle.getNextState()

            block = 0
            for tile in Tiles:
                tile['block'] = str(nextState[block])
                block += 1

                if tile['block'] == '-':
                    tile['color'] = BLACK

                else:
                    tile['color'] = RED

                pygame.draw.rect(WindowSurface, tile['color'], tile['rect'])
                textSurf = BasicFont.render(tile['block'], True, Text)
                textRect = textSurf.get_rect()
                textRect.center = tile['rect'].left+50, tile['rect'].top+50
                WindowSurface.blit(textSurf, textRect)

            pygame.display.update()
            time.sleep(0.04)
            
        print("Total Number Moves :",NoOfMove)

        break


while True:
    # check for the QUIT event
    for event in pygame.event.get():
        """if event.type == QUIT:
            pygame.quit()
            sys.exit()
        """
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if pygame.mouse.get_pos()[0] >= 380 and pygame.mouse.get_pos()[1] >= 600:
                if pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] <= 650:
                    pygame.quit()
                    sys.exit()
             
       
