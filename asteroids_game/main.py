import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
import player

def main():
    #print(f"Starting Asteroids")
   # print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    deltaTime = 0.0
    p1 = player.Player(SCREEN_WIDTH/ 2,SCREEN_HEIGHT/ 2)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        p1.update(deltaTime)
        screen.fill("black")
        p1.draw(screen)
        pygame.display.flip()
        deltaTime = clock.tick(60) / 1000
        #print(deltaTime)


if __name__ == "__main__":
    main()
