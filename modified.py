from random import randrange
print("This game consists of 3 different dice and 3 rounds. \n At the beginning of the game, each player will choose a certain number sided dice.")
print("There will be a 4,8, and 12 sided dice to choose from.")
player1roll=0
player2roll=0
player1win=0
player2win=0
wincount=3
dice= [randrange(1,4), randrange(1,8), randrange(1,12)]
player1dice= int(raw_input("What dice do you want player 1?\n Type 0 to select the d4.\n Type 1 to select the d8.\n Type 2 to select the d12.\n"))
player2dice= int(raw_input("What dice do you want player 2?\n Type 0 to select the d4.\n Type 1 to select the d8.\n Type 2 to select the d12.\n"))

while(player1win != wincount and player2win != wincount):
	player1roll= dice[player1dice]
	print(player1roll)
	player2roll= dice[player2dice]
	print(player2roll)

	if(player1roll>player2roll):
		player1win+= 1
		print("player 1 won that round")

	if(player2roll>player1roll):
		player2win+= 1
		print("player 2 won that round")
	
	if(player1roll == player2roll):
		player1win += 1
		print("Player 1 wins")

	if(player1roll == 1):
		player1win += 3
		print("Congrats Player 1, You won!")
	if(player2roll ==1):
		player2win += 3
		print("Congrats Player 2, You won!")

	if(player1dice == dice[2]):
		player2win += 1
		print("Im sorry player 1, you lost!")
	if(player2dice == dice[2]):
		player1win += 1
		print("Im sorry player 2, you lost!")

	if(player1roll== 3):
		player2win+=1
		print("I'm sorry player 1, you lost!")
	if(player2roll==3):
		player1win +=1
		print("I'm sorry player 2, you lost!")
	if(player1win == wincount):
		print("congrats player 1 you won")
	if(player2win == wincount):
		print("congrats player 2 you won")
	
    

    
