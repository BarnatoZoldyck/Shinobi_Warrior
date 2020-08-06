import pygame as pg
import math
vector = pg.math.Vector2

class Enemy(pg.sprite.Sprite):    


    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)    
        self.velocity = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(x, y)
        self.hitCount = 0
        self.idleCount = 0
        self.attackCount = 0
        self.throwCount = 0
        self.hit = False
        self.isDead = False
        self.image = pg.image.load('../images/Enemys/enemy_1.png')   
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
      
        
    def update(self):  
        self.thrw = (pg.image.load('../images/Enemys/enemyT_1.png').convert_alpha(), pg.image.load('../images/Enemys/enemyT_2.png').convert_alpha(),pg.image.load('../images/Enemys/enemyT_3.png').convert_alpha(),pg.image.load('../images/Enemys/enemyT_4.png').convert_alpha(),pg.image.load('../images/Enemys/enemyT_5.png').convert_alpha())
        self.dth = (pg.image.load('../images/Enemys/enemyD_1.png').convert_alpha(),pg.image.load('../images/Enemys/enemyD_2.png').convert_alpha(),pg.image.load('../images/Enemys/enemyD_3.png').convert_alpha(),pg.image.load('../images/Enemys/enemyD_4.png').convert_alpha())
        
        
        if self.isDead:
            if self.idleCount <= 11:
                self.image = self.dth[self.idleCount//3]
                self.idleCount += 1
            else:
                self.image =  pg.image.load('../images/Enemys/enemyD_4.png').convert_alpha()
        else:     
            self.image = self.thrw[self.throwCount//4]
            
            self.throwCount += 1
            
            if self.throwCount >= 20:
                self.throwCount = 0

    def getRect(self):
        return self.rec.center
