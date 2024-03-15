word_to_count = {}

text = "this is a collection of words of nice words this is a fun thing it is"
# text = input("Text: ")
words = text.split()

for word in words:
    counting_word = word_to_count.get(word, 0)
    word_to_count[word] = counting_word + 1

words = list(word_to_count.keys())
words.sort()

max_length = max(len(word) for word in words)

for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
