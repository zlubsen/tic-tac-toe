quit_game_signal = False
player_turn = 'X'
empty_cell = ' '
board = [ [ " ", " ", " " ],
    [ " ", " ", " " ],
    [ " ", " ", " " ]
    ]
board_size = len(board)
board_vertical_spacer = "|"
board_horizonal_spacer = "-"
board_line = "-------"

cursor_position_x = 0
cursor_position_y = 0
cursor_char = '*'

key_index = {
    ' ' : lambda: setMark(),
    'i' : lambda: moveUp(),
    'k' : lambda: moveDown(),
    'j' : lambda: moveLeft(),
    'l' : lambda: moveRight(),
    'q' : lambda: quitGame()
}

def main():
    while gameRunning():
        printBoard()
        print(f"Player {player_turn} is to make a move:")
        evalInput()

    printBoard()
    print("Game finished.")

def gameRunning():
    return not aPlayerHasWon() and not noMoveMovesAvailable() and not quit_game_signal

def aPlayerHasWon():
    won = checkRows() or checkCols() or checkDiagionals()
    if won:
        swapPlayerTurn()
        print(f"Player {player_turn} has won!")
    return won

def checkRows():
    won = False
    for row in range(0,3):
        won = won or (board[row][0] == board[row][1] == board[row][2] and not board[row][0] == empty_cell)
    return won

def checkCols():
    won = False
    for col in range(0,3):
        won = won or (board[0][col] == board[1][col] == board[2][col] and not board[0][col] == empty_cell)
    return won

def checkDiagionals():
    diag_top_left = board[0][0] == board[1][1] == board[2][2]
    diag_top_right = board[2][0] == board[1][1] == board[0][2]
    return not board[1][1] == empty_cell and (diag_top_left or diag_top_right)

def noMoveMovesAvailable():
    for row in board:
        for cell in row:
            if cell == empty_cell:
                return False
    print("No more moves available.")
    return True

def swapPlayerTurn():
    global player_turn
    if player_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'

    resetCursorPostition()

def printBoard():
    print(board_line)
    x_coordinate = 0
    for row in board:
        if cursor_position_x == x_coordinate and cursor_position_y == 0:
            line = '>'
        else:
            line = board_vertical_spacer
        y_coordinate = 0
        for cell in row:
            line += renderCell(x_coordinate, y_coordinate, cell)
            y_coordinate += 1
        print(line)
        print(board_line)
        x_coordinate += 1

def renderCell(x, y, cell):
    if (cursor_position_x, cursor_position_y) == (x, y):
        return cell + '<'
    elif cursor_position_x == x and cursor_position_y == y + 1:
        return cell + '>'
    else:
        return cell + board_vertical_spacer

def evalInput():
    key_pressed = input()

    if key_pressed in key_index:
        key_index[key_pressed]()
    else:
        print("Unbound key")

def setMark():
    global board
    cell = board[cursor_position_x][cursor_position_y]
    if cell == empty_cell:
        board[cursor_position_x][cursor_position_y] = player_turn
        swapPlayerTurn()
    else:
        print("Cell not empty, try again.")

def moveUp():
    global cursor_position_x
    if cursor_position_x == 0:
        cursor_position_x = board_size - 1
    else:
        cursor_position_x -= 1

def moveDown():
    global cursor_position_x
    if cursor_position_x == board_size - 1:
        cursor_position_x = 0
    else:
        cursor_position_x += 1

def moveLeft():
    global cursor_position_y
    if cursor_position_y == 0:
        cursor_position_y = board_size - 1
    else:
        cursor_position_y -= 1

def moveRight():
    global cursor_position_y
    if cursor_position_y == board_size - 1:
        cursor_position_y = 0
    else:
        cursor_position_y += 1

def quitGame():
    global quit_game_signal
    quit_game_signal = True
    print("You pressed Quit...")

def resetCursorPostition():
    global cursor_position_x
    global cursor_position_y
    cursor_position_x = 0
    cursor_position_y = 0

def setBoard(test_board):
    global board
    board = test_board

if __name__ == '__main__':
    main()
