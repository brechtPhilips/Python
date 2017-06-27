from Games import Game
from Job import Job
from Player import Player
from Food import Food

import os

from codecs import StreamReader

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def ReadFood():
    foods = list()
    file = open("food.txt",'r')
    file.seek(0)
    line = file.readline()
    while line != '' or None:
        temp_food = line.split(',')
        foods.append(Food(temp_food[0],temp_food[1],temp_food[2]))
        line = file.readline()
    return foods


def ReadJobs():
    jobs = list()
    file = open("jobs.txt", 'r')
    file.seek(0)
    line = file.readline()
    while line != '' or None:
        temp_job = line.split(',')
        jobs.append(Job(temp_job[0], temp_job[1], temp_job[2]))
        line = file.readline()
    return jobs

class Main:
    def Start(self):
        foods = ReadFood()
        jobs = ReadJobs()
        print("Welcome to the Real Life Simulator!")
        print("Please fill in your forename and lastname seperated by a ',': ", end='')
        forename, lastname = input().split(',')
        player = Player(forename, lastname)
        print("Welcome {} {}".format(player.firstname, player.lastname))
        print("Try to survive by working, eating and sleeping, every hour is 3sec in game")
        print("When your hunger and sleep reaches 0 it's game over! Have Fun")
        clear()
        game = Game(player,foods,jobs)

if __name__ == '__main__':
    Main().Start()