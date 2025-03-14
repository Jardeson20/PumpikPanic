from code.Menu import Menu
import pygame

# Inicializa o PyGame
pygame.init()

# Cria a janela do jogo com resolução 1920x1080
window = pygame.display.set_mode((1280, 720))

# Cria o menu
menu = Menu(window)

# Executa o menu
action = menu.run()

# Verifica a ação escolhida pelo jogador
if action == "start":
    print("Iniciar Jogo")
elif action == "options":
    print("Abrir Opções")
elif action == "quit":
    print("Sair do Jogo")