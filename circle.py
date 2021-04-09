import random
import pygame
import math

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


    def draw(self,time_since_start):
        self.update_position(time_since_start)
        pygame.draw.circle(self.win,self.color,self.position,self.radius)

    def update_position(self,time_since_start):
        b = (2 * math.pi)/self.velocity
        a = 600
        x = time_since_start
        c = 0
        d = 500
        self.position =  (a * math.sin(b * (x + c)) + d,self.position[1])
        print(self.position[0])

