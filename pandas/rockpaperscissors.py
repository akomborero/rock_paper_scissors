import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True
if player not in options:
       print("invalid choice")
while running:
        
        player = input("Enter a choice(rock, paper, scissors): ")

        while player not in options:
         player =  input("Enter a choice(rock, paper, scissors): ")

        print(f"player: {player}")
        print(f" computer:{computer}")


        if player == computer:
                print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
                (player == "paper" and computer == "rock") or \
                player == "scissors" and computer == ("paper"):
                print("You win!")
        else:
                print("You lose!")


