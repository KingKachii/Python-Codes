print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
stage_1 = input(
    "Stage 1: You are at a crossroads. Where do you want to go? Left or Right?\n"
)
stage_one = stage_1.lower()
if stage_one == "left":
    print("Good choice: Proceed to Stage 2")
    print()
    stage_2 = input(
        "Stage 2: You have reached a lake. Do you want to swim or wait? Swim or Wait?\n"
    )
    stage_two = stage_2.lower()
    if stage_two == "wait":
        print("Good choice: Take the boat and proceed to the next stage")
        print()
        print(
            "Stage 3. You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue."
        )
        stage_3 = input("Which colour do you choose? Red, Yellow or Blue?\n")
        stage_three = stage_3.lower()
        if stage_three == "yellow":
            print("Congratulations! You found the treasure. You win!")

        elif stage_three == "red":
            print("You were burned by fire. Game over.")

        elif stage_three == "blue":
            print("You were eaten by beasts. Game over.")

    else:
        print("You were attacked by a trout. Game over.")
else:
    print("You fell into a hole. Game over.")

