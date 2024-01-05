import copy
from board import Board


class Game:
    """
    A class that represents a game of GO
    """

    def __init__(self, board_size=9):
        """
        Initialize a new Game instance.
        :param board_size: The size of the board, by default it is 9.
        """
        self.__PLAYER_1 = 1
        self.__PLAYER_2 = 2
        self.__is_player_1_turn = True
        self.__board = Board(board_size, self.__PLAYER_1, self.__PLAYER_2)
        self.__nr_captured_stones_by_player_1 = 0
        self.__nr_captured_stones_by_player_2 = 0
        self.__last_2_boards = []
        self.__game_finished = False
        self.__previous_player_passed = False

    def make_move(self, row, col):
        """
        Place a stone on the board at the intersection of row and col.
        :param row: a number representing the row
        :param col: a number representing the column
        :return: True if the move is a legal one, False otherwise
        """
        if self.__game_finished:
            return False

        if self.__previous_player_passed:
            self.__previous_player_passed = False

        if self.__board.is_legal_move(row, col, self.__PLAYER_1 if self.__is_player_1_turn else self.__PLAYER_2, self.__last_2_boards):
            if self.__is_player_1_turn:
                self.__board.set_cell(row, col, self.__PLAYER_1)
                self.__nr_captured_stones_by_player_1 += self.__board.remove_captured_stones(self.__PLAYER_1)
            else:
                self.__board.set_cell(row, col, self.__PLAYER_2)
                self.__nr_captured_stones_by_player_2 += self.__board.remove_captured_stones(self.__PLAYER_2)

            if len(self.__last_2_boards) < 2:
                self.__last_2_boards.append(copy.deepcopy(self.__board))
            else:
                self.__last_2_boards.pop(0)
                self.__last_2_boards.append(copy.deepcopy(self.__board))

            self.__change_turn()

            return True

        return False

    def player_passed(self):
        """
        Pass the turn of the player.
        """
        if self.__previous_player_passed:
            self.__game_finished = True
        self.__previous_player_passed = True
        self.__change_turn()

    def is_game_finished(self):
        """
        :return: True if the game is finished, False otherwise
        """
        return self.__game_finished

    def __change_turn(self):
        """
        Change the turn of the player. If it is player 1's turn, change it to player 2's turn
        and vice versa.
        """
        self.__is_player_1_turn = not self.__is_player_1_turn

    def get_board_size(self):
        """
        :return: the size of the board
        """
        return self.__board.get_size()

    def get_board(self):
        """
        :return: the board, a list of lists
        """
        return self.__board.get_board()

    def get_current_player(self):
        """
        :return: the current player
        """
        return self.__PLAYER_1 if self.__is_player_1_turn else self.__PLAYER_2

    def __str__(self):
        """
        :return: a string representation of the board
        """
        string = ""
        for row in self.__board.get_board():
            string += str(row) + "\n"
        string += f"Point Player-1 : {self.__nr_captured_stones_by_player_1}\n"
        string += f"Point Player-2 : {self.__nr_captured_stones_by_player_2}\n"

        return string
