import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def display_result(player_choice, computer_choice, winner):
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to stop playing: ").lower()
        if player_choice == "quit":
            break
        elif player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = get_computer_choice()
        winner = get_winner(player_choice, computer_choice)
        display_result(player_choice, computer_choice, winner)

        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score: You {player_score} - {computer_score} Computer")
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"\nFinal Score: You {player_score} - {computer_score} Computer")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
