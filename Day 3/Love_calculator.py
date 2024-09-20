# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


name1_lower = name1.lower()
name2_lower = name2.lower()

new_name = name1_lower + name2_lower

true = new_name.count("t") + new_name.count("r") + new_name.count("e") + new_name.count("u")
love = new_name.count("l") + new_name.count("o") + new_name.count("v") + new_name.count("e")

score = int(f"{true}" + f"{love}")

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
