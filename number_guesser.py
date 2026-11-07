import random

user_number = input("Type a number : ")

if user_number.isdigit():
    user_number = int(user_number)

    if user_number <= 0:
        print("Please type a number larger than 0 next time.")
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, user_number) 
guesses = 0

while True:
    guesses += 1
    user_guesses = input("Make a guess: ")
    if user_guesses.isdigit():
        user_guesses = int(user_guesses)
    else:
        print("please type a number next time.")
        continue

    if user_guesses == random_number:
        print("This is correct guess.")
        break
    elif user_guesses > random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print(f"You go it in {guesses} guesses") 
           