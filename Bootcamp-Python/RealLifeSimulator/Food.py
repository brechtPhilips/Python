class Food:

    def __init__(self,description,health,price):
        self.description = description
        self.health = int(health)
        self.price = price

    @property
    def Price(self):
        return self.price
    def Health(self):
        return self.health

    def __str__(self):
        return "{} health: {}  price: {}".format(self.description,self.health,self.price)