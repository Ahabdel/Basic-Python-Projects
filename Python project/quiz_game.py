print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Congragulations you are playing")
score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Sorry that's incorrect")
    if score > 0:
        score -= 1

print("Your got " + str(score) + (" questions correct!"))