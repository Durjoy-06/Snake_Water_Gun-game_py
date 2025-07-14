import random

def snake_water_gun(user, computer):
    if user == computer:
        return "tie"
    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "user"
    else:
        return "computer"

def play_game(rounds):
    user_score = 0
    computer_score = 0
    options = ["snake", "water", "gun"]

    for round in range(1, rounds + 1):
        print(f"\n🔄 Round {round}")
        user_choice = input("Enter your choice (snake, water, gun): ").lower()
        if user_choice not in options:
            print("❌ Invalid choice. Please try again.")
            continue
        computer_choice = random.choice(options)
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = snake_water_gun(user_choice, computer_choice)
        if result == "tie":
            print("Result: 🤝 It's a tie!")
        elif result == "user":
            print("Result: ✅ You win this round!")
            user_score += 1
        else:
            print("Result: ❌ Computer wins this round!")
            computer_score += 1

    print("\n🏁 Final Scores 🏁")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    if user_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif user_score < computer_score:
        print("😅 Sorry! Computer won the game.")
    else:
        print("🤝 It's a draw!")

def main():
    print("🐍💧🔫 Welcome to Snake, Water, Gun Game! 💥")
    while True:
        print("\nMenu:")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            try:
                rounds = int(input("Enter number of rounds you want to play: "))
                play_game(rounds)
            except ValueError:
                print("❌ Please enter a valid number.")
            again = input("\nDo you want to play again? (yes/no): ").lower()
            if again != "yes":
                print("👋 Thanks for playing! Goodbye!")
                break
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid menu choice. Please select 1 or 2.")

main()
