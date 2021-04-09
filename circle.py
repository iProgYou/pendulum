import random
import pygame

class Circle:
    def __init__(self,win,position,ratio):
        self.position = position
        self.win = win
        self.radius = 50
        self.color = (
            random.randint(0,256),
            random.randint(0,256),
            random.randint(0,256)
        )
        self.ratio = ratio
        self.velocity = 2
        self.vector = (1,0)


    def draw(self):
        self.update_position()
        pygame.draw.circle(self.win,self.color,self.position,self.radius)

    def update_position(self):
        old_x,old_y = self.position
        new_x = old_x + (self.vector[0] * self.velocity * self.ratio)
        new_y = old_y + (self.vector[1] * self.velocity * self.ratio)

        if new_x >= 800 or new_x <= 200:
            self.vector = (self.vector[0] * -1,self.vector[1])

        self.position = (new_x,new_y)
