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
        self.line_pos = [*self.position]
        self.change_colors = False

    def draw_line(self):
        line_pos_start = (self.line_pos[0] - 50,self.line_pos[1] - 50)
        line_pos_end = (self.line_pos[0] - 50,self.line_pos[1] + 50)
        if self.change_colors:
            pygame.draw.line(self.win,self.color,line_pos_start,line_pos_end,5)
        else:
            pygame.draw.line(self.win,(0,0,0),line_pos_start,line_pos_end,5)
            


    def draw(self,time_since_start):
        self.update_position(time_since_start)
        self.draw_line()
        pygame.draw.circle(self.win,self.color,self.position,self.radius)

    def update_position(self,time_since_start):
        b = (2 * math.pi)/(self.velocity * (1 / self.ratio))
        a = 300
        x = time_since_start / 200
        c = 0
        d = 500

        new_pos = (a * math.sin(b * (x + c)) + d,self.position[1])
        dir = self.position[0] - new_pos[0]

        if new_pos[0] > 300:
            self.change_colors = False

        if dir >= 0 and self.right:
            self.right = False
        elif dir <= 0 and not self.right:
            self.sound.play()
            self.right = True
            self.change_colors = True
        self.position =  new_pos

