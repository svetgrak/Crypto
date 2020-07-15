from Alf import *
from datetime import datetime



def randint(num,a,c,m):
    return (a*num + c)%m

def gamma_gen_rus(text):

    result = ''
    count = len(text)
    time = datetime.now().time()
    num = time.hour * time.minute * time.second * time.microsecond
    while len(result) < count:
        num = randint(num,67,7,33)
        result+= alf1[num]

    return result

def gamma_gen_en(text):

    result = ''
    count = len(text)
    time = datetime.now().time()
    num = time.hour * time.minute * time.second * time.microsecond

    while len(result) < count:
        num = randint(num,79,19,26)
        result+= alf3[num]

    return result

def enc (text,key):

    result = ''
    key = list(key)

    for ch in text:
        if ch in alf1: result += alf1[(alf1.index(ch)+alf1.index(key.pop(0))) % len(alf1)]
        elif ch in alf2: result += alf2[(alf2.index(ch) + alf1.index(key.pop(0))) % len(alf2)]
        elif ch in alf3: result += alf3[(alf3.index(ch) + alf3.index(key.pop(0))) % len(alf3)]
        elif ch in alf4: result += alf4[(alf4.index(ch) + alf3.index(key.pop(0))) % len(alf4)]
        else: result+= ch
    return result

def dec (text,key):
    result = ''
    key = list(key)

    for ch in text:
        if ch in alf1: result += alf1[(alf1.index(ch) - alf1.index(key.pop(0))) % len(alf1)]
        elif ch in alf2: result += alf2[(alf2.index(ch) - alf1.index(key.pop(0))) % len(alf2)]
        elif ch in alf3: result += alf3[(alf3.index(ch) - alf3.index(key.pop(0))) % len(alf3)]
        elif ch in alf4: result += alf4[(alf4.index(ch) - alf3.index(key.pop(0))) % len(alf4)]
        else: result+= ch
    return result

