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

if __name__ == "__main__":
    # Creating display with '_' for each letter
    for i in range(len(secret_word)):
        display += '_'
    print(display)

    # Hangman game loop
    while not game_over:
        guessed_letter = input("Guess a letter: ")

        for position in range(len(secret_word)):
            letter = secret_word[position]
            if letter == guessed_letter:
                display[position] = guessed_letter
        print(display)

        if guessed_letter not in secret_word:
            lives -= 1
            if lives == 0:
                game_over = True
                print(hangman_picture.lives_left[lives])
                print("Game over! You lose!")

        if '_' not in display:
            game_over = True
            print("Congratulations! You win!")
        print(hangman_picture.lives_left[lives])
