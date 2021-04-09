import pygame
import circle

pygame.init()

WIDTH,HEIGHT = 1000,1000

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.display.set_caption("Pendulum?")


# ratios = [
#     2,
#     1.77777777777,
#     1.58024691358,
#     1.5,
#     1.33333333333,
#     1.18518518518,
#     1.0534979424,
#     1
# ]
# one_div_6 = 1/7
ratios = [2 - (1/7 * i) for i in range(0,8)]
print(ratios)
VECTOR = (1,0)
VELOCITY = 10

def draw_window(circles,time_since_start):
    WIN.fill(WHITE)
    for circle in circles:
        circle.draw(time_since_start)
    pygame.display.update()

def main():
    circles = [circle.Circle(WIN,(200,i * 110),ratios[i - 1]) for i in range(1,9)]
    counter = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        time_since_start = counter
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window(circles,time_since_start)
        counter += 1

    pygame.quit()

if __name__ == "__main__":
    main()

