from random import randint
winning=2
#scores
comp=0
p=0
#scores

while p<winning and comp<winning: 
	rand_num = randint(0,2)
	print(f"computer score:{comp} player score:{p}\n")
	player = input("Player, make your move: \n").lower()
	if player=="quit" or player=="q":
		break
	if rand_num == 0:
		computer = "rock"

	elif rand_num == 1:
		computer = "paper"

	else:
		computer = "scissors"

	print(f"Computer plays {computer} \n" )

	if player == computer:
		print("It's a tie!\n")

	elif player == "rock":
		if computer == "scissors":
			print("player wins!\n")
			p+=1
		else:
			print("computer wins!\n")
			comp+=1
	elif player == "paper":
		if computer == "rock":
			print("player wins!\n")
			p+=1
		else:
			print("computer wins!\n")
			comp+=1
	elif player == "scissors":
		if computer == "paper":
			print("player wins!\n")
			p+=1
		else:
			print("computer wins!\n")
			comp+=1
	else:
			print("Please enter a valid move!\n")
if comp>p:
	print("the computer wins")
elif p>comp:
	print("the player wins")
else :
	print("its a tie")