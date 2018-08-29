from random import *

def guess_number():
	count = 0
	correctNumber = randint(1,100)
	print('The correct number is {}'.format(correctNumber))
	userGuess = int(input('Please enter a number between 1 and 100: '))
	if userGuess == correctNumber:
		print('You are correct! It is your first try too')
		exit()
	while userGuess < correctNumber:
		userGuess = int(input('You need to choose a bigger number: '))
		count = count + 1
		print(count)
		if userGuess == correctNumber:
				print('You are correct! It took you {}'.format(count) + ' times to guess it right')
				exit()
		while userGuess > correctNumber:
			userGuess = int(input('You need to choose a smaller number: '))
			count = count + 1
			print(count)
			if userGuess == correctNumber:
				print('You are correct! It took you {}'.format(count) + ' times to guess it right')
				exit()
	while userGuess > correctNumber:
		userGuess = int(input('You need to choose a smaller number: '))
		count = count + 1
		print(count)
		if userGuess == correctNumber:
				print('You are correct! It took you {}'.format(count) + ' times to guess it right')
				exit()
		while userGuess < correctNumber:
			userGuess = int(input('You need to choose a bigger number: '))
			count = count + 1
			print(count)
			if userGuess == correctNumber:
				print('You are correct! It took you {}'.format(count) + ' times to guess it right')
				exit()

guess_number()