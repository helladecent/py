#libz
import random

#game elements
strikes = 0
max_strikes = 3
strikes_left = 3
rps_list = ["rock", "paper", "scissors"]

#start the game
player_1_choice = input("Rock, Paper, or Scissors?")

#check for valid input, shame player if invalid
while player_1_choice != "rock" or "paper" or "scissors":
    while strikes_left >= 1:
        strikes_left -= 1
        print(f"follow the rules, fucker. {player_1_choice} is not an option. You now have {strikes_left} Strikes left")
        strikes += 1
        if strikes_left == 0:
            print("you suck, rerun the game if you want to try again")
            exit()
        player_1_choice = input("Rock, Paper, or Scissors?")

player_2_choice = random.choice(rps_list)

print("----------")
print("ROCK...")
print("PAPER...")
print("SCISSORS...")
print("----brought to you by whythefuckdidImakethis labs------")
print("---S H O O T---")


print(f"YOU chose {player_1_choice}")
print(f"random() chose {player_2_choice}")
print("----------")

if player_1_choice == player_2_choice:
    print("It's a TIE!")
elif player_1_choice == "rock" and player_2_choice == "scissors":
    print("YOU win!")
elif player_1_choice == "scissors" and player_2_choice == "paper":
    print("YOU win!")
elif player_1_choice == "paper" and player_2_choice == "rock":
    print("YOU win!")
else:
    print("Random() wins!")