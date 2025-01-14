import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scaling")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function 
def line(x1,y1,x2,y2,sx,sy):
   pygame.draw.line(screen,WHITE,(x1,y1),(x2,y2),2)
   pygame.draw.line(screen,WHITE,(x1*sx,y1*sy),(x2*sx,y2*sy),2) 

 



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
        line(100,100,100,200,2,3)# sx,sy=2,3

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
