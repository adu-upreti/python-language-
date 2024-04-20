
import random
random_number = random.randint(1, 100)
print("random number:", random_number)

guesses = 0

while True:
    num = int(input("Enter the guessing Value:"))
    guesses += 1

    if num == random_number:
        print("Congrats!", num, "is correct number. you have guessed the answer in just", guesses, "time.")
        break
    elif num < random_number:
        print("hints. just above than your input")
    else:
        print("hints. just less than your input")
