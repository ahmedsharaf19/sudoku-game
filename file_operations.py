import sudoku
import time
def write_board (board,flag,filename) :
    """ 
    Write Board With Generate Puzzle 
    parameter => board and choise write puzzle or solution and filname (solution or puzzle name)
    return => void
    """
    # flag knows me to choose the board 
    if flag :
          board = sudoku.remove_field(board)
     # We will open the file in which we will write
    with open(__file__.replace("file_operations.py",f"{filename}.txt"), "w") as f:
        for i in range(9):
            f.write(" --------- --------- ---------  --------- --------- ---------  --------- --------- --------- \n")
            f.write("|         |         |         ||         |         |         ||         |         |         |\n"*2)
            for j in range(9):
                f.write("|")
                if j == 3 or j == 6 :
                     f.write("|")
                if board[i][j] != 0 :
                     f.write(f"    {board[i][j]}    ")
                else :
                     f.write("         ")
                if j == 8 :
                     f.write("|")
            f.write("\n|         |         |         ||         |         |         ||         |         |         |"*2)
            if i == 2 or i == 5 :
                 f.write("\n --------- --------- ---------  --------- --------- ---------  --------- --------- --------- ")
            f.write("\n")
        f.write(" --------- --------- ---------  --------- --------- ---------  --------- --------- --------- \n\n\n")
    print(__file__.replace("file_operations.py",f"{filename}.txt"))

# generate complete board
board = sudoku.generate_board()
# copy orignal board before creating puzzle 
solution_board = [[j for j in i] for i in board]
# generate puzzle board and write in file
write_board(board,True,'sudoku_game')
print("You Can Play Sudoku Game Now")
start_time = time.time()
choose = input("If You Finish Game Enter (y or yes) : ").strip().lower()
if choose == 'y' or choose == 'yes' :
     end_time = time.time()

# Ask Users To Save Original Solution
while True :
     try :
          ch = input("You Need To Show Solution(y or n ) : ").strip().lower()
          if ch == 'y' or ch == 'yes' :
               write_board(solution_board,False,' solution')
               break
          elif ch == 'n'  or ch == 'no' :
               break
          else :
               raise ValueError
     except ValueError :
          print("Plese Enter Valid Choise!")
     except KeyboardInterrupt:
          print("\nGood Bye!")
          exit()
time_taken = end_time - start_time
print(f"Time taken: {time_taken // 60:.0f} minutes {time_taken%60:.0f} Seconds ")
