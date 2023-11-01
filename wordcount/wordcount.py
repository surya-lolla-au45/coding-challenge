n="Data preprocessing is an important task in text classification. With the emergence of Python in the field of data science"
words=n.split()
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print("Unique words and their counts of occurrence:")
for word, count in word_count.items():
      print(f"{word}: {count}")
 





