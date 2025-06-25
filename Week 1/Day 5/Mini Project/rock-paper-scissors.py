from game import Game

def get_user_menu_choice():
    print("\nMenu:")
    print("1. Play a new game")
    print("2. Show scores")
    print("q. Quit")
    choice = input("Enter your choice: ").lower()
    if choice in ['1', '2', 'q']:
        return choice
    print("Invalid choice. Please enter 1, 2, or q.")
    return None

def print_results(results):
    print("\nGame Results Summary:")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("Thank you for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice is None:
            continue
        if choice == '1':
            game = Game()
            result = game.play()
            results[result] += 1
        elif choice == '2':
            print_results(results)
        elif choice == 'q':
            print_results(results)
            print("Exiting the game. Goodbye!")
            break

if __name__ == "__main__":
    main()