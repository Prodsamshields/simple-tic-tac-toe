import random
board = []
player = "X"


def print_board():
    print("")
    print("\t0\t1\t2")
    count = 0
    for item in board:
        row = ""
        for space in item:
            row += "\t" + space
        print(count, row, "\n")
        count += 1


def is_valid_move(row, column):
    if ((row >= len(board)) or (column >= len(board[0]))):
        return False
    return board[row][column] == "-"


def place_player(player, row, column):
    board[row][column] = player

def minimax(player):
    optimal_row = -1
    optimal_column = -1
    if (check_win("X") == True):
        return (-1, None, None)
    elif (check_win("O" == True)):
        return(1, None, None)
    elif (check_tie() == True):
        return(0, None, None)
    if (player == "X"):
        worst = 1000
        for row in range(3):
            for column in range(3):
                if (board[row][column] == "-"):
                    place_player("X", row, column)
                    payoff = minimax("O")[0]
                    if payoff < worst:
                        worst = payoff
                        optimal_row = row
                        optimal_column = column
                    place_player("-", row, column)
        return (worst, optimal_row, optimal_column)
    else:
        best = -1000
        for row in range(3):
            for column in range(3):
                if ([board][row][column] == "-"):
                    place_player("O", row, column)
                    payoff = minimax("X")[0]
                    if (payoff > best):
                        best = payoff
                        optimal_row = row
                        optimal_column = column
                    place_player("-", row, column)
        return (best, optimal_row, optimal_column)

def take_turn(player):
    if player == "X":
        print("Player X's Turn")
        row = int(input("Enter a row: "))
        column = int(input("Enter a column: "))
        while (is_valid_move(row, column) == False):
            print("Please enter a valid move.")
            row = int(input("Enter a row: "))
            column = int(input("Enter a column: "))
    else:
        print("Player 0's turn")
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        while (is_valid_move(row, column) == False):
            print("Please enter a valid move.")
            row = random.randint(0, 2)
            column = random.randint(0, 2)
    place_player(player, row, column)
    print_board()

def check_row(player):
    for i in range(3):
        if ((board[i][0] == player) and (board[i][1] == player) and (board[i][2] == player)):
            return True
    return False


def check_column(player):
    for i in range(3):
        if ((board[0][i] == player) and (board[1][i] == player) and (board[2][i] == player)):
            return True
    return False


def check_diagonal(player):
    if ((board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player)):
        return True
    elif ((board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player)):
        return True
    else:
        return False


def check_win(player):
    return check_row(player) or check_column(player) or check_diagonal(player)


def check_tie():
    if (("-" in board[0]) or ("-" in board[1]) or ("-" in board[2])):
        return False
    else:
        return (not check_win("X")) and (not check_win("O"))


def check_results():
    if check_win("X") == True:
        print("X wins!")
    elif check_win("O") == True:
        print("O wins!")
    else:
        print("It's a tie!")


for i in range(3):
    board.append(["-", "-", "-"])
print("\t\t Welcome to Tic-Tac-Toe!")
print_board()

while ((check_win("X") == False) and (check_win("O") == False) and (check_tie() == False)):
    take_turn(player)
    if player == "X":
        player = "O"
    else:
        player = "X"

check_results()
