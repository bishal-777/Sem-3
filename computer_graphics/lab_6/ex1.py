import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Translation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function 
def line(x1,y1,x2,y2,tx,ty):
   pygame.draw.line(screen,WHITE,(x1,y1),(x2,y2),2) 
   pygame.draw.line(screen,WHITE,(x1+tx,y1+ty),(x2+tx,y2+ty),2) 

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
        line(100,100,700,500,300,400)# tx,ty=200,300

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
