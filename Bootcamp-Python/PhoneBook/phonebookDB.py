#!/usr/bin/env python3

from peewee import *

from PhoneBook import PhoneBooks

db = SqliteDatabase("phonelist.db")


class PhoneBookDB(Model):
    fullname = CharField(50)
    phonenumber = CharField(24)

    class Meta:
        database = db


def initialize():
    """Initialize the database"""
    try:
        db.connect()
    except ConnectionError:
        print("**")
    else:
        db.create_table(PhoneBookDB, safe=True)


def add_contact(PhonebookObject):
    """Add a new contact to the database"""
    try:
        new_contact = PhonebookObject

    except ValueError:
        help()
    else:
        full_name = (new_contact.firstname + " " + new_contact.lastname)
        number = new_contact.phonenumber
        if PhoneBookDB.create(fullname=full_name, phonenumber=number):
            print("Added contact to the database")


def search_contact(name):
    phone_list = PhoneBookDB.select().order_by(PhoneBookDB.fullname.desc())

    contact = phone_list.where(PhoneBookDB.fullname.contains(name))

    for cont in contact:
        print("{} : {}".format(cont.fullname, cont.phonenumber))


def show_all():
    phone_list = PhoneBookDB.select()

    for contact in phone_list:
        print("{} : {}".format(contact.fullname, contact.phonenumber))


if __name__ == '__main__':
    initialize()
