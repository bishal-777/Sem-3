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
    dx=x2-x1
    dy=y2-y1

    if abs(dx)>abs(dy):
        steps=abs(dx)
    else:
        steps=abs(dy)

    x_inc=dx/steps
    y_inc=dy/steps

    x,y=x1,y1

    for _ in range(steps):
        pygame.draw.circle(screen,WHITE,(round(x),round(y)),1)#(surface,color,centre_of_circle,radius)
        pygame.draw.circle(screen,WHITE,(round(x*sx),round(y*sy)),1)
        x+=x_inc
        y+=y_inc
   




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
        line(100,100,100,800,2,3)# sx,sy=2,3

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
