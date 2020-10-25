import pygame

class Withbong:
    def __init__(self, x, y, radius, color, facing):
        self.x = x #кордината x снаряда
        self.y = y #кордината y снаряда
        self.radius = radius #радиус снаряда
        self.color = color #цвет снаряда
        self.facing = facing #направление снаряда
        self.vel = facing * 8 #скорость снаряда

    def draw(self, win):
        #рисуем снаряды
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

