import pygame

from ticTacToe import withBong

pygame.init()

def moveObject(keys, WIN_WIDTH, WIN_HEIGHT, width, height, kor_x, kor_y, run, isJump, left=False, right=False):
    # перемещение объекта принажатии на кнопки

    if (keys[pygame.K_LEFT] and kor_x > 5):
        kor_x -= run
        left = True
    elif (keys[pygame.K_RIGHT]) and kor_x < WIN_WIDTH - width - 5:
        kor_x += run
        right = True
    if (keys[pygame.K_UP] and isJump == False and kor_y > 5):
        kor_y -= run
    elif (keys[pygame.K_DOWN] and isJump == False and kor_y < WIN_HEIGHT - height - 5):
        kor_y += run
    else:
        return [{'kor_x': kor_x, 'kor_y': kor_y}, {'left': left, 'right': right}]

    return [{'kor_x': kor_x, 'kor_y': kor_y}, {'left': left, 'right': right}]

def jumpObject(keys, isJump, jumpStep, kor_y):
    #подпрыгивание объекта при нажатии на пробел
    if (keys[pygame.K_SPACE]):
        isJump = True

    if (isJump and jumpStep >= -10):
        if (jumpStep > 0):
            kor_y -= (jumpStep ** 2) / 4
            jumpStep -= 1
            return {'kor_y': kor_y, 'jumpStep': jumpStep, 'isJump': isJump}
        else:
            kor_y += (jumpStep ** 2) / 4
            jumpStep -= 1
            return {'kor_y': kor_y, 'jumpStep': jumpStep, 'isJump': isJump}
    else:
        isJump = False
        jumpStep = 10
        return {'kor_y': kor_y, 'jumpStep': jumpStep, 'isJump': isJump}

def main():
    WIN_WIDTH = 500     #ширина окна
    WIN_HEIGHT = 500    #высота окна

    width = 60          #ширина объекта
    height = 71         #высота объекта

    kor_x = 20          #координата по х объетка
    kor_y = 20          # коордиата по у объкта

    run = 5             #скорость объкта
    jumpStep = 10       #шаг прыжка объекта
    isJump = False      #условин: делпть прыжок или нет

    FPS = 60
    clock = pygame.time.Clock()

    animCount = 0       #счетчик анимаций объекта
    left = False
    right = False

    def drawWindow():
        #рисование окна и объктов
        #рисуем окно
        sc.blit(bg, (0, 0))

        #рисуем объкт
        if (left):
            sc.blit(imgGoLeft[animCount // 10], (kor_x, kor_y))
        elif (right):
            sc.blit(imgGoRight[animCount // 10], (kor_x, kor_y))
        else:
            sc.blit(imgStay, (kor_x, kor_y))

        #рисуем снаряд
        for bullet in bullets:
            bullet.draw(sc)
            break

        pygame.display.update()

        return animCount

    #загрузка изображений для приложения
    imgGoLeft = [pygame.image.load('pygame_left_1.png'), pygame.image.load('pygame_left_2.png'), pygame.image.load('pygame_left_3.png'),
                 pygame.image.load('pygame_left_4.png'), pygame.image.load('pygame_left_5.png'), pygame.image.load('pygame_left_6.png')]
    imgGoRight = [pygame.image.load('pygame_right_1.png'), pygame.image.load('pygame_right_2.png'), pygame.image.load('pygame_right_3.png'),
                  pygame.image.load('pygame_right_4.png'), pygame.image.load('pygame_right_5.png'), pygame.image.load('pygame_right_6.png')]
    imgStay = pygame.image.load('trumpStay.png')
    bg = pygame.image.load('pygame_bg.jpg')

    #создание главного окна
    sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('My_progect')

    BLACK = (0, 0, 0)
    GREEN = (0, 200, 64)

    #массив для хранения снарядов
    bullets = []

    #основной цикл работы приложения
    while True:
        clock.tick(FPS)

        #выход из приложения
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        #хранит ключи последних действий пользователя
        keys = pygame.key.get_pressed()

        # ключи последних действий объекта
        dictKor = moveObject(keys, WIN_WIDTH, WIN_HEIGHT, width, height, kor_x, kor_y, run, isJump)
        kor_x = dictKor[0]['kor_x']
        kor_y = dictKor[0]['kor_y']
        left = dictKor[1]['left']
        right = dictKor[1]['right']

        dictJump = jumpObject(keys, isJump, jumpStep, kor_y)
        isJump = dictJump['isJump']
        jumpStep = dictJump['jumpStep']
        kor_y = dictJump['kor_y']

        #обновление счетчика изображений
        if (animCount >= FPS-1): animCount = 0
        else: animCount +=1

        #условия полета пуль и их обновление
        if keys[pygame.K_f]:
            if (right): facing = 1
            elif (left): facing = -1

            if (len(bullets) < 5):
                bullets.append(withBong.Withbong(round(kor_x + width // 2),
                                                 round(kor_y + height // 2), 8, BLACK, facing))

        for bullet in bullets:
            if (bullet.x < 500 and bullet.x > 0):
                bullet.x +=bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
                print(bullet.x)

        drawWindow()

if __name__ == '__main__':
    main()
