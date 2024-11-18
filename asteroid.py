import pygame
import constants
import random
from circleshape import CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        random_angle = random.uniform(0, 360)
        random_speed_value = random.uniform(constants.MIN_SPEED, constants.MAX_SPEED)
        
        random_direction = pygame.Vector2(1, 0).rotate(random_angle)
        self.velocity = random_direction * random_speed_value
    
    def draw(self, screen):
        some_color = (255, 255, 255) 
        pygame.draw.circle(screen, some_color, (int(self.position.x), int(self.position.y)), self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
       
        if self.position.x > constants.SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = constants.SCREEN_WIDTH

        if self.position.y > constants.SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = constants.SCREEN_HEIGHT
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return "small asteroid"
        # Rotate the current velocity
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        # Create two new asteroids at the current position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
       
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2
        group_drawable = pygame.sprite.Group()
        group_updatable = pygame.sprite.Group()
        group_asteroid = pygame.sprite.Group()
        group_drawable.add(asteroid1, asteroid2)
        group_updatable.add(asteroid1, asteroid2)
        group_asteroid.add(asteroid1, asteroid2)