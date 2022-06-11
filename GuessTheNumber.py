import random

number_range = input("Type the number range from 0 to : ")

if number_range.isdigit():
    number_range = int(number_range)

    if number_range == 0:
        print("Enter a number greater than 0 next time")
        quit()

else:
    print("Enter a number next time")
    quit()

random_number = random.randint(0, number_range)
no_of_tries = 0

while True:
    no_of_tries +=1
    user_guess = input("Enter your guess : ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess > number_range:
            print("Your guess should be below", number_range,)
            continue
    else:
        print("Enter a number next time")
        continue

    if user_guess == random_number:
        print("Congradulation!!! You guess it correctly")
        break
    elif user_guess > random_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

print("You got", no_of_tries, "tries to guess the correct number")