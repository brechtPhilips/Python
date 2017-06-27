import random

from combat import Combat

# Static color list for monsters!!
COLORS = ["yellow", "red", "green", "black", "blue"]


class Monster(Combat):
    # Attributes
    min_hit_points = 1
    max_hit_points = 1
    max_experience = 1
    min_experience = 1
    weapon = "sword"
    sound = "roar"

    # __init__ is a method every class has in python
    # It get called when we create a new instance of the class
    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    # Method thats called when you print an object print(name of instansce)
    def __str__(self):
        return '{} {}, HP {}, XP:{}'.format(self.color.title(),
                                            self.__class__.__name__,
                                            self.hit_points,
                                            self.experience)

    # Class Methods
    # self represents the instance that calls the method!
    def battlecry(self):
        return self.sound.upper()


# Subclasses
# goblin extends Monster class
class Goblin(Monster):
    max_hit_points = 3
    max_experience = 2
    sound = "squeak"


class Troll(Monster):
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = "growl"


class Dragon(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = "raaaaaaaaar"
