import pygame
import sys


class App:
    def __init__(self, game):
        """
        Initialize the App class, which is responsible for the graphical user interface.
        :param game: an object of type Game
        """
        self.__COLOR_PLAYER_1 = (0, 0, 0)
        self.__COLOR_PLAYER_2 = (255, 255, 255)
        self.__COLOR_BACKGROUND = (255, 255, 255)
        self.__COLOR_GRID = (0, 0, 0)
        self.__MARGIN_PERCENTAGE = 0.05
        self.__STONE_RADIUS_FACTOR = 0.4

        self.__game = game
        self.__PLAYER_1 = 1
        self.__PLAYER_2 = 2

        pygame.init()

        screen_info = pygame.display.Info()
        screen_width, screen_height = screen_info.current_w, screen_info.current_h
        min_dimension = min(screen_width - 100, screen_height - 100)

        self.__SIZE_BOARD = self.__game.get_board_size() - 1
        self.__SIZE_MARGIN = int(min_dimension * self.__MARGIN_PERCENTAGE)
        self.__SIZE_GRID = int((min_dimension - 2 * self.__SIZE_MARGIN) / self.__SIZE_BOARD)
        self.__SIZE_STONE_RADIUS = int(self.__SIZE_GRID * self.__STONE_RADIUS_FACTOR)
        self.__SIZE_SCREEN = self.__SIZE_BOARD * self.__SIZE_GRID + 2 * self.__SIZE_MARGIN

        self.__screen = pygame.display.set_mode((self.__SIZE_SCREEN, self.__SIZE_SCREEN))

        self.__app_running = False

    def run(self):
        """
        Run the game.
        """
        pygame.display.set_caption("Game of GO")

        self.__app_running = True

        self.__draw_board()
        while self.__app_running:
            self.__handle_events()
            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def __draw_board(self):
        """
        Draw the board with the specified size.
        """
        self.__screen.fill(self.__COLOR_BACKGROUND)  # Fill the background with the desired color

        # Draw horizontal lines
        for i in range(self.__SIZE_BOARD + 1):
            pygame.draw.line(self.__screen, self.__COLOR_GRID,
                             (self.__SIZE_MARGIN, i * self.__SIZE_GRID + self.__SIZE_MARGIN),
                             (self.__SIZE_SCREEN - self.__SIZE_MARGIN, i * self.__SIZE_GRID + self.__SIZE_MARGIN),
                             2)

        # Draw vertical lines
        for j in range(self.__SIZE_BOARD + 1):
            pygame.draw.line(self.__screen, self.__COLOR_GRID,
                             (j * self.__SIZE_GRID + self.__SIZE_MARGIN, self.__SIZE_MARGIN),
                             (j * self.__SIZE_GRID + self.__SIZE_MARGIN, self.__SIZE_SCREEN - self.__SIZE_MARGIN),
                             2)

        # draw the stones
        board = self.__game.get_board()
        for i in board:
            for j in i:
                print(j, end=" ")
            print()
        for nr_row, row in enumerate(board):
            for nr_col, cell in enumerate(row):
                if cell == self.__PLAYER_1:
                    self.__draw_stone(nr_row, nr_col, self.__COLOR_PLAYER_1)
                elif cell == self.__PLAYER_2:
                    self.__draw_stone(nr_row, nr_col, self.__COLOR_PLAYER_2)

    def __handle_events(self):
        """
        Handle the events of the game
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__app_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # left mouse button was clicked
                self.__handle_left_mouse_button_click()

    def __handle_left_mouse_button_click(self):
        """
        When the left mouse button was clicked, place a stone on the board
        for the player whose turn it is.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        clicked_row, clicked_col = self.__closest_intersection_point(mouse_x, mouse_y)

        if self.__game.make_move(clicked_row, clicked_col):
            self.__draw_board()

    def __draw_stone(self, row, col, color):
        """
        Draw a stone at the specified row and column, of the specified color.
        :param row: a number representing the row
        :param col: a number representing the column
        :param color: a tuple representing the color of the stone
        """
        x = col * self.__SIZE_GRID + self.__SIZE_MARGIN
        y = row * self.__SIZE_GRID + self.__SIZE_MARGIN

        # draw the outline
        pygame.draw.circle(self.__screen, (0, 0, 0), (x, y), self.__SIZE_STONE_RADIUS + 2, 0)
        # draw the stone
        pygame.draw.circle(self.__screen, color, (x, y), self.__SIZE_STONE_RADIUS, 0)

    def __closest_intersection_point(self, x, y):
        """
        Find the closest intersection points to the given coordinates.
        :param x: the x coordinate
        :param y: the y coordinate
        :return: a tuple containing the row and column of the closest intersection point
        """
        print(f"margin: {self.__SIZE_MARGIN}, grid: {self.__SIZE_GRID}")
        print(f"mouse x: {x}, mouse y: {y}")
        closest_row = round((y - self.__SIZE_MARGIN) / self.__SIZE_GRID)
        closest_col = round((x - self.__SIZE_MARGIN) / self.__SIZE_GRID)
        print(f"closest row: {closest_row}, closest col: {closest_col}")
        return closest_row, closest_col

