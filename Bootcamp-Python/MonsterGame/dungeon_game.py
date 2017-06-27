import os
import random
import sys

SIZE = 0
CELLS = []
addMonster = False

# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define Map Size
def set_map_size(size):
    x = 0
    y = 0
    for i in range(int(size)):
        for j in range(int(size)):
            CELLS.append((j, i))

def get_locations():
    return random.sample(CELLS, 3)


# Move the player on the map
def move_player(player, move):
    x, y = player

    if move == "LEFT":
        x -= 1
    if move == "RIGHT":
        x += 1
    if move == "UP":
        y -= 1
    if move == "DOWN":
        y += 1

    return x, y


# See where the player kan move to
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]
    x, y = player

    if x == 0:
        moves.remove("LEFT")
    if x == SIZE - 1:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == SIZE - 1:
        moves.remove("DOWN")
    return moves


# Draw the map
def draw_map(player, monster, door):
    print(" _" * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < (SIZE - 1):
            line_end = ""
            if cell == player:
                output = tile.format("X")
            elif cell == monster:
                output = tile.format("@")
            elif cell == door:
                output = tile.format("^")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            elif cell == monster:
                output = tile.format("@|")
            elif cell == door:
                output = tile.format("^")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

# see if the player wants to play again
def play_again():
    print("Do you want to play again?? Y/n")
    answer = input("> ")
    if answer.lower() == "y":
        global CELLS
        CELLS = []
        play()
    else:
        sys.exit()



def set_monster(monster, valid_moves):
    random_move = valid_moves[random.randrange(0, len(valid_moves))]
    x, y = monster

    if random_move == "LEFT":
        x -= 1
    if random_move == "RIGHT":
        x += 1
    if random_move == "UP":
        y -= 1
    if random_move == "DOWN":
        y += 1

    return x, y


def check_result(player, monster, door):
    if player == monster:
        print("\n ** Oh no! The monster got you! Better luck next time! ** \n")
        return False
    if player == door:
        print("\n ** You've escaped! Congratulations!! ** \n")
        return False
    return True

# Main game loop
def game_loop():
    if addMonster:
        monster, monster_two, door, player = get_locations()
    else:
        monster, door, player = get_locations()
    playing = True
    while playing:
        clear_screen()
        draw_map(player, monster, door)
        valid_moves = get_moves(player)
        valid_monster_moves = get_moves(monster)
        print("You're(X) currently in room {}".format(player))
        print("door : ^ ")
        print("monster_one : @ : {}".format(monster))

        print("You can move {}".format(",".join(valid_moves)))
        print("Enter QUIT to quit")
        move = input("> ")
        move = move.upper()
        if move == "QUIT":
            print("\n ** Goodbye ** \n")
            break
        if move in valid_moves:
            player = move_player(player, move)
            playing = check_result(player, monster, door)
            if playing:
                monster = set_monster(monster, valid_monster_moves)
                playing = check_result(player, monster, door)
        else:
            input("\n ** Walls are hard! Don't run into them ** \n")

    else:
        play_again()


def check_size(size):
    correct_size = True
    while correct_size:
        if (size < 5) or (size > 20):
            print("Please fill in the right map size 5 - 20")
            size = int(input("> "))
        else:
            correct_size = False
    else:
        return size


def play():
    global SIZE
    clear_screen()
    print("Welcome to the dungeon")
    input("Press return to start!")
    print("Set map size 5 - 20!")
    # Get acces to the global variable size
    # global size
    size = check_size(int(input("> ")))
    set_map_size(size)
    SIZE = size
    clear_screen()
    game_loop()


play()
