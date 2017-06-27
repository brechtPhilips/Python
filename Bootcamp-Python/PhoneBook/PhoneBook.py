class PhoneBooks(object):
    PHONEBOOK_List = {}

    firstname : None
    lastname : None
    phonenumber : None

    def __init__(self, firstname, lastname, phonenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber

