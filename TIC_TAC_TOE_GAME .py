def print_board(board):
    """Display the Tic Tac Toe board"""
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_win(board):
    """Check if there's a winner"""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_board_full(board):
    """Check if the board is full (tie)"""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_player_move(player, board):
    """Get valid move from player"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue
            
            row, col = move // 3, move % 3
            if board[row][col] == " ":
                return row, col
            else:
                print("That position is already taken. Try again.")
        except ValueError:
            print("Please enter a valid number.")
            

def play_game():
    """Main game function"""

    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9 from top-left to bottom-right.")
    print_board([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Show position reference
    
    while True:
        print_board(board)
        row, col = get_player_move(current_player, board)
        board[row][col] = current_player
        
        winner = check_win(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            return
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

def main():
    """Main program loop"""
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()