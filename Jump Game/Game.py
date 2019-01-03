import pygame, sys, time, random
from pygame import freetype

#game_font = pygame.freetype.Font("Font.ttf", 75)
#text_surface, rect = game_font.render(("Programmer: 8BitToaster"), (0, 0, 0))
#gameDisplay.blit(text_surface, (150, 300))

# Initialize the game engine
pygame.init()


DisplayWidth,DisplayHeight = 800, 800
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption("Jumpy Game")
game_font = pygame.freetype.Font("Font.ttf", 24)

global CurColor
global HighScore

def MainScreen():
    global clicked
    global CurColor
    global HighScore
    
    run = True

    while run:
        gameDisplay.fill((0,100,150))
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] > 180 and pos[0] < 380 and pos[1] > 500 and pos[1] < 600:
                    if clicked == False:
                        CurColor = (255,0,0)
                    game_loop()
                if pos[0] > 310 and pos[0] < 510 and pos[1] > 650 and pos[1] < 750:
                    clicked = True
                    ChangeColor()
                if pos[0] > 425 and pos[0] < 625 and pos[1] > 500 and pos[1] < 600:
                    Credits = True
                    while Credits:
                        gameDisplay.fill((0,100,150))
                        pos = pygame.mouse.get_pos()

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pos[0] > 310 and pos[0] < 510 and pos[1] > 650 and pos[1] < 750:
                                    Credits = False
                                


                        if pos[0] > 310 and pos[0] < 510 and pos[1] > 650 and pos[1] < 750:
                            pygame.draw.rect(gameDisplay,(200,0,0),(310,650,200,100),0)
                        else:
                            pygame.draw.rect(gameDisplay,(255,0,0),(310,650,200,100),0)

                        text_surface, rect = game_font.render(("Exit"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (395, 690))

                        game_font = pygame.freetype.Font("Font.ttf", 75)

                        text_surface, rect = game_font.render(("Programmer:"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (250, 200))
                        text_surface, rect = game_font.render(("The8BitToaster"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (220, 300))

                        game_font = pygame.freetype.Font("Font.ttf", 50)

                        text_surface, rect = game_font.render(("Check him out on Youtube"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (200, 450))

                        text_surface, rect = game_font.render(("At The8BitToaster"), (0, 0, 0))
                        gameDisplay.blit(text_surface, (250, 500))

                        draw(0,0,"Overlay")
                            

                        pygame.display.flip()
                        clock.tick(20)

        draw(0,0,"Overlay")

        game_font = pygame.freetype.Font("Font.ttf", 75)
        text_surface, rect = game_font.render(("Jumpy Game"), (0, 0, 0))
        gameDisplay.blit(text_surface, (250, 200))
        game_font = pygame.freetype.Font("Font.ttf", 25)
        text_surface, rect = game_font.render(("Highscore: " + str(HighScore)), (0, 0, 0))
        gameDisplay.blit(text_surface, (350 - (10 * len(str(int(HighScore)))), 300))



        
        if pos[0] > 180 and pos[0] < 380 and pos[1] > 500 and pos[1] < 600:
            pygame.draw.rect(gameDisplay,(200,0,0),(180,500,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(255,0,0),(180,500,200,100),0)

        if pos[0] > 310 and pos[0] < 510 and pos[1] > 650 and pos[1] < 750:
            pygame.draw.rect(gameDisplay,(200,0,0),(310,650,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(255,0,0),(310,650,200,100),0)

        if pos[0] > 425 and pos[0] < 625 and pos[1] > 500 and pos[1] < 600:
            pygame.draw.rect(gameDisplay,(200,0,0),(425,500,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(255,0,0),(425,500,200,100),0)


        game_font = pygame.freetype.Font("Font.ttf", 40)
        text_surface, rect = game_font.render(("Play"), (0, 0, 0))
        gameDisplay.blit(text_surface, (230, 540))
        text_surface, rect = game_font.render(("Credits"), (0, 0, 0))
        gameDisplay.blit(text_surface, (470, 540))
        text_surface, rect = game_font.render(("Player Color"), (0, 0, 0))
        gameDisplay.blit(text_surface, (325, 690))
        

        pygame.display.flip()
        clock.tick(20)

def ChangeColor():
    global Color
    global CurColor

    ColorList = [(255,0,0),(0,0,255),(0,255,0),(255,255,0),(0,255,255),"rainbow"]
    num = 0
    RainbowNum = 0
    CurColor = ColorList[num]

    run = True
    while run:

        gameDisplay.fill((0,100,150))
        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0] > 525 and pos[0] < 625 and pos[1] > 390 and pos[1] < 430:
                    num += 1
                    if len(ColorList) == num:
                        num = 0
                    CurColor = ColorList[num]

                if pos[0] > 170 and pos[0] < 270 and pos[1] > 390 and pos[1] < 430:
                    num -= 1
                    if num == -1:
                        num = len(ColorList) - 1
                    CurColor = ColorList[num]
                if pos[0] > 310 and pos[0] < 510 and pos[1] > 650 and pos[1] < 750:
                    MainScreen()

        draw(0,0,"Overlay")

        if pos[0] > 525 and pos[0] < 625 and pos[1] > 390 and pos[1] < 430:
            pygame.draw.rect(gameDisplay,(57,255,20),(525,400,50,20),0)
            pygame.draw.polygon(gameDisplay,(57,255,20),[(575,390),(575,430),(625,410)],0)
        else:
            pygame.draw.rect(gameDisplay,(0,0,0),(525,400,50,20),0)
            pygame.draw.polygon(gameDisplay,(0,0,0),[(575,390),(575,430),(625,410)],0)

        if pos[0] > 170 and pos[0] < 270 and pos[1] > 390 and pos[1] < 430:
            pygame.draw.rect(gameDisplay,(57,255,20),(220,400,50,20),0)
            pygame.draw.polygon(gameDisplay,(57,255,20),[(220,390),(220,430),(170,410)],0)
        else:
            pygame.draw.rect(gameDisplay,(0,0,0),(220,400,50,20),0)
            pygame.draw.polygon(gameDisplay,(0,0,0),[(220,390),(220,430),(170,410)],0)

        if CurColor != "rainbow":
            pygame.draw.rect(gameDisplay,CurColor,(325,340,150,150),0)
        else:
            
            if RainbowNum >= 0 and RainbowNum <= 37:
                pygame.draw.rect(gameDisplay,(RainbowNum * 4,0 ,0 ),(325,340,150,150),0)
            elif RainbowNum >= 38 and RainbowNum <= 75:
                pygame.draw.rect(gameDisplay,(255,RainbowNum * 2,0 ),(325,340,150,150),0)
            elif RainbowNum >= 76 and RainbowNum <= 150:
                pygame.draw.rect(gameDisplay,(255,255,RainbowNum),(325,340,150,150),0)
            elif RainbowNum >= 151 and RainbowNum <= 200:
                pygame.draw.rect(gameDisplay,(255 - (200-RainbowNum) * 5,255,255),(325,340,150,150),0)
            elif RainbowNum >= 201 and RainbowNum <= 225:
                pygame.draw.rect(gameDisplay,(0,255 - (225-RainbowNum) * 5,255),(325,340,150,150),0)
            elif RainbowNum >= 226 and RainbowNum <= 255:
                pygame.draw.rect(gameDisplay,(0,0,255 - (255-RainbowNum) * 5),(325,340,150,150),0)
            else:
                RainbowNum = 0
            RainbowNum += 2


        if pos[0] > 310 and pos[0] < 510 and pos[1] > 650 and pos[1] < 750:
            pygame.draw.rect(gameDisplay,(200,0,0),(310,650,200,100),0)
        else:
            pygame.draw.rect(gameDisplay,(255,0,0),(310,650,200,100),0)

        text_surface, rect = game_font.render(("Exit"), (0, 0, 0))
        gameDisplay.blit(text_surface, (395, 690))
            
        
        pygame.display.flip()
        clock.tick(20)


def randomPlatform():
    return [random.randint(150,450),0]

def boundaries():
    global Platforms
    global gravity
    global x
    global y
    global JumpAllowed

    stop = False

    for platform in Platforms:
        if x >= platform[0] - 50 and x <= platform[0] + 200 and platform[1] >= y + 35 and platform[1] <= y + 55:
            if gravity != -20 and gravity >= 0:
                y = platform[1] - 45
                gravity = 0
                stop = True
                JumpAllowed = True
    if stop == False:
        gravity += 1

def draw(x,y,Obj):
    global score
    global PlatformCount
    global CurColor
    global RainbowNum
    if Obj == "Overlay":
        pygame.draw.rect(gameDisplay,(100,100,100),(0,0,150,800),0)
        pygame.draw.rect(gameDisplay,(100,100,100),(650,0,150,800),0)
        pygame.draw.rect(gameDisplay,(0,0,0),(0,0,150,800),10)
        pygame.draw.rect(gameDisplay,(0,0,0),(650,0,150,800),10)
    if Obj == "Score":
        game_font = pygame.freetype.Font("Font.ttf", 24)
        text_surface, rect = game_font.render(("Score: " + str(int(score))), (0, 0, 0))
        gameDisplay.blit(text_surface, (20, 50))
        text_surface, rect = game_font.render(("Platforms: " + str(int(PlatformCount))), (0, 0, 0))
        gameDisplay.blit(text_surface, (20, 80))
    if Obj == "platform":
        pygame.draw.rect(gameDisplay,(100,100,100),(x,y,200,20),0)
        pygame.draw.rect(gameDisplay,(0,0,0),(x,y,200,20),5)
    if Obj == "player":
        if CurColor != "rainbow":
            pygame.draw.rect(gameDisplay,CurColor,(x,y,50,50),0)
        else:
            if RainbowNum >= 0 and RainbowNum <= 37:
                pygame.draw.rect(gameDisplay,(RainbowNum * 4,0 ,0 ),(x,y,50,50),0)
            elif RainbowNum >= 38 and RainbowNum <= 75:
                pygame.draw.rect(gameDisplay,(255,RainbowNum * 2,0 ),(x,y,50,50),0)
            elif RainbowNum >= 76 and RainbowNum <= 150:
                pygame.draw.rect(gameDisplay,(255,255,RainbowNum),(x,y,50,50),0)
            elif RainbowNum >= 151 and RainbowNum <= 200:
                pygame.draw.rect(gameDisplay,(255 - (200-RainbowNum) * 5,255,255),(x,y,50,50),0)
            elif RainbowNum >= 201 and RainbowNum <= 225:
                pygame.draw.rect(gameDisplay,(0,255 - (225-RainbowNum) * 5,255),(x,y,50,50),0)
            elif RainbowNum >= 226 and RainbowNum <= 255:
                pygame.draw.rect(gameDisplay,(0,0,255 - (255-RainbowNum) * 5),(x,y,50,50),0)
            else:
                RainbowNum = 0
            RainbowNum += 2

def game_loop():
    global Platforms
    global gravity
    global x
    global y
    global JumpAllowed
    global score
    global PlatformCount
    global RainbowNum
    global HighScore
    game_run = True
    Platforms = [[300,-100],[300,550]]
    score = 0
    PlatformCount = 0
    if CurColor == "rainbow":
        RainbowNum = 0

    for i in range(6):
        Platforms.append([random.randint(150,450),(i*100) + 100])

    x = 400
    y = 500
    x_change = 0
    gravity = 0
    JumpAllowed = True

    while game_run == True:

        gameDisplay.fill((0,100,150))

        #Key Checker
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_a]:
            x_change -= 0.5
        if keys[pygame.K_d]:
            x_change += 0.5
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and JumpAllowed == True:
                    tempX = x_change
                    if tempX <= 0:
                        tempX *= -1
                    gravity = -1 * tempX - 10
                    JumpAllowed = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0 

        stop = False
        if x + x_change < 145:
            stop = True
        if x + x_change > 610:
            stop = True
        if stop == False:
            x += x_change
        y += gravity
        if gravity < 0:
            score += gravity * -1
        else:
            score += gravity
        
        draw(0,0,"Overlay")
        draw(0,0,"Score")

        for platform in Platforms:
            if y <= 100:
                if PlatformCount >= 10:
                    platform[1] += 15 * PlatformCount/50 + 1
            elif y <= 300:
                platform[1] += 10 * PlatformCount/50 + 1
            else:
                platform[1] += 5 * PlatformCount/50 + 1
            if gravity < 0:
                platform[1] -= gravity
            if platform[1] >= 800:
                Platforms[Platforms.index(platform)] = randomPlatform()
                PlatformCount += 1
            draw(platform[0],platform[1],"platform")

        draw(x,y,"player")
        boundaries()

        if y >= 800:
            if score > HighScore:
                HighScore = score
            MainScreen()

            

        pygame.display.flip()
        clock.tick(60)


clicked = False
HighScore = 0
MainScreen()
