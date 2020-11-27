import random
tie_score = int()
winning_score = int()
loosing_score = int()
internal_player = ["rock", "paper", "scissors"]
#user_input = print(input("Please make a choice; rock, paper, scissors"))

play_again = 'y'
count = 0

while play_again == "y":
    internal_player_choice = random.choice(internal_player)
    #print(internal_player_choice)
    user_input = input("Please make a choice; rock, paper, scissors: ")
    if user_input == internal_player_choice:
        print("It's a tie")
        tie_score += 1
        #print(internal_player_choice)
    elif user_input == "rock" and internal_player_choice == "scissors":
        winning_score += 1
        print("you won")
        #print(internal_player_choice)
    elif user_input == "scissors" and internal_player_choice == "paper":
        winning_score += 1
        print("you won")
        #print(internal_player_choice)
    elif user_input == "paper" and internal_player_choice == "rock":
        winning_score += 1
        print("you won")
        #print(internal_player_choice)
    else:
        loosing_score += 1
        print("you lost")
        print(user_input)
        #print(internal_player_choice)
    count += 1
    play_again = input("Would you like to play again? Enter y = Yes, or n = No: ")
print("you won", winning_score, "out of", count)
print("you lost", loosing_score, "out of", count)
print(tie_score, "was tied")
percentage = ((winning_score * 100)/count)
print("Your winning_percentage is: ", percentage)
