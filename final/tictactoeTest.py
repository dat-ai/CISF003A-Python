import unittest
import pygame
from lib import Board

pygame.init()


class TicTacToeTestCase(unittest.TestCase):
    """
    Unittest for TicTacToe Game
    """
    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        try:
            unittest.TestCase.__init__(self, *args, **kwargs)
            board1 = Board(grid_size=3, box_size=100, border=50, line_width=10)
            board2 = Board(grid_size=5, box_size=50, border=20, line_width=5)
            board3 = Board(grid_size=5, box_size=100, border=20, line_width=5)
            self.test_boards = [board1, board2, board3]
        finally:
            pass

    def setUp(self):
        """
        Create boards with different parameters
        """
        pygame.display.init()

    def test_board_init(self):
        """
        Check if board can initialize with different sizes
        :return:
        """
        for b in self.test_boards:
            self.assertIsNotNone(b)

    def test_box_init(self):
        """
        Test if boxes are initialized correctly
        :return:
        """
        for b in self.test_boards:
            b.initialize_boxes()
            self.assertIsNotNone(b.boxes)

    def test_util_init(self):
        """
        Test if pygame utility is initialized
        :return:
        """
        for b in self.test_boards:
            self.assertIsNotNone(b.pgTool)

    def test_check_winner(self):
        """
        Check if winner is checked properly
        :return:
        """
        # Game is not running, there should be no winner
        for b in self.test_boards:
            self.assertEqual(0, b.check_for_winner())

    def test_calculate_winner(self):
        """
        Check if winner is calculated properly
        :return:
        """
        # Should be not empty
        for b in self.test_boards:
            self.assertIsNotNone(b.winning_combinations)

    def tearDown(self):
        """
        Tear Down unittest
        """
        pygame.display.quit()

if __name__ == '__main__':
    unittest.main()
