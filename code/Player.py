import pygame

class Player:
    def __init__(self, window):
        self.window = window
        self.original_image = pygame.image.load("asset/pumpik_icon.png")
        self.image = pygame.transform.scale(self.original_image, (80, 80))
        self.rect = self.image.get_rect(center=(100, window.get_height() // 2))
        self.velocity = 0
        self.gravity = 0.5
        self.hitbox = pygame.Rect(10, 10, 50, 50)
        self.update_hitbox()

    def update_hitbox(self):
        self.hitbox.center = self.rect.center

    def move(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.top < 0:
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > self.window.get_height():
            self.rect.bottom = self.window.get_height()
            self.velocity = 0

        self.update_hitbox()

    def jump(self):
        self.velocity = -10

    def draw(self):
        self.window.blit(self.image, self.rect)