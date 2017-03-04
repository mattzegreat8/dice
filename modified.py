from random import randrange
print("This game consists of 6 different dice and 3 rounds. \n At the beginning of the game, each player will choose a certain number sided dice.")
print("There will be a 4,6,8,10,12, and 20 sided dice to choose from.")
player1roll=0
player2roll=0
player1win=0
player2win=0
wincount=3
dice= [randrange(1,4), randrange(1,6), randrange(1,8), randrange(1,12), randrange(1,18), randrange(1,20)]
player1dice= raw_input("What dice do you want?")
player2dice= raw_input("What dice do you want?")
