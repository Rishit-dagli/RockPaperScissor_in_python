from random import randint 
msg=input("Do you want to play:")
while msg != "y"or"Y"or"yes"or"Yes":
	#p=players move
	p=input("Player make your move").lower()
	#n=number
	n=randint(0,2)
	if n==0:
	#c=computers move	
		c="rock"
	elif n==1:
	#c=computers move	
		c="paper"
	else:
	#c=computers move	
		c="scissor"

	print(f"computer plays {c}")

	if p==c:
		print("it is a tie")
	elif p=="rock":
		if c=="scissor":
			print("player wins")
		else:
			print("computer wins")
	elif p=="paper":
		if c=="scissor":
			print("computer wins")
		else:
			print("plater wins")
			
	elif p=="scissor":
		if c=="rock":
			print("player wins")
		else:
			print("computer wins")
	else:
		print("error")