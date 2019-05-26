import forca
import adivinhacao


def game_picker():
    print("\n\n*********************************")
    print("******* Choose your game! *******")
    print("*********************************\n")

    print("(1) Forca (2) Adivinhação\n")

    game_of_choice = int(input("What's gonna be? "))

    if game_of_choice == 1:
        print("\nSwitching to Forca.........\n")
        forca.start()
    elif game_of_choice == 2:
        print("\nSwitching to Adivinhacao.........\n")
        adivinhacao.start()


if __name__ == "__main__":
    game_picker()