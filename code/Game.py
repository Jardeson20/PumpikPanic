import pygame
from code.Player import Player
from code.Background import Background
from code.Obstacle import Obstacle
from code.Score import Score

class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.score = 0
        self.player = Player(window)
        self.background = Background(window)
        self.obstacle = Obstacle(window)
        self.game_sound = pygame.mixer.Sound("asset/game_sound.wav")
        self.finish_sound = pygame.mixer.Sound("asset/finishGame_sound.wav")
        self.font = pygame.font.Font("asset/zombie.ttf", 42)
        self.passed_obstacles = set()
        self.score_manager = Score()

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (10, 10))

    def game_over(self):
        self.game_sound.stop()

        self.finish_sound.play()

        self.score_manager.save_score(self.score)

        font = pygame.font.Font("asset/zombie.ttf", 92)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))

        self.background.draw()
        self.player.draw()

        self.window.blit(game_over_text, game_over_rect)

        pygame.display.update()

        pygame.time.delay(4000)

        return "menu"

    def run(self):
        self.game_sound.play(-1)

        while True:
            self.window.fill((0, 0, 0))

            self.background.update(self.score)

            self.background.draw()

            self.player.move()

            if self.player.rect.bottom >= self.window.get_height():
                return self.game_over()

            self.obstacle.update()

            if self.obstacle.check_collision(self.player.rect):
                return self.game_over()

            for obs in self.obstacle.obstacles:
                obstacle_id = id(obs)
                if obs[1].right < self.player.rect.left and obstacle_id not in self.passed_obstacles:
                    self.score +=1
                    self.passed_obstacles.add(obstacle_id)
                    print(f"Pontuação: {self.score}")

            self.obstacle.draw_obstacles()

            self.player.draw()

            self.draw_score()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_sound.stop()
                    pygame.quit()
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                    if event.key == pygame.K_ESCAPE:
                        self.game_sound.stop()
                        return "menu"

            self.clock.tick(60)