def get_room(num):
    if num == 2:
        return get_room_two()
    if num == 3:
        return get_room_three()
    if num == 4:
        return get_room_four()
    if num == 5:
        return get_room_five()
    if num == 6:
        return get_room_six()


def get_beginning_page(name):
    story = "Welcome {} are you ready for your worst nightmare Y/n ?!".format(name)
    return story


def get_room_two():
    story = """About five years ago u lived downtown in a major city in the US.
You have always been a night person, so you would often find yourself bored after your roommate, who was decidedly not a night person, went to sleep.
To pass the time, you used to go for long walks and spend the time thinking."""
    return story


def get_room_three():
    story = """You where walking down central park when suddenly a person apeared behind you.
You ask what he was doing but he didn't say anything and just smiled and pulled out is knive!!
Do you wanne run or fight?"""
    return story


def get_room_four():
    story = """You remembered that you forgot your umbrella sow you went back home"""
    return story


def get_room_five():
    story = """The person began to run to ran towards you.
Your leggs froze off fear but than you started to run like hell and didn't stopped running until you where save at home!
"""
    return story


def get_room_six():
    story = """You didn't back down and began to run to this creepy person with his knife!
You struggeld and fought if your live was depending on it!
You succeeded in taking the knife from him and called the police!"""
    return story

    # add more rooms to make a bigger storrie
    # TODO make classes of rooms and not functions
