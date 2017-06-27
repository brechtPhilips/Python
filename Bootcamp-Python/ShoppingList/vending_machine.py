sodas = ["Pepsi", "Cherry Coke Zero", "Sprite"]
chips = ["Doritos", "Fritos"]
candy = ["Snickers", "M&Ms", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, some chips or a CANDY? ").lower()
    try:
        if choice == "soda":
            snack = sodas.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("Sorry I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of  {}! Sorry!".format(choice))
    else:
        print("Her's you {} : {}".format(choice, snack))
