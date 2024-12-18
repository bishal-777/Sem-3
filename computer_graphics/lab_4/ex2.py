#This program make a circluar structure by overlapping multiple circle
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1200, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function 
def draw_circle(xc,yc,r):
    x,y=0,r

    p=1-r

    while(x<=y):

        screen.set_at((x+xc,y+yc),WHITE)
        screen.set_at((y+xc,x+yc),WHITE)
        screen.set_at((x+xc,-y+yc),WHITE)
        screen.set_at((y+xc,-x+yc),WHITE)
        screen.set_at((-y+xc,x+yc),WHITE)
        screen.set_at((-x+xc,-y+yc),WHITE)
        screen.set_at((-y+xc,-x+yc),WHITE)
        screen.set_at((-x+xc,y+yc),WHITE)
        x+=1

        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*x-2*y+1




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
        draw_circle(600,200,100)
        draw_circle(450,250,100)
        draw_circle(750,250,100)
        draw_circle(450,400,100)
        draw_circle(750,400,100)
        draw_circle(600,450,100)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
