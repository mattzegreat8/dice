from random import randrange
print("This game consists of 6 different dice and 3 rounds. \n At the beginning of the game, each player will choose a certain number sided dice.")
print("There will be a 4,8, and 12 sided dice to choose from.")
player1roll=0
player2roll=0
player1win=0
player2win=0
wincount=3
dice= [randrange(1,4), randrange(1,8), randrange(1,12)]
player1dice= int(raw_input("What dice do you want player 1?"))
player2dice= int(raw_input("What dice do you want player 2?"))

while(player1dice or player2dice != 4 or 8 or 12):
	print("I'm sorry, we do not have that dice please choose again. \n Your options are 4, 8 , and 12")
	if(player1dice or player2dice == 1):
		print("Congrats you won!")
