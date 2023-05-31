# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import hangman_picture

word_list = ["test", "monkey", "apple"]
secret_word = random.choice(word_list)
display = []

for i in range(len(secret_word)):
    display += '_'
print(secret_word)
print(display)

guessed_letter = input("Guess a letter: ")

for position in range(len(secret_word)):
    letter = secret_word[position]
    if letter == guessed_letter:
        display[position] = guessed_letter
print(display)
