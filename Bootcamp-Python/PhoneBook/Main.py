import os
import sys

import PhoneBook
import phonebookDB


# Clearing the screen
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def help():
    print("""Welcome to your phonbook
help -- to open the help menu
add -- to add a person to your phonebook
search -- to search for a person
see -- to view your phonebook
quit -- to quit\n""")


def search():
    """Searching for a contact in the database"""
    print("Enter the name")
    name = input("> ")
    phonebookDB.search_contact(name)




def add(answer_string):
    """Adding a contact to the phonebook Database"""
    person = answer_string.split(" ")
    try:
        contact = PhoneBook.PhoneBooks(person[0], person[1], person[2])
    except IndexError:
        help()
    else:
        phonebookDB.add_contact(contact)


def see():
    """Showing all the contacts in the database"""
    phonebookDB.show_all()

def begin():
    """Beginning the programme and initializing the database"""
    phonebookDB.initialize()
    help()
    while True:
        anwers = input(">".lower())

        if anwers == 'see':
            clear_screen()
            see()
        elif anwers == 'add':
            clear_screen()
            print("Enter the firstname,lastname and phonenumber seperated with a space")
            anwers_string = input("> ")
            add(anwers_string)
        elif anwers == "search":
            clear_screen()
            search()
        elif anwers == "help":
            clear_screen()
            help()
        elif anwers == "quit":
            sys.exit()


begin()
