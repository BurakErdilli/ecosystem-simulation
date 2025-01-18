from entity import Predator, Prey, Plant
import pygame

class Simulation:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.entities = []

    def add_entity(self, entity_type, x, y):
        if entity_type == "predator":
            self.entities.append(Predator(x, y))
        elif entity_type == "prey":
            self.entities.append(Prey(x, y))
        elif entity_type == "plant":
            self.entities.append(Plant(x, y))

    def update(self):
        for entity in self.entities:
            entity.update(self.entities)

    def render(self, screen):
        screen.fill((0, 0, 0))  # Black background
        for entity in self.entities:
            entity.render(screen)
        pygame.display.flip()
