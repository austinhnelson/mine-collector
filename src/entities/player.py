from entities.entity import Entity
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Load the entire sprite sheet
        sprite_sheet = pygame.image.load("assets/images/player/default_character.png")

        # Define a rectangle that specifies the area of the sprite you want to extract
        # (x, y, width, height) - Adjust these values to match your specific sprite
        sprite_rect = pygame.Rect(0, 0, 50, 50)

        # Extract the specific sprite from the sprite sheet
        self.image = sprite_sheet.subsurface(sprite_rect)

        self.rect = self.image.get_rect()
