import re
import os
from typing import List, Tuple


SIZE = 15
P1_VICTORY_PATTERN = re.compile(r"11111")
P2_VICTORY_PATTERN = re.compile(r"22222")

PATTERN_1 = re.compile(r"211110|011112")
PATTERN_2 = re.compile(r"011110")
PATTERN_3 = re.compile(r"01110")
PATTERN_4 = re.compile(r"2011100|0011102")
PATTERN_5 = re.compile(r"010110|011010")
PATTERN_6 = re.compile(r"0110|0110")

ADV_PATTERN_1 = re.compile(r"122220|022221")
ADV_PATTERN_2 = re.compile(r"022220")
ADV_PATTERN_3 = re.compile(r"02220")
ADV_PATTERN_4 = re.compile(r"1022200|0022201")
ADV_PATTERN_5 = re.compile(r"020220|022020")
ADV_PATTERN_6 = re.compile(r"0220")


def stringfy(matrix: List[List[int]]) -> str:
    string = ""
    for line in matrix:
        string += "".join(map(str, line)) + "\n"
    return string


class Board():
    """ A gomoku board, i.e., a state of the game. """

    def __init__(self):
        self._board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        self.stones = {0: ' ', 1: '●', 2: '○'}

    def __str__(self) -> str:
        """
        Pretty-prints the board with black and white bullets.

        Code snippet removed from github.com/zambonin/multivac
        """
        os.system('cls' if os.name == 'nt' else 'clear')

        letter_row = "     " + " ".join(
            chr(i) for i in range(65, 65 + len(self._board[0]))) + '\n'
        top_row = '   ┏' + '━' * (2 * len(self._board[0]) + 1) + '┓\n'
        bottom_row = '   ┗' + '━' * (2 * len(self._board[0]) + 1) + '┛'
        mid_rows = ""

        for row, i in zip(self._board, range(len(self._board))):
            mid_rows += '{:02d} ┃ '.format(i + 1) + ' '.join(
                self.stones[i] for i in row) + ' ┃\n'

        return letter_row + top_row + mid_rows + bottom_row

    def place_stone(self, player: int, position: Tuple[int, int]) -> None:
        x_coord, y_coord = position
        self._board[y_coord][x_coord] = player

    def is_empty(self, position: Tuple[int, int]) -> bool:
        x_coord, y_coord = position
        return self._board[y_coord][x_coord] == 0

    def _diagonals(self) -> List[List[int]]:
        return [[self._board[SIZE - p + q - 1][q]
                 for q in range(max(p - SIZE + 1, 0), min(p + 1, SIZE))]
                for p in range(SIZE + SIZE - 1)]

    def _antidiagonals(self) -> List[List[int]]:
        return [[self._board[p - q][q]
                 for q in range(max(p - SIZE + 1, 0), min(p + 1, SIZE))]
                for p in range(SIZE + SIZE - 1)]

    def _columns(self) -> List[List[int]]:
        return [[self._board[i][j]
                 for i in range(SIZE)]
                for j in range(SIZE)]

    def victory(self) -> bool:
        whole_board = "\n".join(
            map(stringfy,
                [self._board,
                 self._diagonals(),
                 self._antidiagonals(),
                 self._columns()]))

        return True if P1_VICTORY_PATTERN.search(whole_board) or \
            P2_VICTORY_PATTERN.search(whole_board) else False

    def evaluate(self) -> int:
        """ Returns an heuristic value of the current board. """

        whole_board = "\n".join(
            map(stringfy,
                [self._board,
                 self._diagonals(),
                 self._antidiagonals(),
                 self._columns()]))

        value = 0
        if P1_VICTORY_PATTERN.search(whole_board):
            value += 2**32
        elif P2_VICTORY_PATTERN.search(whole_board):
            value -= 2**32

        value += 37 * 56 * len(PATTERN_2.findall(whole_board))
        value += 56 * len(PATTERN_1.findall(whole_board))
        value += 56 * len(PATTERN_3.findall(whole_board))
        value += 56 * len(PATTERN_4.findall(whole_board))
        value += 56 * len(PATTERN_5.findall(whole_board))
        value += len(PATTERN_6.findall(whole_board))

        value -= 37 * 56 * len(ADV_PATTERN_2.findall(whole_board))
        value -= 56 * len(ADV_PATTERN_1.findall(whole_board))
        value -= 56 * len(ADV_PATTERN_3.findall(whole_board))
        value -= 56 * len(ADV_PATTERN_4.findall(whole_board))
        value -= 56 * len(ADV_PATTERN_5.findall(whole_board))
        value -= len(ADV_PATTERN_6.findall(whole_board))

        return value
