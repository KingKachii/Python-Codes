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

print("Welcome to the Rock, Paper, Scissors game!")
import random

print()
print("To play, please follow the instructions below:")
print('''
Type 
0 for Rock, 
1 for Paper or 
2 for Scissors.
''')
print()
user_choice = int(input("What do you choose? \n"))
computer = random.randint(0, 2)

#User Choices
if user_choice == 0:
    x = "rock"
    print(f"You chose {x}:\n{rock}")

elif user_choice == 1:
    x = "paper"
    print(f"You chose {x}:\n{paper}")

else:
    x = "scissors"
    print(f"You chose {x}:\n{scissors}")

#Random Conputer Choices
if computer == 0:
    x = "rock"
    y = rock

elif computer == 1:
    x = "paper"
    y = paper

else:
    x = "scissors"
    y = scissors
print(f"Computer chose {x}:\n{y}")

#Game Logic: Trick is to encode all possibilities where the user wins and set the conditions to lose.
if user_choice == 0 and computer == 2:
    print("You win")
    print("Thank you for playing!")
elif user_choice == 2 and computer == 1:
    print("You win")
elif user_choice == 1 and computer == 0:
    print("You win")
elif user_choice == computer:
    print("It's a draw")
else:
    print("You lose")
    print("Try again!")
