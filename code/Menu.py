import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("asset/zombie.ttf", 72)  # Fonte grande para o título
        self.small_font = pygame.font.Font("asset/zombie.ttf", 36)  # Fonte menor para os botões
        self.menu_background = pygame.image.load("asset/menu.png")  # Carrega a imagem de fundo
        self.menu_sound = pygame.mixer.Sound("asset/menu_sound.wav")  # Carrega o som de fundo

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

    def fade_transition(self):
        # Cria uma superfície para o efeito de fade
        fade_surface = pygame.Surface((self.window.get_width(), self.window.get_height()))
        fade_surface.fill((0, 0, 0))  # Preto

        for alpha in range(0, 255, 5):  # Aumenta a opacidade gradualmente
            fade_surface.set_alpha(alpha)
            self.window.blit(fade_surface, (0, 0))
            pygame.display.update()
            pygame.time.delay(30)

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
            options_action = self.draw_button("Opções", (self.window.get_width() // 2 - 100, 320), "options")
            quit_action = self.draw_button("Sair", (self.window.get_width() // 2 - 100, 390), "quit")

            # Verifica se algum botão foi clicado
            if start_action:
                self.fade_transition()  # Efeito de transição
                return "start"
            if options_action:
                self.fade_transition()  # Efeito de transição
                return "options"
            if quit_action:
                self.fade_transition()  # Efeito de transição
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