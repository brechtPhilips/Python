
def readUsers():
    with open("Files/astronomy.txt",'r') as file:
        users=file.readlines()
        users = [i.strip("\n") for i in users]
    return users


users = readUsers()
while True:
    username = input("Enter your username: ")
    if username in users:
        print("Username is fine")
        notes = []
        psw = input("Enter password: ")
        if not any(i.isdigit() for i in psw):
            notes.append("You need at least one number")
        if not any(i.isupper() for i in psw):
            notes.append("You need at least one uppercase letter")
        if len(psw) < 5:
            notes.append("You need at least 5 characters")
        if len(notes) == 0:
            print("Password is fine")
            break
        else:
            print("Please check the following: ")
            for note in notes:
                print(note)