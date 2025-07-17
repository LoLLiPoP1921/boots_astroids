from constants import *
from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, position, rotation):
        super().__init__(position.x, position.y,SHOT_RADIUS)
        self.rotation = rotation
        self.position = position.copy()
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", tuple(self.position), SHOT_RADIUS, 2)
        