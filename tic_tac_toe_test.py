import unittest
from tic_tac_toe import *

class TicTacToeTest(unittest.TestCase):

    def testCheckRowsEmpty(self):
        board = [ [ " ", " ", " " ],
            [ " ", " ", " " ],
            [ " ", " ", " " ]
            ]
        setBoard(board)
        self.assertFalse(checkRows())

    def testCheckRowsFirst(self):
        board = [ [ "X", "X", "X" ],
            [ " ", " ", " " ],
            [ " ", " ", " " ]
            ]
        setBoard(board)
        self.assertTrue(checkRows())

    def testCheckRowsSecond(self):
        board = [ [ "X", "X", " " ],
            [ "O", "O", "O" ],
            [ " ", " ", "X" ]
            ]
        setBoard(board)
        self.assertTrue(checkRows())

    def testCheckRowsThird(self):
        board = [ [ " ", " ", " " ],
            [ "O", "O", " " ],
            [ "X", "X", "X" ]
            ]
        setBoard(board)
        self.assertTrue(checkRows())

    def testCheckRowsUnequal(self):
        board = [ [ "X", "O", "X" ],
            [ " ", " ", " " ],
            [ " ", " ", " " ]
            ]
        setBoard(board)
        self.assertFalse(checkRows())

    def testCheckColsEmpty(self):
        board = [ [ " ", " ", " " ],
            [ " ", " ", " " ],
            [ " ", " ", " " ]
            ]
        setBoard(board)
        self.assertFalse(checkCols())

    def testCheckColsFirst(self):
        board = [ [ "X", " ", "O" ],
            [ "X", " ", " " ],
            [ "X", "O", " " ]
            ]
        setBoard(board)
        self.assertTrue(checkCols())

    def testCheckColsSecond(self):
        board = [ [ "X", "O", " " ],
            [ " ", "O", " " ],
            [ " ", "O", "X" ]
            ]
        setBoard(board)
        self.assertTrue(checkCols())

    def testCheckColsThird(self):
        board = [ [ " ", " ", "X" ],
            [ "O", "O", "X" ],
            [ " ", " ", "X" ]
            ]
        setBoard(board)
        self.assertTrue(checkCols())

    def testCheckColsUnequal(self):
        board = [ [ "X", "O", "X" ],
            [ "O", " ", " " ],
            [ "X", " ", " " ]
            ]
        setBoard(board)
        self.assertFalse(checkCols())

    def testCheckDiagonalsEmpty(self):
        board = [ [ " ", " ", " " ],
            [ " ", " ", " " ],
            [ " ", " ", " " ]
            ]
        setBoard(board)
        self.assertFalse(checkDiagionals())

    def testCheckDiagonalsLeft(self):
        board = [ [ "X", " ", "O" ],
            [ "O", "X", " " ],
            [ " ", "O", "X" ]
            ]
        setBoard(board)
        self.assertTrue(checkDiagionals())

    def testCheckDiagonalsRight(self):
        board = [ [ "X", " ", "O" ],
            [ "", "O", " " ],
            [ "O", "X", "X" ]
            ]
        setBoard(board)
        self.assertTrue(checkDiagionals())

    def testCheckDiagonalsUnequal(self):
        board = [ [ "X", "O", "X" ],
            [ "O", "O", " " ],
            [ "X", " ", "X" ]
            ]
        setBoard(board)
        self.assertFalse(checkDiagionals())

    def testNoMoreMovesAvailable(self):
        board = [ [ "X", "O", "X" ],
            [ "O", "O", "X" ],
            [ "X", "O", "X" ]
            ]
        setBoard(board)
        self.assertTrue(noMoveMovesAvailable())

    def testStillMovesAvailable(self):
        board = [ [ "X", "O", " " ],
            [ " ", "O", "X" ],
            [ "X", "O", "X" ]
            ]
        setBoard(board)
        self.assertFalse(noMoveMovesAvailable())

    def testPlayerMadeARow(self):
        board = [ [ "X", "X", "X" ],
            [ "O", "O", "X" ],
            [ "X", "O", "O" ]
            ]
        setBoard(board)
        self.assertTrue(aPlayerHasWon())

    def testPlayerMadeAColumn(self):
        board = [ [ "X", "O", "X" ],
            [ "O", "O", "X" ],
            [ "X", "O", "O" ]
            ]
        setBoard(board)
        self.assertTrue(aPlayerHasWon())

    def testPlayerMadeADiagonal(self):
        board = [ [ "X", "O", "X" ],
            [ "O", "X", "X" ],
            [ "X", "O", "O" ]
            ]
        setBoard(board)
        self.assertTrue(aPlayerHasWon())

if __name__ == "__main__":
    unittest.main()
