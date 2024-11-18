import pygame
import time
from asteroidfield import AsteroidField
from player import Player
from constants import *
from asteroid import Asteroid
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    group_drawable = pygame.sprite.Group()
    group_updatable = pygame.sprite.Group()
    group_asteroid = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (group_drawable, group_updatable)
    AsteroidField.containers = (group_updatable)
    Asteroid.containers = (group_asteroid, group_drawable, group_updatable)
    Shot.containers = (shots_group, group_drawable, group_updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True
    
    while running:
        dt = clock.tick(60) / 1000
        screen.fill((0, 0, 0))
        for sprite in group_updatable:
            sprite.update(dt)

        for sprite in group_drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for shot in shots_group:
                for asteroid in group_asteroid:
                    if shot.collision(asteroid):  # Pass the asteroid to collision method
                        asteroid.split()
                        shot.kill()
            for asteroid in group_asteroid:
                if player.collision(asteroid):
                    print("Game over!")
                    running = False
if __name__ == "__main__":
    main()