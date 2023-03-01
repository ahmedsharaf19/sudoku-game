import random

def generate_board() :
    """"
      Create Valid Board 
      parameter => Void
      return => Full Board
    """
    # create a 9x9 board all values equal to zero
    board =[[0 for j in range(9)] for i in range(9)]
    #fill the diagonal sub_grid with random value
    for i in range(0,9,3):
        values = list(range(1,10))
        shuffle_list(values)
        for j in range(3) :
            for k in range(3):
                board[i+j][i+k] = values.pop()
        
        # Solve Puzzle To Creat Valid Board
    solve_board(board)

    return board

def shuffle_list(lst) :
    """ 
    Build Random Shfufle 
    parameter => List Need To Applied Shuffle
    return => Void
    """
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]

def solve_board(board) :
    """ 
    Solve Board To Get Valid Full Board Using BruteForce
    parameter => board
    Return => True if Valid Solution Or False If Not Valid Solution
    """ 
    # find empty cell
    num_row , num_col = find_empty_cell(board)

    # Base Case Recursion 
    if num_row == -1 :
        return True
    
    # Applied Brute Force
    for num in range(1,10) :
        if is_valid(board,num_row,num_col,num):
            board[num_row][num_col] = num
            # Recursion To Solve All Board
            if solve_board(board):
                return True
            
            board[num_row][num_col] = 0
        
    return False

def find_empty_cell(board) :
    """
    Find The Row And Col To Empty Cell In Board
    parameter => Board
    return => (row , col) if found else (-1,-1)
    """
    for i in range(9):
        for j in range(9) :
            if board[i][j] == 0:
                return i , j
    
    return -1,-1

def is_valid(board,row,col,num):
    """
    Check The Number Is Valid In Cell
    parameter => board and number of row , numbrt of col and the value
    return => True if Valid else False
    """
    # check Valid number In row
    if num in board[row] :
        return False
    # check Valid Number in Col
    for i in range(9) :
        if num == board[i][col] :
            return False
    # number of row and col to sub_board
    sub_board_row = (row // 3 ) * 3
    sub_board_col = (col // 3 ) * 3
    # check valid number in sub_board
    for i in range(sub_board_row,sub_board_row+3) :
        for j in range(sub_board_col,sub_board_col+3) :
            if num == board[i][j]:
                return False
    return True

def remove_field(board) :
    """ 
    Build Puzzle Board Denpending on difficulty level
    parameter => board and choise user generate unique board or not
    return => puzzle Board 
    """
    while True :
        try :
            difficulty = input("Enter the difficulty level (easy, medium, hard, or extreme): ")
            if difficulty == "easy":
                num_empty_cells = 40
            elif difficulty == "medium":
                num_empty_cells = 50
            elif difficulty == "hard":
                num_empty_cells  = 60
            elif difficulty == "extreme":
                num_empty_cells =  70
            else :
                raise ValueError 
            break
        except ValueError :
            print("Please Enter Valid Choise !")
        except KeyboardInterrupt :
            print("Good Bye!")
            exit()


    # Make a copy of the board to avoid modifying the original board
    board_copy = [row[:] for row in board]
    # create Puzzle Boared With Unique Solution if users needed this
    #if choise_uniq_board == 'y' or choise_uniq_board == 'yes' :
    # Create a list containing the row and column number of each square on the board
    cells = [(i,j) for i in range(9) for j in range(9)]
    shuffle_list(cells)
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
    # create Puzzle Boared With multiple Solution if users needed this
    #else :
        #while num_empty_cells > 0 :
        #    i = random.randint(0, 8)
        #    j = random.randint(0, 8)
        #    if board_copy[i][j] != 0:
        #        board_copy[i][j] = 0
        #        num_empty_cells -= 1

    return board_copy

def count_solutions(board):
    """
    count number of solution to check unique or not
    parameter => board
    return => count of solution
    """
    count = 0
    # find the next empty cell
    i , j = find_empty_cell(board)
    if i != -1 and j != -1 :
        # try each number in the empty cell
        for num in range(1, 10):
            if is_valid(board, i, j, num):
                board[i][j] = num
                count += count_solutions(board)
                board[i][j] = 0
        return count
            
    # board is complete
    return 1 
