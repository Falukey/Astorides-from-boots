import pygame
import constants
from circleshape import CircleShape
from shot import Shot
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.player_shot_cooldown = 0
    
        self.image = pygame.Surface((constants.PLAYER_RADIUS * 2, constants.PLAYER_RADIUS * 2))
        self.rect = self.image.get_rect(center=(x, y))
    def rotate_left(self, dt):
        self.rotation -= constants.PLAYER_TURN_SPEED * dt
    def rotate_right(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
    def forward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    def backward(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= forward * constants.PLAYER_SPEED * dt
    def shoot(self):
        
        shot_position = self.position
        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        shot_velocity *= constants.PLAYER_SHOT_SPEED

        
        new_shot = Shot(shot_position.x, shot_position.y, constants.SHOT_RADIUS)
        new_shot.velocity = shot_velocity
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.forward(dt)
        if keys[pygame.K_s]:
            self.backward(dt)
        if keys[pygame.K_a]:
            self.rotate_left(dt)
        if keys[pygame.K_d]:
            self.rotate_right(dt)
        if self.player_shot_cooldown > 0:
            self.player_shot_cooldown -= dt
        if self.player_shot_cooldown <= 0:
            if keys[pygame.K_SPACE]:
                self.shoot()
                self.player_shot_cooldown = 0.3

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    