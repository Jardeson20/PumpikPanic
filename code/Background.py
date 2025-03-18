import pygame

class Background:
    def __init__(self, window):
        self.window = window
        self.images = [
            pygame.image.load("asset/background_1.png"),
            pygame.image.load("asset/background_2.png"),
            pygame.image.load("asset/background_3.png")
        ]
        self.current_image = 0  # Índice da imagem atual
        self.x = 0  # Posição horizontal do fundo

    def update(self, score):
        # Alterna o fundo conforme a pontuação
        if score >= 10 and self.current_image == 0:
            self.current_image = 1
        elif score >= 20 and self.current_image == 1:
            self.current_image = 2

    def draw(self):
        # Desenha o fundo na tela
        self.window.blit(self.images[self.current_image], (self.x, 0))