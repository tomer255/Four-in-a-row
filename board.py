import numpy as np

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
            while board_size[0] > new_pos[0] >= 0 and board_size[1] > new_pos[1] >= 0 and self.board[tuple(new_pos)] == self.player:
                count += 1
                dis += 1
                new_pos = pos + direction * dis

            dis = 1
            new_pos = pos - direction * dis
            while board_size[0] > new_pos[0] >= 0 and board_size[1] > new_pos[1] >= 0 and self.board[tuple(new_pos)] == self.player:
                count += 1
                dis += 1
                new_pos = pos - direction * dis

            if count >= 3:
                return self.player
        return None

    def move(self, column: int):
        pos = self.drop(column)
        if pos is None:
            return
        self.winner = self.check_win(pos)
        self.player = (self.player % 2) + 1

    def __repr__(self):
        return f"{self.board}\n"
