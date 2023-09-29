import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.move_ip(self.velocity)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
