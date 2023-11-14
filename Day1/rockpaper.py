import random
def game():
    choices=["stone","paper","scissors"]
    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("stone,paper or scissors?? :")
        if(computer==player):
            print("Computer : ",computer)
            print("player : ",player)
            print("its a Tie!!")
        elif player =="stone":
            if(computer=="scissors"):
                print("Computer : ",computer)
                print("player : ",player)
                print("You Won!!")
            if(computer=="paper"):
                print("Computer : ",computer)
                print("player : ",player)
                print("You Lose!!")
        elif player =="paper":
            if(computer=="scissors"):
                print("Computer : ",computer)
                print("player : ",player)
                print("You Lose!!")
            if(computer=="scissors"):
                print("Computer : ",computer)
                print("player : ",player)
                print("You Lose!!")
        elif player =="scissors":
            if(computer=="paper"):
                print("Computer : ",computer)
                print("player : ",player)
                print("You Won!!")
            if(computer=="stone"):
                print("Computer : ",computer)
                print("player : ",player)
                print("You Lose!!")
        # game()

game()