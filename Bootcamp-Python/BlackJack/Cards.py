class Card:

    def __init__(self,deck,suit):
        self.deck = deck
        self.suit = suit
        if str(suit).isalpha():
           self.value = self.AddValue(str(suit).lower())
        else:
            self.value = int(suit)

    def AddValue(self, suit):
        if suit == "jack":
            return 10
        if suit == "queen":
            return 11
        if suit == "king":
            return 12
        if suit == "ace":
            return 13

    def __str__(self):
        return"{}-{}".format(self.deck,self.suit)
