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
        self.scroll_speed = 2  # Velocidade de movimento do fundo

    def update(self, score):
        # Alterna o fundo conforme a pontuação
        if score >= 10 and self.current_image == 0:
            self.current_image = 1
        elif score >= 20 and self.current_image == 1:
            self.current_image = 2

        # Move o fundo para a esquerda
        self.x -= self.scroll_speed

        # Reseta a posição do fundo quando ele sair completamente da tela
        if self.x <= -self.window.get_width():
            self.x = 0

    def draw(self):
        # Desenha o fundo na tela
        self.window.blit(self.images[self.current_image], (self.x, 0))
        # Desenha uma segunda cópia do fundo para criar o efeito de scroll contínuo
        self.window.blit(self.images[self.current_image], (self.x + self.window.get_width(), 0))