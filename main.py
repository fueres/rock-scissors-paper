import random

choices = ["rock", "paper", "scissors"]

play_times = 0
player_wins = 0
computer_wins = 0

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("\nrock, scissors or paper? ").lower()

    # the choices
    print("computer: ",computer)
    print("player: ",player)

    # who won
    if player == computer:
        print("tie!\n")
    
    elif player == "rock":
        if computer == "paper":
            print("You lose\n")
            computer_wins += 1
        if computer == "scissors":
            print("You win\n")
            player_wins += 1
    
    elif player == "scissors":
        if computer == "rock":
            print("You lose\n")
            computer_wins += 1
        if computer == "paper":
            print("You win\n")
            player_wins += 1
    
    elif player == "paper":
        if computer == "scissors":
            print("You lose\n")
            computer_wins += 1
        if computer == "rock":
            print("You win\n")
            player_wins += 1

    play_times += 1

    play_again = input("Another try? (yes/no) ").lower()

    if play_again != "yes":
        break

print("\nYou played "+str(play_times)+" times\nYou won "+str(player_wins)+"\nComputer won "+str(computer_wins)+"\nBye!\n")