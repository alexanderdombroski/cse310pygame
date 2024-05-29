import pygame
from globals import all_sprites, all_walls

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, x: int, y: int, height: int, width: int, color: tuple[int, int, int] = (0, 255, 0)):
        super().__init__(all_sprites, all_walls) # Add to the sprite groups

        # Properties
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        

    def draw(self, surface: pygame.surface) -> None:
        surface.blit(self.image, self.rect)

    def collides_with(self, other_sprite) -> bool:
        return pygame.sprite.collide_rect(self, other_sprite)
    
class BreakableWall (Wall):

    def __init__(self, x: int, y: int, width: int, height: int, 
            health: int, color: tuple[int, int, int] = (255, 0, 0)) -> None:
        super().__init__(x, y, width, height, color)
        self.health = health
        
    
    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.kill()

