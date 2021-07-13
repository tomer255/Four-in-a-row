import numpy as np
import copy

board_size = (6, 7)


class Board:
    def __init__(self):
        self.board = np.zeros(board_size, dtype=int)
        self.player = 1
        self.winner = None

    def drop(self, column: int):
        for i in range(board_size[0]):
            if self.board[i, column] == 0:
                self.board[i, column] = self.player
                return np.array((i, column))
        return None

    def check_win(self, pos: np.array):
        directions = [np.array((1, 1)), np.array((-1, 1)), np.array((0, 1)), np.array((1, 0))]
        for direction in directions:
            count = 0
            dis = 1
            new_pos = pos + direction * dis
            while board_size[0] > new_pos[0] >= 0 and board_size[1] > new_pos[1] >= 0 and self.board[
                tuple(new_pos)] == self.player:
                count += 1
                dis += 1
                new_pos = pos + direction * dis

            dis = 1
            new_pos = pos - direction * dis
            while board_size[0] > new_pos[0] >= 0 and board_size[1] > new_pos[1] >= 0 and self.board[
                tuple(new_pos)] == self.player:
                count += 1
                dis += 1
                new_pos = pos - direction * dis

            if count >= 3:
                return self.player
        return None

    def count_max_row(self, pos: np.array):
        directions = [np.array((1, 1)), np.array((-1, 1)), np.array((0, 1)), np.array((1, 0))]
        max_row = 0
        for direction in directions:
            count = 0
            dis = 1
            new_pos = pos + direction * dis
            while board_size[0] > new_pos[0] >= 0 and board_size[1] > new_pos[1] >= 0 and self.board[
                tuple(new_pos)] == self.player:
                count += 1
                dis += 1
                new_pos = pos + direction * dis

            dis = 1
            new_pos = pos - direction * dis
            while board_size[0] > new_pos[0] >= 0 and board_size[1] > new_pos[1] >= 0 and self.board[
                tuple(new_pos)] == self.player:
                count += 1
                dis += 1
                new_pos = pos - direction * dis

            max_row = max(max_row, count)
        return max_row

    def move(self, column: int):
        pos = self.drop(column)
        if pos is None:
            return
        self.winner = self.check_win(pos)
        self.player = (self.player % 2) + 1
        return self

    def reset_board(self):
        self.board = np.zeros(board_size, dtype=int)
        self.player = 1
        self.winner = None

    def end_game(self):
        return self.winner is not None or len(self.board.nonzero()[0]) == board_size[0] * board_size[1]

    def best_move(self):
        best_score = -99
        best_move = None
        for column in range(board_size[1]):
            if self.board[board_size[0] - 1, column] == 0:
                child = copy.deepcopy(self)
                pos = child.drop(column)
                score = child.count_max_row(pos)
                # offensive
                if score > best_score:
                    best_score = score
                    best_move = column
                # offensive
                child.player = (child.player % 2) + 1
                for column2 in range(board_size[1]):
                    if child.board[board_size[0] - 1, column2] == 0:
                        child2 = copy.deepcopy(child)
                        pos = child2.drop(column2)
                        score = child2.count_max_row(pos)
                        if score > best_score:
                            best_score = score
                            best_move = column2
        return best_move

    def __repr__(self):
        return f"{self.board}\n"
