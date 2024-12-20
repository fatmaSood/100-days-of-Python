# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
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

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game and lives > 0:
    guess = input("Guess a letter: ").lower()

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    if guess not in chosen_word:
        lives -= 1
        # if lives == 5:
        #     print(stages[1])
        #     print(f"Wrong guess! You have {lives} chances left.")
        # if lives == 4:
        #     print(stages[2])
        #     print(f"Wrong guess! You have {lives} chances left.")
        # if lives == 3:
        #     print(stages[3])
        #     print(f"Wrong guess! You have {lives} chances left.")
        # if lives == 2:
        #     print(stages[4])
        #     print(f"Wrong guess! You have {lives} chances left.")
        # if lives == 1:
        #     print(stages[5])
        #     print(f"Wrong guess! You have {lives} chances left.")
    else:
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # If lives goes down to 0 then the game should stop, and it should print "You lose."
    if lives == 0:
        end_of_game = True
        print(stages[6])
        print("You lose!")

        # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

        # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
        #  remaining.
    print(stages[lives])
