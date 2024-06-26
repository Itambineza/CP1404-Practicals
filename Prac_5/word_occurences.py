"""
Word Occurrences
Estimate: 45 minutes
Actual:    minutes
"""
text = input("Text: ")
words = text.split()

word_counts = {}
# Counting the occurrence of each word
for word in words:
    # converting words to lower cases to avoid cases insensitivity
    word = word.lower()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.keys())

for word in sorted_words:
    print(f"{word:<10} : {word_counts[word]}")

