import pygame
from constants import *

def main():
    
    pygame.init
    print("'Starting Asteroids!'")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameExit = False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(SCREEN_COLOR)
        
        
        
        
        pygame.display.flip()
        dt = clock.tick(60)

if __name__ == "__main__":
    main()
