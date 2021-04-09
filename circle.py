import random
import pygame

class Circle:
    def __init__(self,win,position,ratio):
        self.position = position
        self.win = win
        self.radius = 50
        self.color = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        self.ratio = ratio
        self.velocity = 1
        self.vector = (1,0)


    def draw(self,dt):
        self.update_position(dt)
        pygame.draw.circle(self.win,self.color,self.position,self.radius)

    def update_position(self,dt):
        old_x,old_y = self.position
        new_x = old_x + (self.vector[0] * self.velocity * self.ratio * dt)
        new_y = old_y + (self.vector[1] * self.velocity * self.ratio * dt)

        if new_x >= 800:
            
        if new_x <= 200:
            self.vector = (self.vector[0] * -1,self.vector[1])

        self.position = (new_x,new_y)
