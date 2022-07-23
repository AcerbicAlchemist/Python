print("Welcome to my super awesome quiz")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

answer = input("How many legs does a stick insect have? ")
if answer == "6":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Can jellyfish see? ")
if answer.lower() == "no":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

answer = input("Can Orca swim? ")
if answer.lower() == "yes":
    print("Correct!")
    score +=1
else:
    print("Incorrect.")

if score >= 2:
    print("Congratulations, you got " + str(score) + " questions correct!")
else:
    print("You got " + str(score) + " questions correct. You can do better next time.")
    