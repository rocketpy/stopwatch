import random

guess_number = 0

number = random.randint(1, 20)

print('Guess number between 1 and 20')

while guess_number < 5:

    guess = int(input('Take a guess : '))

    guess_number += 1

    if guess < number:
        print('Your guess is low ')

    if guess > number:
        print('Your guess is heigh')

    if guess == number:
        break

if guess == number:
    print('You guess a number !')
else:
    print('You not guess a number ! Number was a : ', number)




