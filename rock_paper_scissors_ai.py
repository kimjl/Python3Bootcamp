import random

player_wins = 0
computer_wins = 0
winning_score = 3

print(f'Playing best of {winning_score}.')

while player_wins < winning_score and computer_wins < winning_score:
	print(f'Player Score: {player_wins}. Computer Score: {computer_wins}.')
	print('...rock...')
	print('...paper...')
	print('...scissors...')

	player = input('Player play your hand: ').lower()
	if player == 'quit' or player == 'q':
		break

	rand_num = random.randint(0, 2)
	if rand_num == 0:
		computer = 'rock'
	elif rand_num == 1:
		computer = 'paper'
	else:
		computer = 'scissors'

	print(f'Computer played {computer}')

	if player == computer:
		print('Your both tied')
	elif player == 'rock':
		if computer =='scissors':
			print('Player wins')
			player_wins += 1
		elif computer == 'paper':
			print('Computer wins')
			computer_wins += 1
	elif player == 'paper':
		if computer == 'rock':
			print('Player wins')
			player_wins += 1
		elif computer == 'scissors':
			print('Computer wins')
			computer_wins += 1
	elif player == 'scissors':
		if computer == 'paper':
			print('Player wins')
			player_wins += 1
		elif computer == 'rock':
			print('Computer wins')
			computer_wins += 1
	else:
		print('Something went wrong')

if player_wins > computer_wins:
	print('Congratulations, you won!')
elif player_wins == computer_wins:
	print('You both tied.')
else:
	print('Oh no, Computer won.')

print(f'Final Score: Player {player_wins}, Computer {computer_wins}')