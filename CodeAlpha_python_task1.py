# TASK 1: Hangman Game
# ● Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
# ● Simplified Scope:
# ○ Use a small list of 5 predefined words (no need to use a file or API).
# ○ Limit incorrect guesses to 6.
# ○ Basic console input/output — no graphics or audio.
# ● Key Concepts Used: random, while loop, if-else, strings, lists.

import random

# List of possible words for the game
words = ["apple", "banana", "grape", "orange", "peach"]
# Randomly select a word from the list
word = random.choice(words)
# Set of unique letters in the chosen word
word_letters = set(word)
# Set to keep track of letters guessed by the player
guessed_letters = set()
# Counter for wrong guesses
wrong_guesses = 0
# Maximum number of allowed wrong guesses
max_wrong = 6

# Game introduction
print("Welcome to Hangman!")

# Main game loop: continues until player runs out of guesses or guesses all letters
while wrong_guesses < max_wrong and word_letters:
    # Display the current state of the word with guessed letters revealed
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("Word:", " ".join(display))
    # Show the letters guessed so far
    print(f'Guessed letters: {" ".join(sorted(guessed_letters))}')
    # Show remaining wrong guesses
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
    # Prompt the player to guess a letter
    guess = input("Guess a letter: ").lower()
    # Validate input: must be a single alphabetic character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic character.")
        continue
    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    # Add the guessed letter to the set
    guessed_letters.add(guess)
    # Check if the guessed letter is in the word
    if guess in word_letters:
        word_letters.remove(guess)
        print("Good guess!")
    else:
        # Increment wrong guess counter if guess is incorrect
        wrong_guesses += 1
        print("Wrong guess!")

# Game over: check win or lose condition
if not word_letters:
    # Player guessed all letters
    print(f"Congratulations! You guessed the word: {word}")
else:
    # Player ran out of guesses
    print(f"Sorry, you lost. The word was: {word}")
