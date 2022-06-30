#/usr/bin/env python3


game = ["Chess", "Poker", "Slapme", "Battle_royal", "Survivor"]
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
        
    elif answer.lower() == "poker":
        input("nickname")
        board= input("Choose a board: ")
        print("sure you want to challenge me?")
