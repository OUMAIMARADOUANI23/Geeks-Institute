import re

paragraph = "Education is the most powerful weapon which you can use to change the world. It empowers individuals, strengthens communities, and creates opportunities for a better future. With knowledge, people can make informed decisions and shape their own destinies."

paragraph_clean = paragraph.strip()

char_count = len(paragraph_clean)

non_whitespace_count = len(paragraph_clean.replace(" ", "").replace("\n", ""))

sentences = re.split(r'[.!?]\s*', paragraph_clean)

if sentences[-1] == '':
    sentences.pop()
sentence_count = len(sentences)

words = re.findall(r'\b\w+\b', paragraph_clean.lower())
word_count = len(words)

unique_words = set(words)
unique_word_count = len(unique_words)

non_unique_word_count = word_count - unique_word_count

average_words_per_sentence = word_count / sentence_count if sentence_count != 0 else 0

print("----- Paragraph Analysis -----")
print(f"Total characters: {char_count}")
print(f"Total sentences: {sentence_count}")
print(f"Total words: {word_count}")
print(f"Unique words: {unique_word_count}")
print(f"Non-whitespace characters: {non_whitespace_count}")
print(f"Average words per sentence: {average_words_per_sentence:.2f}")
print(f"Non-unique words: {non_unique_word_count}")
