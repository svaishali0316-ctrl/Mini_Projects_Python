# Stone Paper Scissors

import random

print("=" * 30)
print("    STONE/PAPER/SCISSOR    ")
print("=" * 30)

choices = ["Stone","Paper","Scissor"]

Player = input("Enter Stone, Paper or Scissor: ")

Bot = random.choice(choices)

print("Bot choosing :",Bot)

if Player == Bot:
   print("Its Tie")
elif (Player == "Stone" and Bot == "Scissor") or \
     (Player == "Paper" and Bot == "Stone") or \
     (Player == "Scissor" and Bot == "Paper"):
    print("You Win")
elif Player in choices:
    print("Bot Wins")
else:
    print("Invalid Choices!,Check the input choices.Enter Stone or Paper or Scissor")

