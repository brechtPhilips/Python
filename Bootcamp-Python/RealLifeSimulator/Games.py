import time
import os

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def UpdateEatState(player, food):
    value = food.health

    if (player.money - int(food.price)) >= 0 :
        player.money = player.money - int(food.price)
        player.hunger += value
        if player.hunger > 100:
            player.hunger = 100
    else:
        print("You don't have enough money to buy this {}".format(food.description))
        time.sleep(2)


def CheckPlayerState(player, job):
    job_time = int(job.hour)
    sleep_damage = job_time
    eat_damage = job_time/4

    if (player.sleep - sleep_damage > 0):
        if (player.hunger - eat_damage > 0):
            player.money += job.money
            player.sleep = player.sleep - sleep_damage
            player.hunger = player.hunger - eat_damage
            print("Going to work!")
            time.sleep(job_time)
        else:
            print("Your to hungry to go to work!")
            time.sleep(2)
    else:
        print("Go get some Sleep first!")
        time.sleep(2)



class Game():
    one_hour = 3
    def __init__(self,player,foods,jobs):
        self.player = player
        self.foods = foods
        self.jobs = jobs
        self.Start()

    def Start(self):
        while self.player.Hunger or self.player.Sleep != 0:
            clear()
            print(self.player)
            answer=self.ChooseAction()
            if answer == 'e' and self.player.hunger != 100 and self.player.money != 0:
                self.BuyFood()
            if answer == 'w':
                self.ChooseWork()
            if answer == 's':
                self.Rest()




    def ChooseAction(self):
        print("Do you wish to Work(w),Eat(E) or Sleep(S) :",end='')
        answer = input().lower()
        return answer

    def BuyFood(self):
        i = 0
        print("Which food would u like to buy ?")
        for food in self.foods:
            print("{}: {}".format(i, food))
            i += 1
        print("Choose the number : ",end='')
        number = int(input())
        food = self.foods[number]
        UpdateEatState(self.player,food)

    def ChooseWork(self):
        i = 0
        print("Which work are you going to do..?")
        for job in self.jobs:
            print("{}: {}".format(i, job))
            i += 1
        print("Choose the number : ", end='')
        number = int(input())
        job = self.jobs[number]
        CheckPlayerState(self.player,job)

    def Rest(self):
        while self.player.sleep < 100:
            self.player.sleep +=5
            print("Resting...")
            time.sleep(1)
            self.player.hunger += -0.5

        self.player.sleep = 100
