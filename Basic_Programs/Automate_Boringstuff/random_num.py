from random import randint


secret_num = randint(1,20)

for guesses in range(6):
    print("Guess a number")
    guess=int(input())
    if guess<secret_num:
        print("Guess is too low!")
    elif guess>secret_num:
        print("Guess is too high!")
    else:
        break
if guess==secret_num:
    print("Your Guess is correct")
else:
    print(f"Lost your Guessing attempts:Correct number was {secret_num} ")





