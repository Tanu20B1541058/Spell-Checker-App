import re
import pandas as pd

def split(word):  
    parts = []
    for i in range(len(word) + 1):
        parts += [(word[:i], word[i:])]
    return parts

def delete(word):
    output = []
    for l, r in split(word):
        output.append(l + r[1:])
    return output

def swap(word):
    output = []    
    for l, r in split(word):
        if len(r) > 1:
            output.append(l + r[1] + r[0] + r[2:])
    return output

def replace(word):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    output = []    
    for l, r in split(word):
        for char in characters:
            output.append(l + char + r[1:])
    return output

def insert(word):
    characters = 'abcdefghijklmnopqrstuvwxyz'
    output = []
    for l, r in split(word):
        for char in characters:
            output.append(l + char + r)
    return output

def edit(word):
    return list(set(insert(word) + delete(word) + swap(word) + replace(word)))

def spell_check_edit_1(word, count=5):
    word_probability = {}
    words = []  # Assume 'words' is defined
    for w in words:
        word_probability[w] = float(words.count(w) / len(words))
    output = []
    suggested_words = edit(word)
    for wrd in suggested_words:
        if wrd in word_probability.keys():
            output.append([wrd, word_probability[wrd]])
    return list(pd.DataFrame(output, columns=['word', 'prob']).sort_values(by='prob', ascending=False).head(count)['word'].values)

def spell_check_edit_2(word, count=5):
    output = []
    suggested_words = edit(word)
    for e1 in edit(word):
        suggested_words += edit(e1)
    suggested_words = list(set(suggested_words))
    for wrd in suggested_words:
        if wrd in word_probability.keys():
            output.append([wrd, word_probability[wrd]])
    return list(pd.DataFrame(output, columns=['word', 'prob']).sort_values(by='prob', ascending=False).head(count)['word'].values)

# 1. Finding the Unique Words

with open('big.txt','r') as fd:
    lines = fd.readlines()
    words = []
    for line in lines:
        words += re.findall('\w+', line.lower())
        

vocab = list(set(words))


# 2. Finding the Probability Distribution
word_probability = {}

for word in vocab:
    word_probability[word] = float(words.count(word) / len(words))
