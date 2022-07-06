#/usr/bin/env python3


game = ["Chess", "Poker", "Survivor", "Battle_royal"]
answer = " "

while True:
    print("welcome to game world")
    answer = input("choose a game: ")
    # if answer is equal to "chess" on line 12...
    if answer.lower() == "chess": # if forcing the answer to lowercase, make sure it's chess and not Chess you're comparing it to
        nickname= input("Enter a Nickname: ")
        color= input("What color would you like: ")
        answer2= input("Do you want to play first: ") # if you're asking inputs, need to save them as variables
        if answer2 == "yes":   # it can't be equal to "yes" on line 17
            print("common let's play")
        else:
            print("I will go first")
            break
        
    elif answer.lower() == "poker":
        input("Enter a nickname: ")
        board= input("Choose a board: ")
        card= input("do you want to chose the first card: ")
        if card == "yes":
            print("There you go!")
        else:
            print("I will deal first")
            break


    elif answer.lower() == "survivor":
        nickname= input("Enter a nickname: ")
        path= input("Choose a terrain: ")
        vehicle= input("select your car: ")
        rules= input("Do you know the rules: ")
        if rules == "yes":
            print("Let's go for a ride..!!")
        else:
            print("Check out game rules and restart game!!")
            break

    elif answer.lower() == "battle_royal":
        nickname= input("Enter a name: ")
        player= input("choose a player: ")
        weapon= input("select your weapon: ")
        ding= input("Are you ready? ")
        if ding == "yes":
            print("fight")
        else:
            print("Are you scare you would loose to me?")
            break
