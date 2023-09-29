import pygame
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from entity_manager import Entity_Manager
from entities.player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mine collector")
clock = pygame.time.Clock()

# Creating players and manager
entity_manager = Entity_Manager()  # Fixed the typo here
player1 = Player(50, 50)

entity_manager.add_entity(player1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    entity_manager.update()
    entity_manager.draw(screen)  # Fixed the typo here

    pygame.display.flip()

    clock.tick(60)

pygame.quit()  # Fixed the missing parentheses
