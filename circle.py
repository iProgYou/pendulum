import random
import pygame
import math



class Circle:
    def __init__(self,win,position,ratio,sound):
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
        self.sound = sound
        self.right = True



    def draw(self,time_since_start):
        self.update_position(time_since_start)
        pygame.draw.circle(self.win,self.color,self.position,self.radius)

    def update_position(self,time_since_start):
        b = (2 * math.pi)/(self.velocity * (1 / self.ratio))
        a = 300
        x = time_since_start / 200
        c = 0
        d = 500

        new_pos = (a * math.sin(b * (x + c)) + d,self.position[1])
        dir = self.position[0] - new_pos[0]
        # if dir is > 0 (traveling left) and self.right == true, flip
        if dir > 0 and self.right:
            self.right = False
        elif dir < 0 and not self.right:
            self.sound.play()
            self.right = True
        self.position =  new_pos

