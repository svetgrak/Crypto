import re
import random
from Alf import*


def KeyForRishele(lenText):
    arrCountInBlock=[]
    result = []
    while lenText!=0:
        if lenText > 10:
            countCh=random.randint(2,9)
            arrCountInBlock.append(countCh)
            lenText-=countCh
        elif lenText > 3:
            countCh = random.randint(2, lenText//2)
            arrCountInBlock.append(countCh)
            lenText -= countCh
        else:
            arrCountInBlock.append(lenText)
            break

    for count in arrCountInBlock:
        arrPositions = [i for i in range (1,count+1)]
        random.shuffle(arrPositions)
        result.append(arrPositions)

    res = ''
    for arr in result:
        res+='('
        for ch in arr: res+=str(ch)
        res+=')'
    return res


def checkKey(text,key):

    countCh = []
    while len(key)!=0:
        res = re.match(r'[(]\d*[)]',key)
        if res == None : return False
        key = key[len(res.group(0)):]
        countCh.append(len(re.findall(r'[^()]',res.group(0))))

    if sum(countCh) != len(text): return False

    return True

def enc(text,key):
    text = list(text)
    result = []
    arrPositions = re.findall(r'\w+',key)
    for positions in arrPositions:
        newText = ['' for i in range(len(positions))]
        i = 0
        for pos in positions:
            newText.pop(int(pos)-1)
            newText.insert(int(pos)-1,text.pop(0))
            i += 1
        result.append(''.join(newText))
    return ''.join(result)

def dec(text,key):

    text = list(text)
    result = []
    arrPositions = re.findall(r'\w+', key)
    for positions in arrPositions:
        newText = []

        for pos in positions: newText.append(text[int(pos)-1])
        for i in range(len(positions)): text.pop(0)


        result.append(''.join(newText))
    return ''.join(result)



