fruits = ["apple", "banana", "pear"]

lengths = { fruit : len(fruit) for fruit in fruits }

long_words = { fruit for fruit in lengths if len(fruit) > 5 }
print(long_words)