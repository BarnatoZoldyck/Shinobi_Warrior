import pygame as pg
import math
vector = pg.math.Vector2

class Player(pg.sprite.Sprite):

    def __init__(self, x, y, g):
        pg.sprite.Sprite.__init__(self)
        #movement of player
        self.mainGame = g;
        self.pressKey =  pg.key.get_pressed()
        self.speed = 0.8
        self.velocity = vector(0,0) #velocity of player
        self.acc = vector(0,0)
        self.pos = vector(x, y)
        self.fric = -0.15
        #rect of player
        self.image = pg.image.load('../images/Ninja/R_idle_1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.isDownR = False
        self.isDownL = False
        self.isRunR = False
        self.isRunL = False
        self.isJump = False
        self.isUpR = False
        self.isUpL = False
        self.isIdle = True
        self.isAtck = False
        self.isL = False
        self.isR = True
        self.isHurt = False
        self.isDead = False
        self.jumpC = 7
        self.walkC = 0
        self.runC = 0 
        self.idle = 0  
        self.atckUC = 0
        self.atckC = 0  
        self.hurtCount = 0 #formerly hrtC
        self.deathCount = 0 #formerly dthC
        self.atckIsK = False
        self.atckIsI = False
        self.atckIsL = False 
 
        
    def update(self):
        self.animation()
        #============
        #KEYS INPUT
        #============
        self.acc = vector(0,0)
        if not self.isDead:
            if pg.key.get_pressed()[pg.K_d] or pg.key.get_pressed()[pg.K_RIGHT]:
                self.acc.x = self.speed
                self.isR = True
                self.isL = False
                self.isIdle = False
                self.isRunL = False
                self.isRunR = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif (pg.key.get_pressed()[pg.K_s] or pg.key.get_pressed()[pg.K_DOWN]):
                self.acc.x = self.speed * 2
                self.isR = False
                self.isL = False 
                self.isRunR = True
                self.isIdle = False
                self.isRunL = False
                self.isAtck = False
                self.atckC = 0
                self.atckUC = 0
            elif pg.key.get_pressed()[pg.K_k]:
                self.isAtck = True  
                self.atckIsK = True 
                self.atckIsL = False
                self.atckIsI = False
                self.isIdle = False 
            elif pg.key.get_pressed()[pg.K_i]:
                self.isAtck = True 
                self.atckIsI = True
                self.atckIsK = False  
                self.atckIsL = False 
                self.isIdle = False 
            elif pg.key.get_pressed()[pg.K_l]:
                self.isAtck = True 
                self.atckIsL = True 
                self.atckIsI = False
                self.atckIsK = False  
                self.isIdle = False         
            else:
                self.idle += 1
                self.isIdle = True
                self.isAtck = False 
                self.atckIsI = False
                self.atckIsK = False   
                self.atckIsL = False  
    
            #applies friction    
            self.acc += self.velocity * self.fric    
            
            #equations of motion
            self.velocity += self.acc
            self.pos += self.velocity + 0.5 * self.acc
            
            #changing screens
            if self.pos.x > self.mainGame.windowWidth:
                self.pos.x = 40   
                self.mainGame.background_no += 1
                self.mainGame.red.isDead = False
                
                for  kunai in self.mainGame.kunais:
                    kunai.pos = self.mainGame.red.pos
                     
                if self.mainGame.background_no >= 5:
                    self.mainGame.background_no = 1
                    
            if self.pos.x <= 10:
                self.pos.x = 40
                self.isR = True
                self.isL = False
             
            #changing position
            self.rect.center = self.pos  
              
            #==============
            #JUMPING
            #==============
        
            if not self.isJump:
                if pg.key.get_pressed()[pg.K_j] or pg.key.get_pressed()[pg.K_SPACE]:
                    self.isJump = True
                    self.isIdle = False
                    self.walkC = 0
                    self.runC = 0
                    self.atckC = 0
                    self.atckUC = 0
            else:
                if self.jumpC >= -7:
                    n = 1
                    self.isUpR = True
                    self.isUpL = True
                    self.isDownR = False
                    self.isDownL = False
                    self.isIdle = False
                    if self.jumpC < 0:
                        n = -1
                        self.isDownR = True
                        self.isDownL = True
                        self.isUpR = False
                        self.isUpL = False
                        self.isIdle = False
                    self.pos.y -= ((self.jumpC ** 2) / 2) * n 
                    self.jumpC -= 1
                else: 
                    self.idle = 0
                    self.isJump = False
                    self.jumpC = 7
                    self.isIdle = True
                    self.isDownR = False
                    self.isUpR = False
                    self.isDownL = False
                    self.isUpL = False

    def animation(self):
        #Moving Right
        self.runR = (pg.image.load('../images/Ninja/R_run_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_run_2.png').convert_alpha(),pg.image.load('../images/Ninja/R_run_3.png').convert_alpha(),pg.image.load('../images/Ninja/R_run_4.png').convert_alpha(),pg.image.load('../images/Ninja/R_run_5.png').convert_alpha(),pg.image.load('../images/Ninja/R_run_6.png').convert_alpha())
        self.walkR = (pg.image.load('../images/Ninja/R_walk_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_walk_2.png').convert_alpha(),pg.image.load('../images/Ninja/R_walk_3.png').convert_alpha(),pg.image.load('../images/Ninja/R_walk_4.png').convert_alpha())
        self.ninR = (pg.image.load('../images/Ninja/R_idle_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_idle_2.png').convert_alpha())
        self.jumpR = (pg.image.load('../images/Ninja/R_jump.png').convert_alpha(),pg.image.load('../images/Ninja/R_land.png').convert_alpha())
    
        #Damage
        self.dead = (pg.image.load('../images/Ninja/R_death_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_death_2.png').convert_alpha(),pg.image.load('../images/Ninja/R_death_3.png').convert_alpha(),pg.image.load('../images/Ninja/R_death_4.png').convert_alpha(), pg.image.load('../images/Ninja/R_death_5.png').convert_alpha(), pg.image.load('../images/Ninja/R_death_6.png').convert_alpha(), pg.image.load('../images/Ninja/R_death_7.png').convert_alpha(), pg.image.load('../images/Ninja/R_death_8.png').convert_alpha())
        
        if not self.isDead:
            
            if not self.isIdle:
    
                if not self.isJump:
    
                    if not self.isAtck:
                            self.direction()
                    elif self.isAtck:
                        
                        self.attack()
         
                elif self.isJump:
                    self.jump()    
            elif self.isIdle:
                # self.idle()
                if self.isR or self.isRunR or self.isAtck: 
                    self.image = self.ninR[self.idle//7]
        
                if self.idle >= 13:
                    self.idle = 0
        elif self.isDead:
            self.dead()

 
    def attack(self):
        #Attacking Right
        self.lightAtckR = (pg.image.load('../images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_4.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_6.png').convert_alpha())
        self.medAtckR = (pg.image.load('../images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_5.png').convert_alpha())
        self.strngAtckR = (pg.image.load('../images/Ninja/R_attack_1.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_2.png').convert_alpha(),pg.image.load('../images/Ninja/R_attack_3.png').convert_alpha())
 
        #===========
        #ACTIONS
        #===========
        
        if self.atckIsK:          
            self.image = self.lightAtckR[self.atckC//1]
            self.rect = self.image.get_rect()
           
            self.atckC += 1
            if self.atckC >= 4:
                self.atckC = 0
                
        elif self.atckIsI:
            self.image = self.medAtckR[self.atckUC//1]
            self.rect = self.image.get_rect()
            
            self.atckUC += 1
            if self.atckUC >= 3:
                self.atckUC = 0
        
        elif self.atckIsL:
            self.image = self.strngAtckR[self.atckUC//1]
            self.rect = self.image.get_rect()
            
            self.atckUC += 1
            if self.atckUC >= 3:
                self.atckUC = 0
    ### NEW ###
    def direction(self):
        if self.isL :
            self.image = self.walkL[self.walkC//3]
            self.walkC += 1
            if self.walkC >= 12:
                self.walkC = 0
        elif self.isR: 
            self.image = self.walkR[self.walkC//3]
            self.walkC += 1
            if self.walkC >= 12:
                self.walkC = 0
        elif self.isRunL:
            self.image = self.runL[self.runC//2]
            self.runC += 1
            if self.runC >= 12:
                self.runC = 0
        elif self.isRunR:
            self.image = self.runR[self.runC//2]
            self.runC += 1
            if self.runC >= 12:
                self.runC = 0

    def jump(self):
        if self.isR or self.isRunR:               
            if self.isUpR:
                self.image = self.jumpR[0]
            elif self.isDownR:
                self.image = self.jumpR[1]
        elif self.isL or self.isRunL:               
            if self.isUpL:
                self.image = self.jumpL[0]
            elif self.isDownL:
                self.image = self.jumpL[1]

    def idle(self):
        if self.isR or self.isRunR or self.isAtck: 
            self.image = self.ninR[self.idle//7]
        elif self.isL or self.isRunL or self.isAtck: 
            self.image = self.ninL[self.idle//7]

        if self.idle >= 13:
            self.idle = 0

    def dead(self):
        self.image = self.dead[self.runC//2]
        self.image = self.dead[7]
        self.dthC += 1 * 2
        if self.dthC >= 16:
            self.dthC = 0