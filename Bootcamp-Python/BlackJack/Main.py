from Cards import Card
from Players import Player


def CreatePlayers(answer):
    templist = list()
    for i in range(answer):
        print("New Player :")
        print("Please fill in your name: ", end='')
        name = input()
        player = Player(name)
        templist.append(player)

    return templist


def Begin(playersList):
    while True:
        for player in playersList:
            for card in player.cardlist:
                print(card)
        



class Main:
    def Start(self):
        print("Welcome")
        try:
            print("How many players are u gonne play ?: ", end='')
            answer = int(input())

        except ValueError:
            print("Please fill in a number!")
            self.Start()
        else:
            playersList = CreatePlayers(answer)
            self.CreateCards(playersList)
            Begin(playersList)


    def CreateCards(self, playersList):
        temp_cards = list()
        cards_list = list()
        file = open("Cards.txt",'r')
        file.seek(0)
        line = file.readline().strip('\n')
        while line is not '' or None:
            temp_cards.append(line.split(','))
            line = file.readline().strip('\n')
        for deck in temp_cards[1]:
            for suit in temp_cards[0]:
                card = Card(deck,suit)
                cards_list.append(card)
        for player in playersList:
            player.cardlist = cards_list


if __name__ == '__main__':
    Main().Start()