import re

matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

cols = len(matrix[0])
rows = len(matrix)
raw_text = ''

for col in range(cols):
    for row in range(rows):
        raw_text += matrix[row][col]

decoded = re.sub(r'(?<=[a-zA-Z])[^a-zA-Z]+(?=[a-zA-Z])', ' ', raw_text)

print(decoded)
