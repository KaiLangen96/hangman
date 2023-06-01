import random
import hangman_picture
import os
from time import sleep
from words import animals

secret_word = random.choice(animals)
display = []
lives = 6
game_over = False
guessed_letter = ''
already_used = []
result = ''


def create_display(secret_word):
    """
    Creates the display string with underscores for each character from
    secret_word.
    """
    display = ['_'] * len(secret_word)
    return display


def guess_letter():
    """
    Getting the guess from the user and checking if the input was valid.
    A valid input is only one alphabetic letter.
    """
    guess_letter = input("Please guess a letter and confirm with Enter:\n")

    if len(guess_letter) > 1:
        print("\033[91mYou entered more than one letter!")
        print("Please enter only one letter.\033[0m\n")
        return False

    if not guess_letter.isalpha():
        print("\033[91mYou have entered a non-alphabetic character.")
        print("Enter only one alphabetic letter.\033[0m\n")
        return False

    if guess_letter in already_used:
        print(f"\033[91m{guess_letter} has already been used.\033[0m")
        return False

    guessed_letter = guess_letter.lower()
    already_used.append(guessed_letter)
    return guessed_letter


def update_display(secret_word, guessed_letter, display):
    """
    Updates the display based on the guessed letter.
    """
    for position, letter in enumerate(secret_word):

        if letter == guessed_letter:
            display[position] = guessed_letter

    return display


def check_game(guessed_letter, secret_word, display):
    """
    Checks the game status after each guess and prints appropriate messages.
    Returns the game over status.
    """
    global lives, result

    if guessed_letter not in secret_word:
        lives -= 1

        if lives == 0:
            result = 'lose'
            return True

    if '_' not in display:
        result = 'win'
        return True

    return False


def display_home_screen():
    """
    Displays the home screen with options to start or quit the game.
    """
    print("*" * 60)
    print()
    print("*{:^58}*".format("Hangman Game"))
    print()
    print("*" * 60)
    print(hangman_picture.lives_left[0])
    print("*" * 60)
    print("*{:^58}*".format("Options:"))
    print()
    print("*{:^58}*".format("1. Start Game"))
    print("*{:^58}*".format("2. Quit"))
    print("*" * 60)


def display_ingame_screen():
    """
    Displays the screen during the game.
    """
    print("*" * 60)
    print()
    print("*{:^58}*".format("Welcome to Hangman!"))
    print()
    print("*" * 60)
    print(hangman_picture.lives_left[lives])
    print("*" * 60)
    print("*{:^58}*".format("Your word is:"))
    print(display)
    print(f"\033[90mUsed: {already_used}\033[0m")
    print("*" * 60)


def display_game_over_screen(result):
    """
    Displays the game over screen for winning or losing.
    """
    clear_screen()
    print("\n" + "*" * 60)
    print()

    if result == "win":
        print("*{:^67}*".format("\033[92mCongratulations! You won!\033[0m"))

    if result == "lose":
        print("*{:^67}*".format("\033[91mGame over! You lost!\033[0m"))

    print("\n" + "*" * 60)
    print(hangman_picture.lives_left[lives])
    print("*{:^67}*".format(f"Your word was \033[33m{secret_word}\033[0m"))
    print("*" * 60)
    print("*{:^58}*".format("Do you want to..."))
    print("*{:^58}*".format("1. Play Again?"))
    print("*{:^58}*".format("2. Go back to Menu?"))
    print("*" * 60)


def restart_game():
    """
    Resets the game variables for a new game.
    """
    global secret_word, display, lives, game_over, guessed_letter, already_used

    secret_word = random.choice(animals)
    display = create_display(secret_word)
    lives = 6
    game_over = False
    guessed_letter = ''
    already_used = []


def clear_screen():
    """
    Function to clear terminal
    """
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":

    while True:
        display_home_screen()
        choice = input("Enter your choice:\n")

        if choice == "1":
            restart_game()

            while not game_over:
                clear_screen()
                display_ingame_screen()
                guessed_letter = guess_letter()

                while guessed_letter is False:
                    guessed_letter = guess_letter()

                display = update_display(secret_word, guessed_letter, display)
                print(display)
                game_over = check_game(guessed_letter, secret_word, display)

                if game_over:

                    while True:
                        display_game_over_screen(result)
                        choice = input("Enter your choice:\n")

                        if choice == "1":
                            restart_game()
                            break
                        elif choice == "2":
                            clear_screen()
                            break
                        else:
                            print("\033[91mInvalid choice.")
                            print("Please try again.\033[0m\n")
                continue

        elif choice == "2":
            break

        else:
            print("\033[91mInvalid choice. Please try again.\033[0m\n")
            clear_screen()
