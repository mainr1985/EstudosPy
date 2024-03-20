import random

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

print("Welcome to Rock, Paper, Scissors - Python Edition!")
choice1 = int(
    input(
        "Which do you want? Press 0 for Rock, 1 for Paper or 2 for Scissors: \n"
    ))
if choice1 == 0:
    print("You chose Rock:")
    print(rock)
elif choice1 == 1:
    print("You chose Paper:")
    print(paper)
elif choice1 == 2:
    print("You chose Scissors:")
    print(scissors)

#escolha do computador
choice2 = random.randint(0, 2)
if choice2 == 0:
    print("The computer chose Rock:")
    print(rock)
    if choice1 == 1:
        print("Paper covers rock - you win! :D ")
    elif choice1 == 2:
        print("Rock crushes Scissors - you lose. :( ")   
    
elif choice2 == 1:
  print("The computer chose Paper:")
  print(paper)
  if choice1 == 0:
    print("Paper covers rock - you lose! :( ")  
  elif choice1 == 2:
    print("Scissors cuts Paper - you win! :D ")   

elif choice2 == 2:
  print("The computer chose Scissors:")
  print (scissors)
  if choice1 == 0:
    print("Rock crushes Scissors - you win! :D ")
  elif choice1 == 1:
    print("Scissors cuts Paper - you lose! :( ")   

if choice1==choice2:
    print("It's a tie. Go again.")
  