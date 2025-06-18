user_word = input("Enter a word: ")

result = ""

for i in range(len(user_word)):
    if i == 0 or user_word[i] != user_word[i - 1]:
        result += user_word[i]

print("Cleaned word:", result)