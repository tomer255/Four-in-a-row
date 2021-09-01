import pygame
import board
from pygame.locals import *

column_size = 100
width = board.board_size[1] * column_size
height = board.board_size[0] * column_size


def start():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    game_loop(screen)
    pygame.quit()


def game_loop(screen):
    pygame.display.set_caption('Four in a row')
    game_board = board.Board()
    colors = {0: (255, 255, 255), 1: (200, 0, 0), 2: (255, 255, 0), None: (255, 255, 255)}
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if game_board.end_game():
                    game_board.reset_board()
                pos = pygame.mouse.get_pos()
                pos = pos[0] // column_size
                game_board.move(pos)
                if not game_board.end_game() and game_board.player == 2:
                     game_board.move(game_board.best_move())

        screen.fill((0, 0, 255))
        for i in range(board.board_size[0]):
            for j in range(board.board_size[1]):
                pygame.draw.circle(screen, (5, 5, 5), (column_size/2 + column_size * j, height - column_size/2 - column_size * i), 45)
                pygame.draw.circle(screen, colors[game_board.board[i, j]], (column_size/2 + column_size * j, height - column_size/2 - column_size * i), 43)

        if game_board.end_game():
            font = pygame.font.Font('Inkfree.ttf', 72)
            text = font.render(f"player {game_board.winner} win!!!", True, colors[game_board.winner], (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            screen.blit(text, textRect)

        pygame.display.flip()
