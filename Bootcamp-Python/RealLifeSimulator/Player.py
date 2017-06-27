class Player:

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.hunger = 100
        self.sleep = 100
        self.money = 0

    @property
    def Hunger(self):
        return self.hunger


    @property
    def Sleep(self):
        return self.sleep


    @property
    def Money(self):
        return self.money



    def __str__(self):
        return "firstname: {} \nlastname: {} \nsleep: {} \nhunger: {} \nmoney: {}".format(self.firstname,self.lastname,self.sleep,self.hunger,self.money)

