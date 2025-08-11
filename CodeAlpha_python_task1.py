# TASK 1: Hangman Game
# ● Goal: Create a simple text-based Hangman game where the player guesses a word one letter at a time.
# ● Simplified Scope:
# ○ Use a small list of predefined words (no need to use a file or API).
# ○ Limit incorrect guesses to 6.
# ○ Basic console input/output — no graphics or audio.
# ● Key Concepts Used: random, while loop, if-else, strings, lists.

import random
word_list = [
    "puzzle", "rocket", "blanket", "forest", "laptop",
    "python", "island", "wizard", "castle", "jungle",
    "mystery", "camera", "thunder", "mirror", "planet",
    "guitar", "engine", "desert", "travel", "tunnel",
    "orange", "pencil", "secret", "pirate", "dragon",
    "helmet", "circle", "market", "window", "monster",
    "bridge", "galaxy", "shadow", "animal", "school",
    "legend", "garden", "hunter", "rocket", "castle",
    "energy", "castle", "zombie", "banana", "goblin",
    "snowman", "volcano", "treasure", "whistle", "wizard"
]
print(r'''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    ''')
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
chosen_word = random.choice(word_list)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)
game_over = False
correct_letters = []
while not game_over:
    print(f"************************{lives}/6 LIVES LEFT************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"\n***********************IT WAS {chosen_word}..! YOU LOSE**********************")
    if "_" not in display:
        game_over = True
        print("\n**************************YOU WIN****************************")
    print(stages[lives])
    