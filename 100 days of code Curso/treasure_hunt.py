print('''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island!\n Your mission is to find the lost treasure of the Sea People")
direction = input("\nThe map says to go straight ahead for a hundred yards. You do, and enter a dense forest. You can proceed to the left or the right. Which do you choose?\n")
if direction.lower()=="right":
    print("\n=> Oops! You stepped over some leaves and straight into the hole they were covering. Game Over.")
elif direction.lower() == "left":
    swim_wait = input("=> \nYou go left and after a few more yards a river emerges. There's no other way but through it. Do you swim or wait for a boat to show up?\n")
    if swim_wait.lower() == "swim":
        print("=> The river currents are stronger than they look and you were never a good swimmer to begin with. You get pulled under and drown. Game over.")
    elif swim_wait.lower() == "wait":
        print("\n => It takes over an hour, but eventually a couple of indians show up on a boat and agree to give you a ride in exchange for your lovely thrift store necklace. \n The search continues!")

door = input("\n Finally across the lake, you come to a patch of grass with three cabins, side by side. Their only doors are painted Red, Blue and Yellow, respectively. Which door do you choose?\n")        
if door.lower() == "blue":
    print("\n => Oops, IT WAS A TRAP! Turns out you're not the only treasure hunter in this island. You are ambushed and are no match to their shotguns. Game Over.")
elif door.lower() == "red":
    print("\n => Red's always been a synonym for danger, and this case is no different. As soon as you walk through, you step on something that clicks. A second later, arrows come flying at you seemingly out of nowhere. 'A trap', you realize too late. Game over.")
elif door.lower() == "yellow":
    print("\n => Carefully you search inside until you find a switch on a wall that opens up a trap door. \n   Going down countless steps, you marvel at the amount of gold and jewels scattered in the cave you've just entered. \n 'Goodbye, money problems!', you grin")
    print('''                ___
            ,-'"   "`-.
          ,'_          `.  
         / / \  ,-       \ 
    __   | \_0 ---        |
   /  |  |                |
   \  \  `--.______,-/    |
 ___)  \  ,--""    ,/     |
/    _  \ \-_____,-      / 
\__-/ \  | `.          ,'  
  \___/ <    �--------'    
   \__/\ | Wny             
    \__//
''')
    print("Game over! You won!")