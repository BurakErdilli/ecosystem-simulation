import pygame
import math

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def update(self, objects):
        pass

    def render(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 5)

class Predator(Entity):
    def render(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 10)

class Prey(Entity):
    def render(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (int(self.x), int(self.y)), 8)

class Plant(Entity):
    def render(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 5)
