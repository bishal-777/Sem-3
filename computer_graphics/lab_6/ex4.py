import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1600, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cycle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =(255,0,0)
BLUE=(0,0,255)
# Function 
def cycle(tx):
    #road
    pygame.draw.line(screen, BLACK,(0,1000),(1600,1000),2)
    #wheels of cycle
    pygame.draw.circle(screen, BLACK,(100+tx,950),50)
    pygame.draw.circle(screen, BLACK,(300+tx,950),50)
    #Chasis frame of cycle
    pygame.draw.line(screen, RED,(100+tx,950),(200+tx,950),7)
    pygame.draw.line(screen, RED,(100+tx,950),(150+tx,850),7)
    pygame.draw.line(screen, RED,(200+tx,950),(250+tx,850),7)
    pygame.draw.line(screen, RED,(300+tx,950),(250+tx,850),7)
    pygame.draw.line(screen, RED,(150+tx,850),(250+tx,850),7)
    pygame.draw.line(screen, RED,(100+tx,950),(330+tx,800),7)
    pygame.draw.line(screen, RED,(150+tx,850),(100+tx,825),7)
    #seat of cycle
    pygame.draw.line(screen, BLUE,(75+tx,825),(125+tx,825),7)





# Main loop
def main():
    tx=0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(WHITE)
        #function call
        cycle(tx)
        tx+=1
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
