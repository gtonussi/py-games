import random


def start():
    print("\n\n****************************************")
    print("***** Welcome to the Guessing Game *****")
    print("****************************************\n")

    print("I want to know how much of a psychic you are. I'm thinking of a number, can you guess it?")

    print("Keep in mind that I will set a score for you. You start with 1000 points.\n"
          "Each time you try, and miss, I will calculate the distance between your shoot, and the secret number.\n"
          "Then, I will subtract that value of your initial points. "
          "The higher number you end with, the better you are.\n")

    print("All right, enough talking! LET'S PLAY!! \n")

    secret_number = random.randrange(1, 101)
    number_of_tries = 0
    winner = False
    points = 1000

    print("Do you want to reveal the number? (FOR TESTING PURPOSES)")
    reveal = input("Type 'yes' or 'no': ")
    if reveal == "yes":
        print(f"\nWell, either you are the Creator or a smelly cheater: {secret_number}\n")
    else:
        print("\nWise man. It is said that non-cheaters have more sex.\n")

    print("(1) Easy - 30 rounds\n"
          "(2) Medium - 20 rounds\n"
          "(3) Hard - 10 rounds\n"
          "(4) Psychic - Single round")
    level = int(input("Choose your difficulty level: "))

    if level == 1:
        number_of_tries = 30
    elif level == 2:
        number_of_tries = 20
    elif level == 3:
        number_of_tries = 10
    else:
        number_of_tries = 1

    for round_number in range(1, number_of_tries + 1):

        print(f"\n********* ROUND {round_number}/{number_of_tries} **********\n")

        shoot = int(input("Insert any number from 1 to 100: "))

        print("\nYou have tried:", shoot)
        print("Let me think......\n")

        if shoot < 1 or shoot > 100:
            print("You must enter a number between 1 and 100. Try Again!")
            continue

        guessed_right = shoot == secret_number
        guessed_bigger = shoot > secret_number
        guessed_lower = shoot < secret_number

        if guessed_right:
            print("You have guessed it right! Congratulations!")
            print(f"Your score: {points} points.\n")
            winner = True
            break
        else:
            if guessed_bigger:
                print("Oh crap! You guesses it wrong! The number is lower than that.")
            elif guessed_lower:
                print("Oh crap! You guessed it wrong! The number is higher than that.")

            lost_points = abs(secret_number - shoot)
            points = points - lost_points

    if winner is False:
        print(f"The secret number was {secret_number}")

    print("End Game. Thank you for playing!")


if __name__ == "__main__":
    start()