import random

print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player1 = player1.lower()

computer = random.randint(1,3);

if computer == 1:
	computer = "rock"
elif computer == 2:
	computer = "paper"
else:
	computer = "scissors"
print("The Computer chose: " + computer)

print("SHOOT!")

if (player1 and computer) and (player1 == "paper" or player1 == "rock" or player1 == "scissors") and (computer == "paper" or computer == "rock" or computer == "scissors"):

	if player1 == computer:
			print("It's a draw!")

	if player1 == "rock":
		if computer == "paper":
			print("The Computer Wins!")
		elif computer == "scissors": 
			print("Player 1 Wins!")

	elif player1 == "paper":
		if computer == "rock":
			print("Player 1 Wins!")
		elif computer == "scissors":
			print("The Computer Wins!")

	else:
		if computer == "paper":
			print("Player 1 Wins!")
		elif computer == "rock":
			print("The Computer Wins!")

else:
	print("You must enter a valid choice!")