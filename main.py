from game.game import Game
from game.board import SPIRAL_ORDER


def main() -> None:
    ai_player = 1 if input("AI plays first? [Y/n]") != "n" else 2
    game = Game(ai_player)
    game.play()

if __name__ == "__main__":
    main()
