rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if user_input == "0":
    print(rock)
elif user_input == "1":
    print(paper)
elif user_input == "2":
    print(scissors)
else:
    print("Invalid Input")

choice = [rock, paper, scissors]
random_choice = random.choice(choice)
print(random_choice)

if (user_input == scissors) and (random_choice == paper):
    print("you lose")
    if (user_input == paper) and (random_choice == scissors):
        print("You win")
elif (user_input == paper) and (random_choice == rock):
    print("you lose")
    if (user_input == rock) and (random_choice == paper):
        print("You win")
elif (user_input == rock) and (random_choice == scissors):
    print("you lose")
    if (user_input == scissors) and (random_choice == rock):
        print("You win")
else:
    print("It is a draw")
