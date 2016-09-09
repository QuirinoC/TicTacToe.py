'''
    Juan Carlos Quirino Carrasco
    -----------------------------------------------------
    Tried to do all functions as simple as possible
    Maybe later i will do a more beautiful change_turn(),
    user_input() and win(),tie()
    -----------------------------------------------------
    You are free to user, change and everything, just dont
    copy and present like yours, you can, but give credit
'''
def table():
    #this function creates a 3x3 table
    '''
        - / - / -
        - / - / -
        - / - / -
    '''
    board = []
    for i in range(3):
        board.append(["-"]*3)
    return board
def print_board(board):
    '''This function prints the board in pretty formated way'''
    for column in board:
        print ()
        for i in column:
            print (i, end=" ")
    print ("\n")
    '''
    This is incorrect since it would
    print the same column 3 times
    '''
            #print ("        ", board_[i] , end=" / ")
            #print (board_[i] , end=" / ")
            #print (board_[i])
            #print()
def win(board):
    global turn
    '''
        This function checks if someone wins
        Must be called every time someone writes
    '''
    a = board[0][0]
    b = board[0][1]
    c = board[0][2]
    d = board[1][0]
    e = board[1][1]
    f = board[1][2]
    g = board[2][0]
    h = board[2][1]
    i = board[2][2]
    #Add to test for not being '-' DONE
    '''  0   1   2
    0    a / b / c
    1    d / e / f
    2    g / h / i
    '''
    if \
    (a == b and b == c and b != "-") or \
    (d == e and e == f and e != "-") or \
    (g == h and h == i and h != "-") or \
    \
    (a == d and d == g and d != "-") or \
    (b == e and e == h and e != "-") or \
    (c == f and f == i and f != "-") or \
    \
    (a == e and e == i and e != "-") or \
    (c == e and e == g and e != "-"):
        if turn == 1:
            turn = 2
        else:
            turn = 1
        print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer {} wins!".format(turn))
        play_again()
def tie(board):
    a = board[0][0]
    b = board[0][1]
    c = board[0][2]
    d = board[1][0]
    e = board[1][1]
    f = board[1][2]
    g = board[2][0]
    h = board[2][1]
    i = board[2][2]
    if a != "-" and b != "-" and c != "-" and  \
       d != "-" and e != "-" and f != "-" and \
       g != "-" and h != "-" and i != "-":
       return True
    return False
def change_turn():
    global turn
    global OXturn
    print_board(board)
    if turn == 1:
        turn = 2
        OXturn = "O"
    else:
        turn = 1
        OXturn = "X"
def user_input():
    #
    global turn
    #
    valid_inputs = ['Q','W','E',
                     'A','S','D',
                      'Z','X','C']
    #
    u_input = input("Its player {} turn [] ... ".format(turn)).upper()
    if u_input in valid_inputs:
        if u_input == "Q" and board[0][0] == "-":
            board[0][0] = OXturn
            change_turn()
        elif u_input == "W" and board[0][1] == "-":
            board[0][1] = OXturn
            change_turn()
        elif u_input == "E" and board[0][2] == "-":
            board[0][2] = OXturn
            change_turn()
        elif u_input == "A" and board[1][0] == "-":
            board[1][0] = OXturn
            change_turn()
        elif u_input == "S" and board[1][1] == "-":
            board[1][1] = OXturn
            change_turn()
        elif u_input == "D" and board[1][2] == "-":
            board[1][2] = OXturn
            change_turn()
        elif u_input == "Z" and board[2][0] == "-":
            board[2][0] = OXturn
            change_turn()
        elif u_input == "X" and board[2][1] == "-":
            board[2][1] = OXturn
            change_turn()
        elif u_input == "C" and board[2][2] == "-":
            board[2][2] = OXturn
            change_turn()
        else:
            print ("Cant write there")
            user_input()
    else:
        print ("Please give a valid input")
        user_input()
    '''  0   1   2
    0    q / w / e
    1    a / s / d
    2    z / x / c
    '''
def instructions():
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\nThis is a tictactoe game to play just type in your keyboard as described\n")
    print ("q / w / e")
    print ("a / s / d")
    print ("z / x / c")
def play_again():
    global board
    global OXturn
    if input("Want to play again? (Y/N)").upper() == "Y":
        board = []
        board = table()
        print_board(board)

        game()
def game():
    '''
    To-Do:
        Cuando gana el jugador 2 y se reinicia el juego este tiene 2 turnos
        Al iniciar - HECHO
    '''
    global OXturn
    OXturn = "X"
    change_turn()
    instructions()
    while True:
        user_input()
        if tie(board) or win(board):
            print ("Its a tie")
            play_again()
    print_board(board)


board = table()
input_board = table()
turn = 1
game()
