import random
my_number = random.randint(1, 100)
guess = 0

while guess != my_number:
    guess = int(input("Your guess (0 to give up)? "))
    if guess == 0:
        print("Sorry that you're giving up!")
        break
    elif guess > my_number:
        print("Guess was too high")
    else:
        print("Guess was too low")
else:
    print("Congratulations. You guessed it!")
