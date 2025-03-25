import pygame
import random

class Obstacle:
    def __init__(self, window):
        self.window = window
        self.original_image = pygame.image.load("asset/obstacle.png")
        self.image = pygame.transform.scale(self.original_image, (100, 250))
        self.gap = 250
        self.speed = 5
        self.obstacles = []

    def create_obstacle(self):
        obstacle_height = random.randint(100, 400)
        obstacle_top = pygame.transform.flip(self.image, False, True)
        obstacle_top_rect = obstacle_top.get_rect(midbottom=(self.window.get_width(), obstacle_height))
        obstacle_bottom_rect = self.image.get_rect(midtop=(self.window.get_width(), obstacle_height + self.gap))
        self.obstacles.append((obstacle_top, obstacle_top_rect, self.image, obstacle_bottom_rect))

    def move_obstacles(self):
        for obstacle in self.obstacles:
            obstacle[1].x -= self.speed
            obstacle[3].x -= self.speed

        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle[1].right > 0]

    def draw_obstacles(self):
        for obstacle in self.obstacles:
            self.window.blit(obstacle[0], obstacle[1])
            self.window.blit(obstacle[2], obstacle[3])

    def check_collision(self, player_rect):
        for obstacle in self.obstacles:
            if player_rect.colliderect(obstacle[1]) or player_rect.colliderect(obstacle[3]):
                return True
        return False

    def update(self):
        self.move_obstacles()
        if len(self.obstacles) == 0 or self.obstacles[-1][1].x < self.window.get_width() - 300:
            self.create_obstacle()