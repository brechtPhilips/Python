import random
from IPython.display import clear_output
"""Tic Tac Toe"""

# Global variables
board  = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
player_dic = {"player1":[0,'',False],"player2":[0,'',False]}

def draw_board(board):
    clear_output()
    print("-"*13)
    print("| {} ".format(board[0][0])+"| {} ".format(board[0][1])+"| {} |".format(board[0][2]))
    print("-" * 13)
    print("| {} ".format(board[1][0]) + "| {} ".format(board[1][1]) + "| {} |".format(board[1][2]))
    print("-" * 13)
    print("| {} ".format(board[2][0]) + "| {} ".format(board[2][1]) + "| {} |".format(board[2][2]))
    print("-" * 13)


def set_character():
    player_dic.get("player1")[1] = input("Player1 are you the 'X' or the 'O' :")
    if player_dic.get("player1")[1] == 'X':
        player_dic.get("player2")[1] = 'O'
    else:
        player_dic.get("player2")[1] = 'X'


def pick_beginner():
    number = random.randrange(1,3)
    if number == 1:
        player_dic.get("player1")[2] = True
    else:
        player_dic.get("player2")[2] = True


def check_position(row, coll):
   if board[row][coll] == 'X' or board[row][coll] == 'O':
       if check_full_board():
           print("It's a draw")
           play_again()
       else:
           print("This place is already chosen, choose another place!")
           return False
   else:
       return True




def make_move(num):
    row = int(input("choose a row :"))-1
    coll = int(input("choose a column :"))-1
    if check_position(row,coll):
        if num == 1 :
            board[row][coll] = player_dic.get("player1")[1]
        else:
            board[row][coll] = player_dic.get("player2")[1]
    else:
        make_move(num)


def check_full_board():
    for i in board:
        if i == '':
            return True
    return False


def check_result(board):
    if (board[0][0] == board[0][1] == board[0][2] == player_dic.get('player1')[1]) or\
            (board[1][0] == board[1][1] == board[1][2] == player_dic.get('player1')[1]) or\
            (board[2][0] == board[2][1] == board[2][2] == player_dic.get("player1")[1]) or \
            (board[0][0] == board[1][1] == board[2][2] == player_dic.get('player1')[1]) or \
            (board[0][2] == board[1][1] == board[2][0] == player_dic.get('player1')[1]) or \
            (board[0][0] == board[1][0] == board[2][0] == player_dic.get("player1")[1]) or \
            (board[0][1] == board[1][1] == board[2][1] == player_dic.get("player1")[1]) or \
            (board[0][2] == board[1][2] == board[2][2] == player_dic.get("player1")[1]):
        print("We have a winner! player 1!")
        player_dic.get('player1')[0] +=1
        return True
    elif (board[0][0] == board[0][1] == board[0][2] == player_dic.get('player2')[1]) or\
            (board[1][0] == board[1][1] == board[1][2] == player_dic.get('player2')[1]) or\
            (board[2][0] == board[2][1] == board[2][2] == player_dic.get("player2")[1]) or \
            (board[0][0] == board[1][1] == board[2][2] == player_dic.get('player2')[1]) or \
            (board[0][2] == board[1][1] == board[2][0] == player_dic.get('player2')[1]) or \
            (board[0][0] == board[1][0] == board[2][0] == player_dic.get("player2")[1]) or \
            (board[0][1] == board[1][1] == board[2][1] == player_dic.get("player2")[1]) or \
            (board[0][2] == board[1][2] == board[2][2] == player_dic.get("player2")[1]):
        print("We have a winner! player 2!")
        player_dic.get('player2')[0] +=1
        return True


def reset_board():
    global board
    board = [["", "", ""],
             ["", "", ""],
             ["", "", ""]
             ]


def play_again():
    answer = input("Do you want to play again? :").lower()
    if answer =='y':
        reset_board()
        play()
    else:
        print("player1 won {} times, and player2 won {} times".format(player_dic.get("player1")[0],player_dic.get("player2")[0]))


def play():
    print("Welcome to Tic Tac Toe")
    set_character()
    pick_beginner()
    while True:
        draw_board(board)
        if not check_result(board):
            if player_dic.get("player1")[2] == True:
                print("Player1 it's your turn!")
                make_move(1)
                player_dic.get("player1")[2] = False
                player_dic.get("player2")[2] = True
            else:
                print("Player2 it's your turn!")
                make_move(2)
                player_dic.get("player2")[2] = False
                player_dic.get("player1")[2] = True
        else:
            play_again()
            break




play()



