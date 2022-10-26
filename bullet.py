from re import X
from ship import Ship

class Bullet:
    
    def __init__(self):
        
        self.myship=Ship()
        self.condition= "STOP"        
        self.ybullet=self.shipy
        
    def shoot(self):
        if self.condition== "SHOOT":
            self.ybullet-=5
        elif self.ship.direction== "STOP":
            pass