#!/usr/bin/python3

def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    # Lignes
    for row in board:
        if row[0] != " " and row.count(row[0]) == 3:
            return row[0]
    # Colonnes
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # Diagonales
    if board[1][1] != " ":
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None  # pas de gagnant

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(player):
    while True:
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input. Please enter integers 0, 1, or 2.")
            continue
        if row not in (0, 1, 2) or col not in (0, 1, 2):
            print("Out of range. Use 0, 1, or 2 for both row and column.")
            continue
        return row, col

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row, col = get_move(player)

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # alterne le joueur
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
