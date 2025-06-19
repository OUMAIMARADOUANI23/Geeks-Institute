import random
wins = 0
losses = 0

print("Welcome to the guessing game!")
print("Guess a number from 1 to 9. Type 'quit' to exit.")

while True:
    user_input = input("Enter a number between 1 and 9 (or 'quit' to stop): ")

    if user_input.lower() == 'quit':
        break  

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    if guess < 1 or guess > 9:
        print("Number must be between 1 and 9.")
        continue

    random_number = random.randint(1, 9)

    if guess == random_number:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time. The number was ." ,random_number)
        losses += 1

print("Game Over!")
print("Total Wins:", wins)
print("Total Losses: ",losses)