#Create a program that askes for user input until
#the user types CLOSE and save the input to a file
#Option if the user types SAVE the input will be saved to a file and continue to run

list_inputs = []
user_input = ""


def WriteToFile(list_inputs):
    with open("Files/values.txt", 'a+') as file:
        for i in list_inputs:
            file.write(i + "\n")


while True:
    user_input = input("Write a value: ")
    if user_input == "CLOSE":
        WriteToFile(list_inputs)
        break
    elif user_input == "SAVE":
        WriteToFile(list_inputs)
        list_inputs = []
    else:
        list_inputs.append(user_input)


