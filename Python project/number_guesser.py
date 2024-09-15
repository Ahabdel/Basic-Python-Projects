import random

top_of_range = input("Input a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Please enter a number.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    guess_a_number = input("Guess a number: ")
    if guess_a_number.isdigit():
        guess_a_number = int(guess_a_number)
    
        if guess_a_number < 0:
            print("Please type a number more than zero next time.")
            continue
        if guess_a_number > 10:
            print("Please type a number that is 0-10 next time.")
            continue  
    else:
        print("Please enter a number.")
        continue

    if random_number == guess_a_number:
        print("Congragulations you guessed right! The number was " + str(random_number) + "." + " You guessed it in " + str(guesses) + " tries, good job!")
        break
    else:
        print("Sorry you guess wrong, try again.")
        