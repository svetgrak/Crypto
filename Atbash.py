from Alf import *

def enc(text):
    text.split()
    result=[]
    for ch in text:
        if ch in alf1: result.append(alf1[len(alf1)-alf1.index(ch)-1])
        elif ch in alf2:result.append(alf2[len(alf2)-alf2.index(ch)-1])
        elif ch in alf3: result.append(alf3[len(alf3)-alf3.index(ch)-1])
        elif ch in alf4: result.append(alf4[len(alf4)-alf4.index(ch)-1])
        else: result.append(ch)
    return ''.join(result)

def dec (text):
    return enc(text)


