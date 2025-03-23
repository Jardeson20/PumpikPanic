import pygame
import random

class Obstacle:
    def __init__(self, window):
        self.window = window
        self.original_image = pygame.image.load("asset/obstacle.png")  # Carrega a imagem original da vassoura
        self.image = pygame.transform.scale(self.original_image, (100, 250))  # Redimensiona a vassoura (largura, altura)
        self.gap = 250  # Espaço entre as vassouras (ajuste conforme necessário)
        self.speed = 5  # Velocidade de movimento das vassouras
        self.obstacles = []  # Lista para armazenar os pares de vassouras

    def create_obstacle(self):
        # Gera um novo par de vassouras (uma em cima e uma embaixo)
        obstacle_height = random.randint(100, 400)  # Altura aleatória para a vassoura de cima
        obstacle_top = pygame.transform.flip(self.image, False, True)  # Inverte a imagem para a vassoura de cima
        obstacle_top_rect = obstacle_top.get_rect(midbottom=(self.window.get_width(), obstacle_height))
        obstacle_bottom_rect = self.image.get_rect(midtop=(self.window.get_width(), obstacle_height + self.gap))
        self.obstacles.append((obstacle_top, obstacle_top_rect, self.image, obstacle_bottom_rect))

    def move_obstacles(self):
        # Move as vassouras para a esquerda
        for obstacle in self.obstacles:
            obstacle[1].x -= self.speed  # Move a vassoura de cima
            obstacle[3].x -= self.speed  # Move a vassoura de baixo

        # Remove as vassouras que saíram da tela
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle[1].right > 0]

    def draw_obstacles(self):
        # Desenha as vassouras na tela
        for obstacle in self.obstacles:
            self.window.blit(obstacle[0], obstacle[1])  # Desenha a vassoura de cima
            self.window.blit(obstacle[2], obstacle[3])  # Desenha a vassoura de baixo

    def check_collision(self, player_rect):
        # Verifica colisão entre o jogador e as vassouras
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle[1]) or player_rect.colliderect(obstacle[3]):
                return True  # Colisão detectada
        return False  # Sem colisão

    def update(self):
        # Atualiza as vassouras (movimento e geração)
        self.move_obstacles()
        if len(self.obstacles) == 0 or self.obstacles[-1][1].x < self.window.get_width() - 300:
            self.create_obstacle()  # Gera um novo par de vassouras