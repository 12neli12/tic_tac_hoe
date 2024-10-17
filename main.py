game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_one = True


def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")  # joins row with | between them


def check_cord(x, y):
    if game_board[x][y] == " ":
        if player_one:
            game_board[x][y] = "X"
        else:
            game_board[x][y] = "0"


def change_player():
    return not player_one


def check_diagonal():
    return game_board[0][0] == game_board[1][1] == game_board[2][2] != " "


def check_row():
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] != " ":
            return True
    return False


def check_col():
    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != " ":
            return True
    return False


def check_sec():
    return game_board[0][2] == game_board[1][1] == game_board[2][0] != " "


def check_tie():
    for line in game_board:
        if " " in line:
            return False
    return True


def win():
    if check_tie() or check_sec() or check_col() or check_row():
        return True
    return False


def check_endgame():
    for row in game_board:
        if " " in row:
            return False
    return True


while not check_endgame() and not win():
    print_board(game_board)
    try:
        str_cord = input("Enter position (row, col)").strip().split(",")
        coordinates = [int(num) for num in str_cord]
        x_cor = coordinates[0]
        y_cor = coordinates[1]
        check_cord(x_cor, y_cor)
        if win():
            print(f"The winner is player {1 if player_one else 2}!")
        player_one = change_player()
    except (ValueError, IndexError):
        print("Please enter correct numbers in correct form separated by comma!")

    if check_endgame() and not win():
        print("Its a tie!")
