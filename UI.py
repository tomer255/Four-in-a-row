import pygame
import board
from pygame.locals import *

width = 700
height = 600


def start():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    game_loop(screen)
    pygame.quit()


def game_loop(screen):
    game_board = board.Board()
    colors = {0: (255, 255, 255), 1: (200, 0, 0), 2: (255, 255, 0)}
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                if game_board.winner is not None:
                    game_board.reset_board()
                pos = pygame.mouse.get_pos()
                pos = pos[0] // 100
                game_board.move(pos)

        screen.fill((0, 0, 255))
        for i in range(board.board_size[0]):
            for j in range(board.board_size[1]):
                pygame.draw.circle(screen, (5, 5, 5), (50 + 100 * j, 550 - 100 * i), 45)
                pygame.draw.circle(screen, colors[game_board.board[i, j]], (50 + 100 * j, 550 - 100 * i), 43)

        if game_board.winner is not None:
            pygame.display.set_caption('Show Text')
            font = pygame.font.Font('Inkfree.ttf', 72)
            text = font.render(f"player {game_board.winner} win!!!", True, colors[game_board.winner], (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (width // 2, height // 2)
            screen.blit(text, textRect)

        pygame.display.flip()
