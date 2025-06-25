import random

class Game:
    def __init__(self):
        self.valid_items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        while True:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in self.valid_items:
                return choice
            print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(self.valid_items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "paper" and computer_item == "rock") or \
             (user_item == "scissors" and computer_item == "paper"):
            return "win"
        else:
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        if result == "win":
            print(f"You selected {user_item}. The computer selected {computer_item}. You win!")
        elif result == "loss":
            print(f"You selected {user_item}. The computer selected {computer_item}. You lose.")
        else:
            print(f"You selected {user_item}. The computer selected {computer_item}. You drew!")

        return result