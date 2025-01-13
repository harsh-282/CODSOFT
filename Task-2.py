# Tic-Tac-Toe Board
board = [["", "", ""], ["", "", ""], ["", "", ""]]

# Function to display the board
def display_board(board):
    for row in board:
        print("|".join([cell if cell != "" else " " for cell in row]))
        print("-" * 5)

# Check for winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

# Check if the board is full
def is_draw(board):
    for row in board:
        if "" in row:
            return False
    return True

# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return 10 - depth
    elif winner == "O":
        return depth - 10
    elif is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ""
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ""
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Find the best move for the AI
def best_move(board):
    best_val = -float("inf")
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "X"
                move_val = minimax(board, 0, False, -float("inf"), float("inf"))
                board[i][j] = ""
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        # Human move
        print("Your turn! Enter row and column (0, 1, or 2):")
        row, col = map(int, input().split())
        if board[row][col] == "":
            board[row][col] = "O"
        else:
            print("Cell is already occupied. Try again!")
            continue

        display_board(board)

        # Check if the game is over
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        # AI move
        print("AI's turn...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"

        display_board(board)

        # Check if the game is over
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()