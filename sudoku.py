import random


def generate_board():
    """"Create a valid and complete board:
    Generate random shuffle of numbers from 1 to 9 for
    each 3x3 sub-grid of the main diagonal to ensure a
    random valid board between different calls to this
    function. Then it calls solve_board function which
    tries to fill the other 6 sub-grids

    Returns
    -------
        board : list[list[int]]
    """

    # create a 9x9 board all values equal to zero
    board = [[0] * 9 for _ in range(9)]

    # fill the diagonal sub_grid with random value
    for i in range(0, 9, 3):
        values = list(range(1, 10))
        random.shuffle(values)
        for j in range(3):
            for k in range(3):
                board[i+j][i+k] = values.pop()

    # Solve puzzle to creat valid board
    solve_board(board)

    return board


def solve_board(board):
    """Solve board to get valid full board using bruteforce

    Parameters
    ----------
        board : list[list[int]]

    Returns
    -------
        state : bool
            True if valid solution or false if not valid solution
    """
    # find empty cell
    num_row, num_col = find_empty_cell(board)

    # Base Case Recursion
    if num_row == -1:
        return True

    # Applied Brute Force
    for num in range(1, 10):
        if is_valid_cell_choice(board, num_row, num_col, num):
            board[num_row][num_col] = num
            # Recursion To Solve All Board
            if solve_board(board):
                return True

            board[num_row][num_col] = 0

    return False


def find_empty_cell(board):
    """Find an empty cell if such one exists, it is a cell with value of 0

    Parameters
    ---------
        board : list[list[int]]

    Returns
    -------
        row, col : int, int
            the position of the empty cell or (-1, -1) if no such cell exists
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return -1, -1


def is_valid_cell_choice(board, row, col, num):
    """Check if the number in the cell is valid or not

    Parameters
    ----------
        board : list[list[int]]
        row : int
        col : int
        num : int

    Returns
    -------
        is_valid : bool
            True if the num is valid in the cell, otherwise False
    """

    # check Valid number In row
    if num in board[row]:
        return False
    # check Valid Number in Col
    for i in range(9):
        if num == board[i][col]:
            return False
    # number of row and col to sub_board
    sub_board_row = (row // 3) * 3
    sub_board_col = (col // 3) * 3
    # check valid number in sub_board
    for i in range(sub_board_row, sub_board_row+3):
        for j in range(sub_board_col, sub_board_col+3):
            if num == board[i][j]:
                return False

    return True


def get_difficulty_level():
    while True:
        difficulty = input(
            "Enter the difficulty level (easy, medium, hard, or extreme): ")
        if difficulty == "easy":
            return 40
        elif difficulty == "medium":
            return 50
        elif difficulty == "hard":
            return 60
        elif difficulty == "extreme":
            return 65
        else:
            print("Please Enter Valid Choise !")


def remove_fields(board):
    """Build puzzle board denpending on difficulty level

    Parameters
    ----------
        board : list[list[int]]

    Returns
    -------
        board: list[list[int]]
    """

    num_empty_cells = get_difficulty_level()

    # Make a copy of the board to avoid modifying the original board
    board_copy = [row[:] for row in board]
    # create Puzzle Boared With Unique Solution if users needed this
    # if choise_uniq_board == 'y' or choise_uniq_board == 'yes' :
    # Create a list containing the row and column number of each square on the board
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells:
        temp = board_copy[i][j]
        board_copy[i][j] = 0
        # Check if the resulting board still has a unique solution
        if count_solutions(board_copy) != 1:
            board_copy[i][j] = temp
        else:
            num_empty_cells -= 1
        # Stop removing cells when the desired number of cells is reached
        if num_empty_cells == 0:
            break

    return board_copy


def count_solutions(board):
    """Count number of solution to a sudoku board

    Parameters
    ----------
        board : list[list[int]]

    Returns
    -------
        count : int
    """

    count = 0
    # find the next empty cell
    i, j = find_empty_cell(board)
    if i != -1 and j != -1:
        # try each number in the empty cell
        for num in range(1, 10):
            if is_valid_cell_choice(board, i, j, num):
                board[i][j] = num
                count += count_solutions(board)
                board[i][j] = 0
        return count

    # board is complete
    return 1


def check_board(board):
    """Check the board if it is a valid complete sudoku board

    Parameters
    ----------
        board : list[list[int]]
    
    Returns
    -------
        state : bool
            True if it is valid, otherwise False
    """

    # check duplication in rows
    for r in range(9):
        if len(set(board[r])) < 9:
            return False

    # check duplication in columns
    for c in range(9):
        s = set()
        for r in range(9):
            if board[r][c] < 1 or board[r][c] > 9:
                return False
            s.add(board[r][c])
        if len(s) < 9:
            return False
    
    # check duplication in sub-grids
    for g in range(9):
        s = set()
        for i in range(9):
            r = (g // 3) * 3 + i // 3
            c = (g % 3) * 3 + i % 3
            s.add(board[r][c])
        if len(s) < 9:
            return False
    
    return True

