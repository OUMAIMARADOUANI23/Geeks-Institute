import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    count = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:
            return count

def main():
    all_throws = [] 

    for _ in range(100):
        throws_needed = throw_until_doubles()
        all_throws.append(throws_needed)

    total_throws = sum(all_throws)
    average_throws = total_throws / len(all_throws)

    print(f"🎯 Total de lancers pour 100 doubles : {total_throws}")
    print(f"📊 Moyenne de lancers pour atteindre un double : {average_throws:.2f}")

main()
