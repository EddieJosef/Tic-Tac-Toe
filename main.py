game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def show_board():
    print("---+-----+---")
    print(game_board[0], " | ", game_board[1], " | ", game_board[2],
          "    1, 2, 3")
    print("---+-----+---")
    print(game_board[3], " | ", game_board[4], " | ", game_board[5],
          "    4, 5, 6")
    print("---+-----+---")
    print(game_board[6], " | ", game_board[7], " | ", game_board[8],
          "    7, 8, 9")


def player_move(char):
    print(f"{char}'s turn")
    o_input = int(input("choose a spot a location 1-9\n"))
    if game_board[o_input - 1] == "-":
        game_board[o_input - 1] = char
        show_board()
    else:
        print("Invalid input. please, try again")


def check_win():
    # rows
    if game_board[0] == game_board[1] == game_board[2] != "-":
        print(f"{game_board[0]} Wins")
        return True
    elif game_board[3] == game_board[4] == game_board[5] != "-":
        print(f"{game_board[3]} Wins")
        return True
    elif game_board[6] == game_board[7] == game_board[8] != "-":
        print(f"{game_board[6]} Wins")
        return True
    # columns
    elif game_board[0] == game_board[3] == game_board[6] != "-":
        print(f"{game_board[0]} Wins")
        return True
    elif game_board[1] == game_board[4] == game_board[7] != "-":
        print(f"{game_board[1]} Wins")
        return True
    elif game_board[2] == game_board[5] == game_board[8] != "-":
        print(f"{game_board[2]} Wins")
        return True
    # diagonals
    elif game_board[2] == game_board[4] == game_board[6] != "-":
        print(f"{game_board[2]} Wins")
        return True
    elif game_board[0] == game_board[4] == game_board[8] != "-":
        print(f"{game_board[0]} Wins")
        return True
    else:
        return False


def game():
    win = False
    players = ["X", "O"]
    print("Welcome to Tic Tac Toe\n")
    show_board()
    player_choice = int(input("\nchoose your character. enter 1 for X and 2 for O\n"))

    if player_choice not in [1, 2]:
        print("Invalid input. please, try again")

    while not win:
        player_move(players[player_choice - 1])
        win = check_win()
        if not win:
            player_move(players[player_choice - 2])
            win = check_win()
    game()


game()
