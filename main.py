from random import randrange
print("This game consists of 2 players.\n Each player will roll the dice and the player that rolled the highest number wins. \n This process will be repeated 3 times.")
'''
player1= raw_input("What is player ones name?")
player2= raw_input("What is player twos name?")


roll1=randrange(1,7)
print("{}, you rolled this!".format(player1))
print(roll1)


roll2=randrange(1,7)
print("{}, you rolled this!".format(player2))
print(roll2)

if(roll1>roll2):
	print( "{} wins".format(player1))
if(roll1<roll2):
	print("{} wins".format(player2))
'''

player1roll=0
player2roll=0

wincount=3
player1win=0
player2win=0

while(player1win != wincount and player2win != wincount):
	player1roll=randrange(1,7)
	print(player1roll)
	player2roll=randrange(1,7)
	print(player2roll)
	if(player1roll>player2roll):
		player1win+= 1
		print("Player 1, you won that round!")

	if(player2roll>player1roll):
		player2win+= 1
		print("Player 2, you won that round!")
		
	if(player1win==3):
		print("Player 1, you win!")
	if(player2win==3):
		print("Player 2, you win!")
