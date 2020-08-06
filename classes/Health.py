import pygame as pg
import math

class Health(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)   
        self.image = pg.image.load("../images/Ninja/health.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)