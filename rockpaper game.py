# Rock, Paper, Scissors Game

import random


def get_computer_choice():
    """Computer randomly picks Rock, Paper, or Scissors"""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    """Determine the winner of the game"""
    user_choice = user_choice.lower()
    
    if user_choice == computer_choice:
        return "Tie"
    
    # Rock beats Scissors
    if user_choice == "rock" and computer_choice == "scissors":
        return "You Win! 🎉"
    # Paper beats Rock
    elif user_choice == "paper" and computer_choice == "rock":
        return "You Win! 🎉"
    # Scissors beats Paper
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You Win! 🎉"
    else:
        return "Computer Wins! 🤖"


def display_game_info(user_choice, computer_choice, result):
    """Display game results"""
    print("\n" + "=" * 50)
    print("GAME RESULTS")
    print("=" * 50)
    print(f"You chose:     {user_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    print(f"Result: {result}")
    print("=" * 50)


def main():
    print("\n" + "=" * 50)
    print("🎮 ROCK, PAPER, SCISSORS GAME 🎮")
    print("=" * 50)
    
    score_user = 0
    score_computer = 0
    
    while True:
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Show Score")
        print("5. Exit")
        
        choice_input = input("\nEnter your choice (1/2/3/4/5): ").strip()
        
        if choice_input == "1":
            user_choice = "rock"
        elif choice_input == "2":
            user_choice = "paper"
        elif choice_input == "3":
            user_choice = "scissors"
        elif choice_input == "4":
            print("\n" + "=" * 50)
            print("SCORE")
            print("=" * 50)
            print(f"You: {score_user}")
            print(f"Computer: {score_computer}")
            print("=" * 50)
            continue
        elif choice_input == "5":
            print("\n" + "=" * 50)
            print("FINAL SCORE")
            print("=" * 50)
            print(f"You: {score_user}")
            print(f"Computer: {score_computer}")
            if score_user > score_computer:
                print("🏆 You are the champion!")
            elif score_user < score_computer:
                print("🤖 Computer is the champion!")
            else:
                print("🤝 It's a tie!")
            print("=" * 50)
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-5.")
            continue
        
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        display_game_info(user_choice, computer_choice, result)
        
        if "Win" in result:
            score_user += 1
        elif "Computer" in result:
            score_computer += 1


if __name__ == "__main__":
    main()
