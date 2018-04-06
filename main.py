from game.game import Game


def main() -> None:
    ai_vs_ai = False if input("AI vs Human, AI vs AI [0,1]") == str(0) else True
    if (ai_vs_ai):
        game = Game()
        game.play_ia_vs_ia()
    else:
        ai_player = 1 if input("AI plays first? [Y/n]") != "n" else 2
        game = Game(ai_player)
        game.play()

if __name__ == "__main__":
    main()
