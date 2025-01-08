import pygame
import math as m
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1600, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =(255,0,0)
BLUE=(0,0,255)
# Function 
def cycle(x):
       #road
       pygame.draw.line(screen, WHITE,(0,1000),(1600,1000),2)
       #wheels of cycle
       pygame.draw.circle(screen, WHITE,(100,950),50)
       pygame.draw.circle(screen, WHITE,(300,950),50)
       #Chasis frame of cycle
       pygame.draw.line(screen, RED,(100,950),(200,950),7)
       pygame.draw.line(screen, RED,(100,950),(150,850),7)
       pygame.draw.line(screen, RED,(200,950),(250,850),7)
       pygame.draw.line(screen, RED,(300,950),(250,850),7)
       pygame.draw.line(screen, RED,(150,850),(250,850),7)
       pygame.draw.line(screen, RED,(100,950),(330,800),7)
       pygame.draw.line(screen, RED,(150,850),(100,825),7)
       #seat of cycle
       pygame.draw.line(screen, BLUE,(75,825),(125,825),7)




# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)
        #function call
        cycle(5)
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
