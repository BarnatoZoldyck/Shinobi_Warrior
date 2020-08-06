import pygame as pg

class Env:
    def __init__(self):
    #initialize game window, etc
        pg.init()
        pg.mixer.init()
        #dimension of window
        self.windowWidth = 500
        self.windowLength = 281
        #window set-up
        self.screen = pg.display.set_mode(size=(self.windowWidth, self.windowLength))
        pg.display.set_caption("Shinobi Warrior")
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = False
        self.background_no = 1
        self.score = 0
        self.last_update = 0
        self.font = pg.font.Font('../fonts/Bank_Gothic_Medium_BT.ttf', 20)
        self.font2 = pg.font.Font('../fonts/Bank_Gothic_Medium_BT.ttf', 15)
    