from game import Game
from parse_arguments import parse_arguments
from interface import App

# game = Game()
# game.make_move(2, 3)
# game.make_move(2, 4)
# game.make_move(3, 2)
# game.make_move(3, 5)
# game.make_move(4, 3)
# game.make_move(4, 4)
# game.make_move(3, 4)
# game.make_move(3, 3)
# game.make_move(3, 4)
# # game.make_move(1, 4)
# # game.make_move(1, 6)
# # game.make_move(1, 2)
# # game.make_move(2, 6)
# # game.make_move(0, 3)
# # game.make_move(3, 6)
# # game.make_move(2, 3)
# # game.make_move(4, 6)
# # game.make_move(3, 3)
# # game.make_move(4, 5)
# # game.make_move(1, 3)
#
# print(f"Final board:\n{game}")


def main():
    # arg = parse_arguments()
    game = Game()
    App(game).run()


if __name__ == '__main__':
    main()
