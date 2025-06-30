def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def player_input(player, board):
    while True:
        try:
            pos = int(input(f"Joueur {player} - entrez une position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Position invalide, entrez un nombre entre 1 et 9.")
            elif board[pos] != " ":
                print("Case déjà prise, choisissez une autre case.")
            else:
                return pos
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre.")

def check_win(board, player):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8), 
        (0,3,6), (1,4,7), (2,5,8),  
        (0,4,8), (2,4,6)            
    ]
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(space != " " for space in board)

def play():
    board = [" "] * 9
    current_player = "X"

    print("Bienvenue au Tic Tac Toe !")
    display_board(board)

    while True:
        pos = player_input(current_player, board)
        board[pos] = current_player
        display_board(board)

        if check_win(board, current_player):
            print(f"Félicitations ! Le joueur {current_player} a gagné !")
            break
        if is_board_full(board):
            print("Match nul ! Personne n'a gagné.")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play()
