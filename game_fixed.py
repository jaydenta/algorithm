from random import *

def guess_number():
    correctNumber = randint(1,100)
    count = 0
    #print('The correct number is {}'.format(correctNumber))
    userGuess = int(input('Please enter a number between 1 and 100: '))
    while userGuess != correctNumber:
        if userGuess > correctNumber:
            userGuess = int(input('Please pick a smaller number: '))
            count = count + 1
        elif userGuess < correctNumber:
            userGuess = int(input('Please pick a bigger number: '))
            count = count + 1
    print('You are correct!')
    print('It took you {}'.format(count) + ' times to guess it right')
guess_number()