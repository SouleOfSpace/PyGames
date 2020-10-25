import pygame, time
from  random import randint
pygame.init()

#размеры окна
WIN_WIDTH = 500
WIN_HEIGHT = 500

#флаг для основного цикла
flag= True

widthScrol = 50
heightScrol = 10

count_rows = 5

FPS = 60
clock = pygame.time.Clock()

COLORSDict = {'black': (85, 49, 100), 'white': (255, 255, 255), 'pink': (255, 192, 203), 'yellow': (255, 255, 0), 'red': (255, 0, 0), 'blue': (0, 0, 255),
          'green': (0, 255, 0), 'fuchsia': (255, 0, 255), 'tomato': (255, 99, 71), 'burlyWood': (222, 184, 135), 'indigo': (75, 0, 130)}

COLORSStr = ['black', 'white', 'pink', 'yellow', 'red', 'blue', 'green', 'fuchsia', 'tomato', 'burlyWood', 'indigo']

kor_x_scrol = 5
KOR_Y_SCROL = WIN_HEIGHT - 40
speed_scrol = 5

radius = 8
speed_circle = 3
kor_x_circle = kor_x_scrol + widthScrol//2
kor_y_circle = KOR_Y_SCROL - radius
routeTopCircle = False
routeBottomCircle = False
routeRightCircle = True
routeLeftCircle = False

xRing = 5
yRing = 5

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)

total = 0

#крайние точки (верхняя и нижняя) при движении шара
pointCircle = [kor_x_circle, 5, kor_y_circle]

def getCreatedRectangls():
    #создаем статичные прямоугольники, располагаем их на рабочем окне, заносим в массив и выводим его
    global sc, COLORS

    # размеры для статичных прямоугольников
    max_width = 40
    min_width = 20
    width = 0
    height = 15

    #координаты для статичных прямоугольников
    kor_x = 5
    kor_y = 5

    #массив созданных прямоугольников
    rectangls = []

    for i in range(0, 5):
        while (kor_x + width < WIN_WIDTH - 5):
            if (kor_x > 454):
                width = WIN_WIDTH - kor_x - 5
            else:
                # width = randint(min_width, max_width)
                width = 40

            color = COLORSDict[COLORSStr[randint(0, len(COLORSStr) - 1)]]
            rect = pygame.Rect((kor_x, kor_y, width, height))
            rectangls.append([color, rect])

            kor_x += width + 2

        kor_y += height + 40
        kor_x = 5

    return rectangls

def drawScrol(kor_x_scrol):
    #рисуем скрол в зависимости от действий пользователя (нажата клавиша влево или вправо)
    global  KOR_Y_SCROL, widthScrol, heightScrol, COLORSDict, sc

    rectScrol = pygame.Rect((kor_x_scrol, KOR_Y_SCROL, widthScrol, heightScrol))
    pygame.draw.rect(sc, COLORSDict['green'], rectScrol)

def drawCircle():
    #рисуем шар
    global sc, kor_x_circle, kor_y_circle, COLORSDict

    pygame.draw.circle(sc, COLORSDict['yellow'], (kor_x_circle, kor_y_circle), 8)

def drawRing(x, y):
    global sc, COLORSDict
    minRadius = 2

    for radius in range(8, 16):
        pygame.draw.circle(sc, COLORSDict['yellow'], (x, y), radius, minRadius)
        minRadius +=1

def moveCircleVertical(top, bottom):
    #перемещение шара по вертикали
    global kor_y_circle, kor_x_circle, speed_circle, radius, kor_x_scrol, widthScrol, KOR_Y_SCROL, total

    if(top):
        kor_y_circle -=speed_circle
    elif(bottom):
        if (KOR_Y_SCROL - (kor_y_circle + radius) < speed_circle and kor_x_circle >= kor_x_scrol and kor_x_circle <= kor_x_scrol + widthScrol):
            kor_y_circle += KOR_Y_SCROL - kor_y_circle - radius
        else:
            kor_y_circle +=speed_circle
    else:
        time.sleep(2)
        total -=5
        kor_y_circle = KOR_Y_SCROL - radius
        kor_x_circle = kor_x_scrol + widthScrol // 2

def moveCircleGorizontal(left, right):
    #Перемещение шара по горизонтали
    global  kor_x_circle, speed_circle

    if (left):
        kor_x_circle -=speed_circle
    elif (right):
        kor_x_circle +=speed_circle
    else:
        return

