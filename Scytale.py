import math

def enc (text,key):
    countColumn = math.ceil((len(text))/key)
    text = list(text.ljust(countColumn*key))
    result = []
    for j in range(countColumn):
        for i in range(key): result.append(text[i*countColumn+j])
    return ''.join(result)

def dec (text,key):
    countColumn = math.ceil((len(text)) / key)
    text = list(text)
    result = []
    for i in range(key):
        for j in range(countColumn): result.append(text[j*key+i])
    return ''.join(result)

