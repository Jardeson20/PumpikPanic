from code.Menu import Menu
from code.Game import Game
import pygame

pygame.init()

window = pygame.display.set_mode((1280, 720))

menu = Menu(window)

while True:
    action = menu.run()

    if action == "start":
        menu.menu_sound.stop()

        game = Game(window)
        game_action = game.run()

        if game_action == "game_over":
            print("Fim de jogo!")
        elif game_action == "menu":
            continue
        elif game_action == "quit":
            break
    elif action == "options":
        print("Abrir Opções")
    elif action == "quit":
        break 
pygame.quit()