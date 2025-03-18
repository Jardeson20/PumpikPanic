import pygame
from code.Player import Player
from code.Background import Background

class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.score = 0
        self.player = Player(window)  # Cria o jogador
        self.background = Background(window)  # Cria o fundo
        self.game_sound = pygame.mixer.Sound("asset/game_sound.wav")  # Carrega o som de fundo
        self.finish_sound = pygame.mixer.Sound("asset/finishGame_sound.wav")  # Carrega o som de fim de jogo

    def game_over(self):
        # Para a música de fundo do jogo
        self.game_sound.stop()

        # Toca o som de fim de jogo
        self.finish_sound.play()

        # Congela a tela e exibe "Game Over"
        font = pygame.font.Font("asset/zombie.ttf", 72)  # Fonte para "Game Over"
        game_over_text = font.render("Game Over", True, (255, 0, 0))  # Texto vermelho
        game_over_rect = game_over_text.get_rect(center=(self.window.get_width() // 2, self.window.get_height() // 2))

        # Desenha o fundo e o jogador na tela congelada
        self.background.draw()
        self.player.draw()

        # Desenha o texto "Game Over"
        self.window.blit(game_over_text, game_over_rect)

        # Atualiza a tela
        pygame.display.update()

        # Aguarda 3 segundos antes de retornar ao menu
        pygame.time.delay(3000)

        # Retorna ao menu
        return "menu"

    def run(self):
        # Toca a música de fundo
        self.game_sound.play(-1)  # -1 faz a música repetir em loop

        # Loop principal do jogo
        while True:
            # Limpa a tela
            self.window.fill((0, 0, 0))  # Preenche a tela com preto

            # Atualiza o fundo
            self.background.update(self.score)

            # Desenha o fundo
            self.background.draw()

            # Atualiza o jogador
            self.player.move()

            # Verifica se o jogador tocou no chão
            if self.player.rect.bottom >= self.window.get_height():
                return self.game_over()  # Chama a função game_over

            # Desenha o jogador
            self.player.draw()

            # Atualiza a tela
            pygame.display.update()

            # Processa os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_sound.stop()  # Para a música de fundo
                    pygame.quit()
                    return "quit"  # Retorna "quit" para fechar o jogo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()  # Faz o jogador pular
                    if event.key == pygame.K_ESCAPE:
                        self.game_sound.stop()  # Para a música de fundo
                        return "menu"  # Retorna "menu" para voltar ao menu

            # Controla o FPS
            self.clock.tick(60)