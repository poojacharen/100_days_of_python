print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
cross_road = input("You're at a cross road. Where do you want to go?\n   Type 'left' or 'right'\n").lower()

if cross_road == "left":
    swim_wait = input("Which one would you choose?\n Type 'swim' or 'wait'\n").lower()
    if swim_wait == "wait":
       color = input("Choose which door you want to enter? ").lower()
       if color == "yellow":
           print("You Win!!")
       elif color == "blue":
            print("Eaten by Beasts. Game Over!!")
       elif color == "red":
            print("Burned by fire. Game Over!!")
       else:
           print("Sorry you have entered in a wrong door. Game Over!!")
    else:
        print("You have been attacked by a crocodile. Game Over!!")
else:
    print("You have chosen a wrong direction. Game Over!!")
    





