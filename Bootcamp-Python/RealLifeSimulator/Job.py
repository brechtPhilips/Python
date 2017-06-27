class Job:

    def __init__(self,describing,money,hour):
        self.description = describing
        self.money = int(money)
        self.hour = int(hour)

    @property
    def Money(self):
        return self.money
    def Hour(self):
        return self.hour

    def __str__(self):
        return "Description: {}, Pay: {}, Hours: {}".format(self.description, self.money, self.hour)