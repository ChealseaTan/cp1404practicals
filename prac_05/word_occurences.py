"""
Word Occurrences
Estimate: 45 minutes
Actual: 45 minutes
"""

word_to_value = {}
string = input("Text: ")

sentence = string.split()
sentence.sort()

for word in sentence:
    if word in word_to_value:
        word_to_value[word] += 1
    else:
        word_to_value[word] = 1

width = len(max(sentence, key=len))

for word, value in word_to_value.items():
    print(f"{word:{width}}: {value}")