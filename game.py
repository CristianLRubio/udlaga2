from sky import Sky
from ship import Ship
from bullet import Bullet
import pygame
import random

class Game:

    def __init__(self):
        
        self.width=400
        self.height=400
        self.mySky=Sky(self.width, self.height, 50)
        self.screen= pygame.display.set_mode((self.width, self.height))
        self.clock= pygame.time.Clock()
        self.fps=60
        #cargar la hoja de imagenes
        self.sprites= pygame.image.load("galaga.png")      
        self.shipsprites= pygame.Surface((64,64)).convert()
        self.shipsprites.blit(self.sprites, (0,0), (250,436, 64,64))
        self.myShip=Ship()
        #self.mybullet=Bullet()
        
        
    def run(self):
        pygame.init()
        
        control=True
        while control:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            
            self.screen.fill((0,0,0))
            
            #show the sky
            for start in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen,(r,g,b), start, 1)
            self.mySky.move()
            x=self.myShip.move(self.checkKeys())
            y=100
            self.screen.blit(self.shipsprites, (x,y))
            pygame.display.flip()
            self.clock.tick(self.fps)

    def checkKeys(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            return "LETF"
        if keys[pygame.K_RIGHT]:
            return "RIGHT"

myGame=Game()
myGame.run()        
    