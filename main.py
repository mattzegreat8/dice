from random import randrange
print("This game consists of 2 players.\n Each player will roll the dice and the player that rolled the highest number wins. \n This process will be repeated 3 times.")

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