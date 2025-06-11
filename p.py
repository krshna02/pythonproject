# Tic Tac Toe Game 

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def main():
    board = [["1", "2", "3"],
             ["4", "5", "6"],
             ["7", "8", "9"]]
    
    current_player = "X"
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose a number (1-9): ")
        
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Try again.")
            continue

        move = int(move)
        row = (move - 1) // 3
        col = (move - 1) % 3
        
        if board[row][col] in ['X', 'O']:
            print("That spot is taken. Try another one.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f" Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
