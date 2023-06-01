# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import hangman_picture
import os
from time import sleep

word_list = ["test", "monkey", "apple"]
secret_word = random.choice(word_list)
display = []
lives = 6
game_over = False
guessed_letter = ''
already_used = []
result = ''


def create_display(secret_word):
    """
    Creates the display string with underscores for each character
    from secret_word.
    """
    display = ['_'] * len(secret_word)
    return display


def guess_letter():
    """
    Getting the guess from the user and checking if
    the input was valid.
    """
    guess_letter = input("Please guess a letter and confirm with Enter: \n")
    if len(guess_letter) > 1:
        print("You entered more than one letter!")
        print("Please enter only one letter and confirm with Enter.\n")
        return False
    if guess_letter.isalpha() is False:
        print("You have entered a non-alphabetic character.")
        print("Enter only one alphabetic letter and confirm with Enter.\n")
        return False
    if guess_letter in already_used:
        print(f"{guess_letter} has already been used.")
        return False

    guessed_letter = guess_letter.lower()
    already_used.append(guessed_letter)
    return guessed_letter


def update_display(secret_word, guessed_letter, display):
    """
    Updates the display based on the guessed letter.
    """
    for position in range(len(secret_word)):
        letter = secret_word[position]
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
    print("*{:^58}*".format("1. Start Game"))
    print("*{:^58}*".format("2. Quit"))
    print()
    print("*" * 60)


def display_game_over_screen(result):
    """
    Displays the game over screen for winning or losing.
    """
    clear_screen()
    print("\n" + "*" * 60)
    if result == "win":
        print("*{:^58}*".format("Congratulations! You won!"))
    elif result == "lose":
        print("*{:^58}*".format("Game over! You lost!"))
    print(hangman_picture.lives_left[lives])
    print("*{:^58}*".format(f"Your word was {secret_word}"))
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
    secret_word = random.choice(word_list)
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
                print(hangman_picture.lives_left[lives])
                print(display)
                guessed_letter = guess_letter()
                while guessed_letter is False:
                    guessed_letter = guess_letter()
                display = update_display(secret_word, guessed_letter, display)
                print(display)
                game_over = check_game(guessed_letter, secret_word, display)

                if game_over:
                    while True:
                        display_game_over_screen(result)
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            restart_game()
                            break
                        elif choice == "2":
                            clear_screen()
                            break
                        else:
                            print("Invalid choice. Please try again.\n")
                continue

        elif choice == "2":
            break

        else:
            print("Invalid choice. Please try again.\n")
            clear_screen()
