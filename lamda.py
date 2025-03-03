file = open('python_assignment.txt', 'r') 

text = file.read() 

file.close() 

words = text.lower().split() 

word_counts = {} 

for word in words: 

     if word in word_counts: 

          word_counts[word] += 1 

     else: 

          word_counts[word] = 1 

print("Word frequencies:") 

for word, count in word_counts.items(): 

     print(f"{word}: {count}") 