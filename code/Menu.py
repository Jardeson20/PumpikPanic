import pygame
from code.Score import Score  # Importa a classe Score

class Menu:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("asset/zombie.ttf", 72)  # Fonte grande para o título
        self.small_font = pygame.font.Font("asset/zombie.ttf", 36)  # Fonte menor para os botões e textos
        self.menu_background = pygame.image.load("asset/menu.png")  # Carrega a imagem de fundo
        self.menu_sound = pygame.mixer.Sound("asset/menu_sound.wav")  # Carrega o som de fundo
        self.score_manager = Score()  # Instancia a classe Score

    def draw_button(self, text, position, action=None):
        # Desenha um botão na tela
        button_rect = pygame.Rect(position[0], position[1], 200, 50)  # Tamanho do botão
        pygame.draw.rect(self.window, (255, 165, 0), button_rect)  # Cor laranja
        button_text = self.small_font.render(text, True, (0, 0, 0))  # Texto preto
        text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, text_rect)

        # Verifica se o botão foi clicado
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if button_rect.collidepoint(mouse_pos) and mouse_click[0]:
            return action
        return None

    def show_scores(self):
        # Carrega as pontuações
        high_scores = self.score_manager.load_scores()

        while True:  # Loop do menu de pontuações
            # Desenha a imagem de fundo
            self.window.blit(self.menu_background, (0, 0))

            # Título "Melhores Pontuações" (centralizado na parte superior)
            title_text = self.font.render("Melhores Pontuações", True, (255, 165, 0))  # Cor laranja
            title_rect = title_text.get_rect(center=(self.window.get_width() // 2, 100))
            self.window.blit(title_text, title_rect)

            # Exibe as pontuações
            y_offset = 200  # Posição Y inicial para as pontuações
            for i, score in enumerate(high_scores):
                # Posição (em cor laranja)
                pos_text = self.small_font.render(f"{i + 1} -", True, (255, 165, 0))  # Cor laranja
                self.window.blit(pos_text, (self.window.get_width() // 2 - 200, y_offset))

                # Jogador (nome fictício, pois ainda não há sistema de nomes)
                player_text = self.small_font.render("Jogador", True, (255, 255, 255))  # Texto branco
                self.window.blit(player_text, (self.window.get_width() // 2 - 50, y_offset))

                # Pontuação (texto branco)
                score_text = self.small_font.render(f"{score}", True, (255, 255, 255))  # Texto branco
                self.window.blit(score_text, (self.window.get_width() // 2 + 150, y_offset))

                y_offset += 50  # Avança para a próxima linha

            # Botão "Voltar" (centralizado abaixo das pontuações)
            if self.draw_button("Voltar", (self.window.get_width() // 2 - 100, y_offset + 50), "menu"):
                return  # Retorna ao menu principal

            # Atualiza a tela
            pygame.display.update()

            # Processa os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_sound.stop()  # Para o som de fundo
                    pygame.quit()
                    return "quit"  # Fecha o jogo

    def run(self):
        # Reproduz o som de fundo do menu
        self.menu_sound.play(-1)  # -1 faz o som repetir em loop

        while True:
            # Desenha a imagem de fundo
            self.window.blit(self.menu_background, (0, 0))

            # Exibe o nome do jogo
            title_text_pumpik = self.font.render("Pumpik", True, (255, 165, 0))  # Cor laranja
            title_rect_pumpik = title_text_pumpik.get_rect(center=(self.window.get_width() // 2, 100))
            self.window.blit(title_text_pumpik, title_rect_pumpik)

            title_text_panic = self.font.render("Panic", True, (255, 165, 0))  # Cor laranja
            title_rect_panic = title_text_panic.get_rect(center=(self.window.get_width() // 2, 150))
            self.window.blit(title_text_panic, title_rect_panic)

            # Exibe as opções do menu como botões
            start_action = self.draw_button("Iniciar Jogo", (self.window.get_width() // 2 - 100, 250), "start")
            score_action = self.draw_button("Score", (self.window.get_width() // 2 - 100, 320), "score")
            quit_action = self.draw_button("Sair", (self.window.get_width() // 2 - 100, 390), "quit")

            # Verifica se algum botão foi clicado
            if start_action:
                return "start"
            if score_action:
                self.show_scores()  # Exibe o menu de pontuações
            if quit_action:
                return "quit"

            # Atualiza a tela
            pygame.display.update()

            # Processa os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.menu_sound.stop()  # Para o som de fundo
                    pygame.quit()
                    return "quit"

            # Controla o FPS
            self.clock.tick(60)