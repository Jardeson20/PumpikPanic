import pygame

class Background:
    def __init__(self, window):
        self.window = window
        self.images = [
            pygame.image.load("asset/background_1.png"),
            pygame.image.load("asset/background_2.png"),
            pygame.image.load("asset/background_3.png")
        ]
        self.current_image = 0
        self.x = 0
        self.scroll_speed = 2

    def update(self, score):
        if score >= 10 and self.current_image == 0:
            self.current_image = 1
        elif score >= 20 and self.current_image == 1:
            self.current_image = 2

        self.x -= self.scroll_speed

        if self.x <= -self.window.get_width():
            self.x = 0

    def draw(self):
        self.window.blit(self.images[self.current_image], (self.x, 0))
        self.window.blit(self.images[self.current_image], (self.x + self.window.get_width(), 0))