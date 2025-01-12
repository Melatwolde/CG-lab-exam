import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("lab exam")
    screen.fill((255, 255, 255))
    
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    
    start = (50, 50)
    end = (250, 50)
    pygame.draw.line(screen, RED, start, end, 3)
    
   
    blue= [(250, 50), (100, 350), (400, 350)]
    pygame.draw.polygon(screen, BLUE, blue)
    
   
    white= [(250, 270), (150, 150), (350, 150)]
    pygame.draw.polygon(screen, WHITE, white)
    
 
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()