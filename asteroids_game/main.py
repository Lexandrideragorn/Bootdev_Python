import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #print(f"Starting Asteroids")
   # print(f"Screen width: {constants.SCREEN_WIDTH}")
    #print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    deltaTime = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    p1 = Player(SCREEN_WIDTH/ 2,SCREEN_HEIGHT/ 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #p1.update(deltaTime)
        updatable.update(deltaTime)
        screen.fill("black")
        #p1.draw(screen)
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        deltaTime = clock.tick(60) / 1000
        #print(deltaTime)


if __name__ == "__main__":
    main()
