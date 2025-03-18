from code.Menu import Menu
from code.Game import Game
import pygame

# Inicializa o PyGame
pygame.init()

# Cria a janela do jogo
window = pygame.display.set_mode((1280, 720))  # Tamanho da tela

# Cria o menu
menu = Menu(window)

# Loop principal do programa
while True:
    # Executa o menu e obtém a ação escolhida pelo jogador
    action = menu.run()

    # Verifica a ação escolhida pelo jogador
    if action == "start":
        # Para a música do menu
        menu.menu_sound.stop()  # Para a música do menu

        # Inicia o jogo
        game = Game(window)  # Passa a janela para a classe Game
        game_action = game.run()

        # Verifica o resultado do jogo
        if game_action == "game_over":
            print("Fim de jogo!")  # Exibe uma mensagem de fim de jogo
        elif game_action == "menu":
            continue  # Volta ao menu
        elif game_action == "quit":
            break  # Encerra o programa
    elif action == "options":
        print("Abrir Opções")  # Aqui você pode implementar a lógica para o menu de opções
    elif action == "quit":
        break  # Encerra o programa

# Encerra o PyGame
pygame.quit()