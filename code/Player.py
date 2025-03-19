import pygame

class Player:
    def __init__(self, window):
        self.window = window
        self.original_image = pygame.image.load("asset/pumpik_icon.png")  # Carrega a imagem original
        self.image = pygame.transform.scale(self.original_image, (80, 80))  # Redimensiona a imagem para 80x80 pixels
        self.rect = self.image.get_rect(center=(100, window.get_height() // 2))  # Posição inicial
        self.velocity = 0  # Velocidade vertical do jogador
        self.gravity = 0.5  # Força da gravidade
        self.hitbox = pygame.Rect(0, 0, 60, 60)  # Hitbox ajustada
        self.update_hitbox()  # Atualiza a posição da hitbox

    def update_hitbox(self):
        # Centraliza a hitbox no personagem
        self.hitbox.center = self.rect.center

    def move(self):
        # Aplica a gravidade ao jogador
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # Impede que o jogador saia da tela (parte superior e inferior)
        if self.rect.top < 0:  # Limite superior
            self.rect.top = 0
            self.velocity = 0
        if self.rect.bottom > self.window.get_height():  # Limite inferior
            self.rect.bottom = self.window.get_height()
            self.velocity = 0

        # Atualiza a hitbox após o movimento
        self.update_hitbox()

    def jump(self):
        # Faz o jogador pular
        self.velocity = -10  # Ajuste a força do pulo conforme necessário

    def draw(self):
        # Desenha o jogador na tela
        self.window.blit(self.image, self.rect)
        # Desenha a hitbox (opcional, para debug)
        # pygame.draw.rect(self.window, (255, 0, 0), self.hitbox, 2)