sentences = 'I love Python an I love JavaScript. I am looking for a new job. I cannot wait to get started.'

print(sentences.split('.'))
print(sentences.split(' '))
words = sentences.split(' ')
print(words)
print(len(words))
print(sentences.count('love') / len(words)) # print(2 / 20)