def choiseDirectionFromRect():
    global routeLeftCircle, routeRightCircle, routeTopCircle, routeBottomCircle, radius, kor_x_circle, kor_y_circle,\
        rectanglsArr, topPoint, bottomPoint, pointCircle, total

    kor_y_bot_circle = kor_y_circle + radius
    kor_y_top_circle = kor_y_circle - radius
    kor_x_left_circle = kor_x_circle - radius
    kor_x_right_circle = kor_x_circle + radius

    for rect in rectanglsArr:
        rect_y_bot = rect[1].y + rect[1].height
        rect_y_top = rect[1].y
        rect_x_left = rect[1].x
        rect_x_rig = rect[1].x + rect[1].width

        if (kor_y_top_circle <= rect_y_bot and kor_y_bot_circle >= rect_y_top and pointCircle[2] > kor_y_circle and kor_x_right_circle >= rect_x_left and kor_x_circle <= rect_x_rig):
            rectanglsArr.pop(rectanglsArr.index(rect))
            pointCircle[0] = pointCircle[1]
            pointCircle[1] = kor_x_circle
            pointCircle[2] = kor_y_circle

            total +=1

            routeBottomCircle = True
            routeTopCircle = False
        elif (kor_y_top_circle <= rect_y_bot and kor_y_bot_circle >= rect_y_top and pointCircle[2] < kor_y_circle and kor_x_right_circle >= rect_x_left and kor_x_circle <= rect_x_rig):
            rectanglsArr.pop(rectanglsArr.index(rect))
            pointCircle[0] = pointCircle[1]
            pointCircle[1] = kor_x_circle
            pointCircle[2] = kor_y_circle

            total += 1

            routeTopCircle = True
            routeBottomCircle = False
        elif (kor_x_right_circle >= rect_x_left and kor_x_left_circle <= rect_x_left + 10 and kor_y_bot_circle <= rect_y_top and kor_y_top_circle >= rect_y_bot):
            rectanglsArr.pop(rectanglsArr.index(rect))
            pointCircle[0] = pointCircle[1]
            pointCircle[1] = kor_x_circle

            routeRightCircle = False
            routeLeftCircle = True
        elif (kor_x_left_circle <= rect_x_rig and kor_x_right_circle >= rect_x_rig - 10 and kor_y_bot_circle <= rect_y_top and kor_y_top_circle >= rect_y_bot):
            rectanglsArr.pop(rectanglsArr.index(rect))
            pointCircle[0] = pointCircle[1]
            pointCircle[1] = kor_x_circle

            routeLeftCircle = False
            routeRightCircle = True

def getTotal():
    global total

    font = pygame.font.Font(None, 25)
    text = font.render(str(total), True, COLORSDict['tomato'])

    return text




#массив статичных прямоугольников
rectanglsArr = getCreatedRectangls()

#основной цикл
while flag:
    clock.tick(FPS)                     #задержка в 60 FPS
    sc.fill((0, 0, 0))                  #обновление рабочего окна с черным фоном
    text = getTotal()
    sc.blit(text, [300, 300])
    keys = pygame.key.get_pressed()     #действия пользователя

    #выход из приложения
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    #рисуем статичные прямоугольники
    for rect in rectanglsArr:
        pygame.draw.rect(sc, rect[0], rect[1])

    #управление местонахождением скрола
    if (keys[pygame.K_LEFT] and kor_x_scrol > 5):
        kor_x_scrol -=speed_scrol
    elif (keys[pygame.K_RIGHT] and kor_x_scrol < WIN_WIDTH - 5 - widthScrol):
        kor_x_scrol +=speed_scrol

#---------------------------------------------------------------
    choiseDirectionFromRect()

    #направление движения шара
    if (kor_y_circle + radius == KOR_Y_SCROL and kor_x_circle >= kor_x_scrol and kor_x_circle <= kor_x_scrol + widthScrol):
        routeTopCircle = True
        routeBottomCircle = False

        pointCircle[1] = pointCircle[1]
        pointCircle[0] = kor_x_circle

        pointCircle[2] = kor_y_circle
    elif (kor_y_circle + radius > KOR_Y_SCROL):
        routeBottomCircle = False
        routeTopCircle = False

        pointCircle[2] = kor_y_circle
    elif (kor_y_circle < 10):
        routeBottomCircle = True
        routeTopCircle = False

        pointCircle[0] = pointCircle[1]
        pointCircle[1] = kor_x_circle


    if (kor_x_circle <= 5):
        routeLeftCircle = False
        routeRightCircle = True

        pointCircle[0] = pointCircle[1]
        pointCircle[1] = kor_x_circle
    elif (kor_x_circle >= WIN_WIDTH - 5):
        routeLeftCircle = True
        routeRightCircle = False

        pointCircle[0] = pointCircle[1]
        pointCircle[1] = kor_x_circle
    elif (kor_y_circle + radius == KOR_Y_SCROL and pointCircle[1] > pointCircle[0]):
        routeLeftCircle = True
        routeRightCircle = False
    elif (kor_y_circle + radius == KOR_Y_SCROL and pointCircle[1] < pointCircle[0]):
        routeLeftCircle = False
        routeRightCircle = True

    #движение шара в зависимости от направления
    moveCircleVertical(routeTopCircle, routeBottomCircle)
    moveCircleGorizontal(routeLeftCircle, routeRightCircle)

    drawScrol(kor_x_scrol)
    drawCircle()

    pygame.display.update()
