import random 
def game():

	computer_choice == random.randint(1,3):
	if computer_choice == 1:
		computer_choice_Rock()

	elif computer_choice == 2:
	    computer_choice_Paper()

	else:
	    computer_choice_Scissors()

# When compurer choice is Rock
def computer_choice_Rock():
	player_choice = raw_input("Rock, Paper, Scissors:")

	if player_choice == "Rock":
	   print "You Tie!"
	   try_again()

	if player_choice == "Paper":
	   print "You Win!"
	   try_again()

	elif player_choice == "Scissors":
	   print "You Lose!"
	   try_again()

	else:
		print "Try again"

# When computer choice is Paper
def computer_choice_Paper():
	player_choice = raw_input("Rock, Paper, Scissors")

	if player_choice == "Rock":
	   print "You Lose!"
	   try_again()

	if player_choice == "Paper":
	   print "You Tie!"
	   try_again()

	elif player_choice == "Scissors":
	   print "You Win!"
	   try_again()

	else:
		print "Try again"

# When compter choice is Scissors
def computer_choice_Paper():
	player_choice = raw_input("Rock, Paper, Scissors")

	if player_choice == "Rock":
	   print "You Win!"
	   try_again()

	if player_choice == "Paper":
	   print "You Lose!"
	   try_again()

	elif player_choice == "Scissors":
	   print "You Tie!"
	   try_again()

	else:
		print "Try again"

# Try again function
def try_again():
	choice = raw_input("Please try again Yes/No")

	if choice == "Yes":
		game()

	elif choice == "No":
	    print "Thank you :-)"
	    quit()

	else:
		print "Try again"
		try_again()

game()
