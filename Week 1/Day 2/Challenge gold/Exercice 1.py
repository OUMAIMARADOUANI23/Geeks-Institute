def letter_indices(word):
    result = {}
    for index, letter in enumerate(word):
        if letter in result:
            result[letter].append(index)
        else:
            result[letter] = [index]
    return result

user_word = input("Enter a word: ")
output = letter_indices(user_word)
print(output)
