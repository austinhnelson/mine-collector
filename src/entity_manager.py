import pygame


class Entity_Manager:
    def __init__(self):
        self.entities = pygame.sprite.Group()

    def add_entity(self, entity):
        self.entities.add(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def update(self):
        self.entities.update()

    def draw(self, surface):
        self.entities.draw(surface)
