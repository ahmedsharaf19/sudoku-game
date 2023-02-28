import random


def generate_board():
    # create a 9x9 board all values equal to zero
    board = [[0 for j in range(9)] for i in range(9)]

    # fill the diagonal sub_grid with random value
    for i in range(0, 9, 3):
        values = list(range(1, 10))
        suffle_list(values)
        for j in range(3):
            for k in range(3):
                board[i+j][i+k] = values.pop()

        # Solve Puzzle To Creat Valid Board
    solve_board(board)

    return board


def suffle_list(lst):
    """ Build Random Shfufle """
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]


def solve_board(board):
    # find empty cell
    num_row, num_col = find_empty_cell(board)

    if num_row == -1:
        return True

    for num in range(1, 10):
        if is_valid(board, num_row, num_col, num):
            board[num_row][num_col] = num

            if solve_board(board):
                return True

            board[num_row][num_col] = 0

    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

    return -1, -1


def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    for i in range(9):
        if num == board[i][col]:
            return False

    sub_board_row = (row // 3) * 3
    sub_board_col = (col // 3) * 3

    for i in range(sub_board_row, sub_board_row+3):
        for j in range(sub_board_col, sub_board_col+3):
            if num == board[i][j]:
                return False
    return True


def remove_field(board, choise_uniq_board):
    """ Build Puzzle Board Denpending on difficulty level """
    difficulty = input(
        "Enter the difficulty level (easy, medium, hard, or extreme): ")
    if difficulty == "easy":
        num_empty_cells = 30
    elif difficulty == "medium":
        num_empty_cells = 40
    elif difficulty == "hard":
        num_empty_cells = 50
    elif difficulty == "extreme":
        num_empty_cells = 60
    else:
        raise ValueError("Invalid Value!")

    # create Puzzle Boared With Unique Solution if users needed this
    if choise_uniq_board == 'y' or choise_uniq_board == 'yes':
        while num_empty_cells > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                temp = board[row][col]
                board[row][col] = 0
                count = count_solutions(board)
                if count != 1:
                    board[row][col] = temp
                else:
                    num_empty_cells -= 1
    # create Puzzle Boared With multiple Solution if users needed this
    else:
        while num_empty_cells > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if board[i][j] != 0:
                board[i][j] = 0
                num_empty_cells -= 1

    return board


def count_solutions(board):
    count = 0
    # find the next empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # try each number in the empty cell
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        count += count_solutions(board)
                        board[i][j] = 0
                return count

    # board is complete
    return 1
