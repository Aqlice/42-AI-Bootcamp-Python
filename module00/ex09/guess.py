import random
import sys

secret_number = random.randint(0, 99)
print(f'This is an interactive guessing game!'
      f'You have to enter a number between 1 and 99 to find out the secret number.'
      f'Type "exit" to end the game.'
      f'Good luck!')
number_try = 0
guess = input()
while guess != 'exit':
    try:
        guess = int(guess)
        if guess == secret_number and secret_number == 42:
            sys.exit("The answer to the ultimate question of life, the universe and everything is 42.")
        if guess == secret_number and number_try == 1:
            sys.exit("Congratz you won on first try") 
        if guess == secret_number:
            sys.exit(f"Congratulations, you've got it!"
                  f'You won in {number_try} attempts!')
        elif guess < secret_number:
            print("too low")
        elif guess > secret_number:
            print("too high")
        number_try += 1
        guess = input()
    except ValueError:
        print("That's not a number.")
        guess = input()