import pygame
import constants
from circleshape import CircleShape
class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = velocity

    def update(self, dt):
        # Update the position based on the velocity
        self.position += self.velocity * dt
       

    def draw(self, screen):
        some_color = (0, 255, 255) 
        pygame.draw.circle(screen, some_color, (int(self.position.x), int(self.position.y)), self.radius)

    def out_of_bounds(self):
        return (self.position.x < 0 or
                self.position.x > constants.SCREEN_WIDTH or
                self.position.y < 0 or
                self.position.y > constants.SCREEN_HEIGHT)

    def destroy(self):
        # Implement logic to remove the shot from the game (e.g., from a group or list)
        pass