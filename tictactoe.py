def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell if cell != " " else " ", end=" | ")
        print()
        print("-------------")

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tictactoe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        print(f"Player {current_player}, choose your move (row and column, 1-3):")
        try:
            move = input().split()
            if len(move) != 2:
                print("Please enter two numbers (row and column).")
                continue
            row, col = map(int, move)
            if not (1 <= row <= 3 and 1 <= col <= 3):
                print("Numbers must be between 1 and 3.")
                continue
            row -= 1
            col -= 1
            if board[row][col] != " ":
                print("Cell already taken. Choose another.")
                continue
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except KeyboardInterrupt:
            print("\nGame interrupted.")
            break

if __name__ == "__main__":
    tictactoe()