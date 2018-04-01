import re
from typing import Tuple
from game.board import Board
from ab_pruning import ab_pruning


class Game():

    def __init__(self, ai_player: int = 1) -> None:
        self._board = Board(ai_player)
        self._turn = 0
        self._ai_player = ai_player

    def play(self) -> None:
        while not self._board.victory():
            print(self._board)
            if (self._turn % 2) + 1 == self._ai_player:
                self._board, _ = \
                    ab_pruning(self._board, 2, -2**32, 2**32, True)
            else:
                pos = self._player_input()
                self._board.place_stone(pos)
            self._turn += 1
        print(self._board)

    def _player_input(self) -> Tuple[int, int]:
        """
        Input loop for the game. Matches valid coordinates on the board.
        Returns:
            A tuple with the (x, y) coordinates

        Code snippet removed from github.com/zambonin/multivac
        """
        while True:
            raw = input("   Place {} on which coordinate? ".format(
                Board.stones[self._turn % 2 + 1]))

            raw = raw.upper() if raw else 'error'

            if re.match(r'Q(UIT)?', raw):
                raise SystemExit

            if raw[-1] in map(chr, range(65, 80)):
                # invert raw input if letter was typed after number
                raw = raw[len(raw) - 1:] + raw[:len(raw) - 1]

            valid_pos = re.match(r'[A-O](0?[1-9]|1[0-5])\Z', raw)
            pos = (ord(raw[:1]) - 65, int(raw[1:]) - 1)

            if len(pos) != 2 or not valid_pos or \
                    not self._board.is_empty(pos):
                continue
            break

        return pos
