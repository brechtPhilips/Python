import random
class Player:

    def __init__(self,name,bankroll = 100,cardlist = list):
        self.bankroll = bankroll
        self.name = name
        self.cardlist = cardlist

    def __str__(self):
        return "name: {} \nBank: {}".format(self.name,self.bankroll)

    def AddAmount(self,amount):
        self.bankroll += amount

    def TakeAmount(self,amount):
        self.bankroll -= amount
