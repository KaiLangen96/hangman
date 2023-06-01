# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import hangman_picture

word_list = ["test", "monkey", "apple"]
secret_word = random.choice(word_list)
display = []
lives = 6
game_over = False
guessed_letter = ''
already_used = []


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
    global lives
    if guessed_letter not in secret_word:
        lives -= 1
        if lives == 0:
            print(hangman_picture.lives_left[lives])
            print("Game over! You lose!")
            return True

    if '_' not in display:
        print("Congratulations! You win!")
        return True

    print(hangman_picture.lives_left[lives])
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


if __name__ == "__main__":
    while True:
        display_home_screen()
        choice = input("Enter your choice:\n")

        if choice == "1":
            display = create_display(secret_word)
            while not game_over:
                print(hangman_picture.lives_left[lives])
                print(display)
                guessed_letter = guess_letter()
                while guessed_letter is False:
                    guessed_letter = guess_letter()
                display = update_display(secret_word, guessed_letter, display)
                print(display)
                game_over = check_game(guessed_letter, secret_word, display)

        elif choice == "2":
            break

        else:
            print("Invalid choice. Please try again.\n")
