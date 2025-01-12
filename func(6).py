import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)  # White color
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def main():

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-1, 1, -1, 1)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_line(-0.5, -0.5, 0.5, 0.5)  
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()