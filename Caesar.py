from Alf import *

def enc (text, key):
    result = []
    for ch in text:
        if ch in alf1: result.append(alf1[(alf1.index(ch)+key)%len(alf1)])
        elif ch in alf2: result.append(alf2[(alf2.index(ch)+key)%len(alf2)])
        elif ch in alf3: result.append(alf3[(alf3.index(ch)+key)%len(alf3)])
        elif ch in alf4: result.append(alf4[(alf4.index(ch)+key)%len(alf4)])
        else: result.append(ch)
    return ''.join(result)

def dec (text, key):
    result = []
    for ch in text:
        if ch in alf1:result.append(alf1[(alf1.index(ch)-key)%len(alf1)])
        elif ch in alf2:result.append(alf2[(alf2.index(ch)-key)%len(alf2)])
        elif ch in alf3:result.append(alf3[(alf3.index(ch)-key)%len(alf3)])
        elif ch in alf4:result.append(alf4[(alf4.index(ch)-key)%len(alf4)])
        else: result.append(ch)
    return ''.join(result)



