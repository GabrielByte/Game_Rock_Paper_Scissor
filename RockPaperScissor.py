''' 
    This is a Rock, Paper and Scissors game
    Rock = o
    Paper = __
    Scissor = >8
'''

# This function will generate a rondom number to decide between Rock, Paper and Scissors
from random import randint  

# It will take your choice
player = input ("Rock (R), Paper (P) or Scissor (S)? ").upper()

# It takes your choice and "Transform" them into a figure
if player == "R":
    print("o", end="")

elif player == "P":
    print("__", end="")

elif player == "S":
    print(">8", end="")

else:
    print("x_x")

# Here we say to randint the numbers that it can choose
chosen = randint (1,3)

# And here we have the number and what they "mean" 
# 1 = R (Which means the number 1 is Rock) and so on
if chosen == 1:
    computer = "R"
    print (" Vs o")

elif chosen == 2:
    computer = "P"
    print (" Vs __")

else:
    computer = "S"
    print (" Vs >8")

# If your choice and the computer were the same, the terminal will print this out
if player == computer:
    print ("DRAW!")

# Otherwise it will print one of these out
elif player == "R" and computer == "S":
    print ("Player wins!")

elif player == "S" and computer == "P":
    print ("Player wins!")

elif player == "P" and computer == "R":
    print ("Player wins!")

elif player == "S" and computer == "R":
    print ("Computer wins!")

elif player == "P" and computer == "S":
    print ("Computer wins!")

elif player == "R" and computer == "P":
    print ("Computer wins!")