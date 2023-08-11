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
0
import random

str_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
num = int(str_choice)
game = [rock , paper , scissors]
computer = random.choice(game)

if num == 0:
  print(rock)
  print("Computer chose:")
  print(computer)
  if computer == rock:
    print("Both are same. Try again!")
  elif computer == paper:
    print("You lost")
  else: 
    print("You won")
elif num == 1:
  print(paper)
  print("Computer chose:")
  print(computer)
  if computer == paper:
    print("Both are same. Try again!")
  elif computer ==  scissors:
    print("You lost")
  else: 
    print("You won")
elif num == 2:
  print(scissors)
  print("Computer chose:")
  print(computer)
  if computer == rock:
    print("You lost")
  elif computer == scissors:
    print("Both are same. Try again!")
  else: 
    print("You won")
else:
  print("You chose something else. Game Over!")


