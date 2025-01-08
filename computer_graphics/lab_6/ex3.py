import pygame
import math as m
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED =(255,0,0)
# Function 
def line(x1,y1,x2,y2,theta):
        theta*=(3.14/180)
        xr1=int(x1*m.cos(theta)-y1*m.sin(theta))
        yr1=int(x1*m.sin(theta)+y1*m.cos(theta))
        xr2=int(x2*m.cos(theta)-y2*m.sin(theta))
        yr2=int(x2*m.sin(theta)+y2*m.cos(theta))

        pygame.draw.line(screen, WHITE,(x1,y1),(x2,y2),2)
        pygame.draw.line(screen, RED,(xr1,yr1),(xr2,yr2),2)
        




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
        line(100,100,100,800,-60)# theta=-60

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
