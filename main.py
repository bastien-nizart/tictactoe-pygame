import random
import pygame
from const import Color
from game import *
from const import Game


# Set the game constants
actual_player_id = random.randint(0, 1)
score = [['', '', ''], ['', '', ''], ['', '', '']]


# Set up the main window
pygame.init()
screen = pygame.display.set_mode([Game.SCREEN_SIZE.value, Game.SCREEN_SIZE.value])
pygame.display.set_caption(f"Joueur {Game.PLAYERS.value[actual_player_id]} tu commences")

screen.fill(Color.WHITE.value)

# Draw the grid
pygame.draw.line(screen, Color.BLACK.value, (175, 25), (175, 475), 1)
pygame.draw.line(screen, Color.BLACK.value, (325, 25), (325, 475), 1)
pygame.draw.line(screen, Color.BLACK.value, (25, 175), (475, 175), 1)
pygame.draw.line(screen, Color.BLACK.value, (25, 325), (475, 325), 1)

sprites = [
    pygame.image.load(Game.TOKEN_IMAGE.value[0]),
    pygame.image.load(Game.TOKEN_IMAGE.value[1])
]


# Run until the user asks to quit
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            line, col = 2, 2
            x, y = pygame.mouse.get_pos()
            # Search col
            if x < 175:
                col = 0
            elif x < 325:
                col = 1
            # Search line
            if y < 175:
                line = 0
            elif y < 325:
                line = 1

            if score[line][col] == '':
                score[line][col] = Game.PLAYERS.value[actual_player_id]
                screen.blit(sprites[actual_player_id], Game.TOKEN_POSITION.value[line][col])

                cond, winner = check(score)
                if cond:
                    print(f"joueur {winner} tu as gagné !")
                    running = False

                actual_player_id = switch_player(Game.PLAYERS.value[actual_player_id])
                pygame.display.set_caption(f"Joueur {Game.PLAYERS.value[actual_player_id]} à toi de jouer")
            else:
                pygame.display.set_caption(
                    f"Joueur {Game.PLAYERS.value[actual_player_id]} à toi de jouer (case déjà prise)"
                )

    pygame.display.flip()

pygame.quit()
