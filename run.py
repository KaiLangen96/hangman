# external imports
import gspread
from google.oauth2.service_account import Credentials

# internal imports
import random
import hangman_picture
import os
from time import sleep
from words import animals

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman_Highscores')

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
    print("*{:^58}*".format("Welcome to my Animal Hangman Game"))
    print()
    print("*" * 60)
    print(hangman_picture.lives_left[0])
    print("*" * 60)
    print("*{:^58}*".format("Options:"))
    print("*{:^58}*".format("1. Start Game"))
    print("*{:^58}*".format("2. Highscores"))
    print("*{:^58}*".format("3. Quit"))
    print("*" * 60)


def display_ingame_screen():
    """
    Displays the screen during the game.
    """
    print("*" * 60)
    print()
    print("*{:^58}*".format("Guess the animal!"))
    print()
    print("*" * 60)
    print(hangman_picture.lives_left[lives])
    print("*" * 60)
    print("*{:^58}*".format("Your animal is:"))
    print("*{:^58}*".format(f"{display}"))
    print("*{:^67}*".format(f"\033[90mUsed: {already_used}\033[0m"))
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
    print("*{:^58}*".format("2. Save your score?"))
    print("*{:^58}*".format("3. Go back to Menu?"))
    print("*" * 60)


def display_highscore_screen():
    """
    Displays the highscores of the top ten players.
    """
    print("*" * 60)
    print()
    print("*{:^58}*".format("Top 10 Highscores!"))
    print()
    print("*" * 60)
    print("*{:^58}*".format("HIGHSCORES"))
    top_ten_scores()
    print("*" * 60)
    print("*{:^58}*".format("Good Luck in your game!"))
    print("*{:^58}*".format("I'm sure you can make it"))
    print("*{:^58}*".format("into the highscores!"))
    print("*" * 60)


def top_ten_scores():
    """
    Displays the top 10 scores, saved in an external document.
    """
    scores_sheet = SHEET.worksheet("scores").get_all_values()[1:]
    ordered_scores = sorted(scores_sheet, key=lambda d: int(d[1]))
    for high_score in reversed(ordered_scores[-10:]):
        print("*{:^58}*".format(f"{high_score[0]}: {high_score[1]}"))


def save_user_score(score):
    """
    Function to save the players score and
    upload it to a google spreadsheet.
    """
    username = input("Enter your username:\n")
    print("Saving your score...")
    scores_sheet = SHEET.worksheet("scores")
    scores_sheet.append_row([username, score])


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
    Function to clear terminal.
    """
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    while True:
        clear_screen()
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
                        choice = input("I want to...\n")
                        if choice == "1":
                            restart_game()
                            break
                        if choice == "2":
                            score = lives * 15
                            save_user_score(score)
                            print("Highscore saved!")
                            print("Going back to menu...")
                            sleep(5)
                            break
                        if choice == "3":
                            clear_screen()
                            display_home_screen()
                            break
                        else:
                            print("\033[91mInvalid choice.")
                            print("Please try again.\033[0m\n")
                    continue
            continue
        if choice == "2":
            clear_screen()
            display_highscore_screen()
            while True:
                choice = input("Press Enter to go back to the menu\n")
                if choice == "":
                    break
                else:
                    print("\033[91mPress only Enter!\033[0m\n")
            continue
        if choice == "3":
            break
        else:
            print("\033[91mInvalid choice. Please try again.\033[0m\n")
