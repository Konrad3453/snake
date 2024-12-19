import pygame
import random
from fruits import Fruit
from constants import *

class Field(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position):
     
        fruit = Fruit(position.x, position.y, radius)

        fruit.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > 1:
            self.spawn_timer = 0

  
            position = pygame.Vector2(
                random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_HEIGHT)
            )
            
 
            self.spawn(20, position) 