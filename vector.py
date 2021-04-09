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

VECTOR = (1,1)
VELOCITY = 10

def draw_window(new_location):
    WIN.fill(WHITE)
    pygame.draw.circle(WIN,BLACK,new_location,CIRCLE_RAD)
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
    location = (100,100)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        location = update_circle_pos(location)
        draw_window(location)

    pygame.quit()

if __name__ == "__main__":
    main()

