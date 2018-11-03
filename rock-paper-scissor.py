print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if (player1 and player2) and (player1 == "paper" or player1 == "rock" or player1 == "scissors") and (player2 == "paper" or player2 == "rock" or player2 == "scissors"):

	if player1 == player2:
			print("It's a draw")

	if player1 == "rock":
		if player2 == "paper":
			print("Player 2 Wins!")
		elif player2 == "scissors": 
			print("Player 1 Wins!")

	elif player1 == "paper":
		if player2 == "rock":
			print("Player 1 Wins!")
		elif player2 == "scissors":
			print("Player 2 Wins!")

	else:
		if player2 == "paper":
			print("Player 1 Wins!")
		elif player2 == "rock":
			print("Player 2 Wins!")

else:
	print("You must enter a valid choice!")