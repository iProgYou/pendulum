import pygame

pygame.init()

WIDTH,HEIGHT = 1000,1000

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.display.set_caption("Pendulum?")

CIRCLE_RAD = 50
STARTING_LOCATION = (100,100)

circle_locations = [(500,i * 110) for i in range(1,9)]
ratios = [
    2,
    1.77777777777,
    1.58024691358,
    1.5,
    1.33333333333,
    1.18518518518,
    1.0534979424,
    1
]

VECTOR = (1,0)
VELOCITY = 10

def draw_window(circle_locations):
    WIN.fill(WHITE)
    for loc in circle_locations:
        pygame.draw.circle(WIN,BLACK,loc,CIRCLE_RAD)
    pygame.display.update()

def update_circle_pos(location):
    old_y,old_x = location
    new_y = old_y + (VECTOR[0] * VELOCITY)
    new_x = old_x + (VECTOR[1] * VELOCITY)
    new_location = (new_y,new_x)
    print(new_location)
    
    return new_location

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # location = update_circle_pos(location)
        draw_window(circle_locations)

    pygame.quit()

if __name__ == "__main__":
    main()

