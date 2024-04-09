# Count the number of unique words in a String in Python

my_str = 'one one two two'

unique_words = set(my_str.split())
print(unique_words)  # 👉️ {'one', 'two'}

length = len(unique_words)
print(length)  # 👉️ 2