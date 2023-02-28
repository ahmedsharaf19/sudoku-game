import sudoku


def write_board(board, choise_uniq_board, flag, filename):
    """ Write Board With Generate Puzzle """

    # flag knows me to choose the board
    if flag:
        board = sudoku.remove_field(board, choise_uniq_board)

    # We will open the file in which we will write
    with open(__file__.replace("file_operations.py", f"{filename}.txt"), "w") as f:
        for i in range(9):
            f.write(
                " --------- --------- ---------  --------- --------- ---------  --------- --------- --------- \n")
            f.write(
                "|         |         |         ||         |         |         ||         |         |         |\n"*2)
            for j in range(9):
                f.write("|")
                if j == 3 or j == 6:
                    f.write("|")
                if board[i][j] != 0:
                    f.write(f"    {board[i][j]}    ")
                else:
                    f.write("         ")
                if j == 8:
                    f.write("|")
            f.write(
                "\n|         |         |         ||         |         |         ||         |         |         |"*2)
            if i == 2 or i == 5:
                f.write(
                    "\n --------- --------- ---------  --------- --------- ---------  --------- --------- --------- ")
            f.write("\n")
        f.write(" --------- --------- ---------  --------- --------- ---------  --------- --------- --------- \n\n\n")

    print(__file__.replace("file_operations.py", f"{filename}.txt"))


# generate complete board
board = sudoku.generate_board()
# copy orignal board before creating puzzle
solution_board = [[j for j in i] for i in board]
# Ask users choise unique board or no
choise_uniq_board = input(
    "Are You Need Unique Board ('y' to yes and 'n' to 'No) : ").strip().lower()
# generate puzzle board and write in file
write_board(board, choise_uniq_board, True, 'sudoku_game')
# Ask Users To Save Original Solution
ch = input("You Need To Show Solution(y or n ) : ").strip().lower()
if ch == 'y' or ch == 'yes':
    write_board(solution_board, choise_uniq_board, False, 'solution')
