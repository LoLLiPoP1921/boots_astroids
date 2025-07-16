import pygame
from constants import *

def main():
    
    pygame.init
    print("'Starting Asteroids!'")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameExit = False
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        screen.fill(SCREEN_COLOR)
        pygame.display.update()

if __name__ == "__main__":
    main()
