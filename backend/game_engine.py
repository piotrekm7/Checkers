import numpy as np
from typing import List
import string


class Move:
    """
    Represent figure move
    """

    def __init__(self, origin: str, destination: str):
        self.origin = origin
        self.destination = destination


class Capture(Move):
    """
    Represent pawn/pawns capture
    """

    def __init__(self, origin: str, destination: str, captures: List[str]):
        super().__init__(origin, destination)
        self.captures = captures


class Board:
    """
    Class representing board of checkers, it describes actual state of the game.
    """
    board_shape = (8, 8)

    def __init__(self):
        """
        Makes board for starting a new game.
        """
        self.men = self.starting_men_position()
        self.kings = np.zeros(self.board_shape, dtype='int8')
        self.current_player = 1

    def starting_men_position(self) -> np.ndarray:
        """
        Return initial positions of men.
        """
        men = np.zeros(self.board_shape, dtype='int8')
        for i in range(self.board_shape[0]):
            for j in range(self.board_shape[1]):
                if i <= 2 and (i + j) % 2 == 0:
                    men[i, j] = 1
                if i >= 5 and (i + j) % 2 == 0:
                    men[i, j] = -1

        return men

    def make_move(self, move: Move):
        pass

    def __str__(self) -> str:
        """
        Board representation for visualization of current game state
        """
        board = np.full(self.board_shape, ' ')
        board[self.men > 0] = '\u26c0'
        board[self.men < 0] = '\u26c2'
        board[self.kings > 0] = '\u26c1'
        board[self.kings < 0] = '\u26c3'
        letter_line = f'\u2726  {"  ".join(string.ascii_letters[:self.board_shape[1]])}  \u2726'
        rep = f'{letter_line}\n'
        for index, row in reversed(list(enumerate(board.tolist()))):
            rep += f'{index + 1}  {"  ".join(row)}  {index + 1}\n'
        rep += letter_line
        return str(rep)


if __name__ == '__main__':
    board = Board()
    print(board)
