from Alf import *


def enc(text, key):
    result = []
    key *= len(text) // len(key) + 1
    if len(key) > len(text): key = key[:(len(text))]
    key = list(key)

    for ch in text:
        if ch in alf1:result.append(alf1[(alf1.index(ch)+int(key.pop(0)))%len(alf1)])
        elif ch in alf2:result.append(alf2[(alf2.index(ch)+int(key.pop(0)))%len(alf2)])
        elif ch in alf3:result.append(alf3[(alf3.index(ch) + int(key.pop(0))) % len(alf3)])
        elif ch in alf4: result.append(alf4[(alf4.index(ch) + int(key.pop(0))) % len(alf4)])
        else: result.append(ch)

    return ''.join(result)

def dec(text, key):
    result = []
    key *= len(text) // len(key) + 1
    if len(key) > len(text): key = key[:(len(text))]
    key = list(key)

    for ch in text:
        if ch in alf1:result.append(alf1[(alf1.index(ch) - int(key.pop(0))) % len(alf1)])
        elif ch in alf2:result.append(alf2[(alf2.index(ch) - int(key.pop(0))) % len(alf2)])
        elif ch in alf3:result.append(alf3[(alf3.index(ch) - int(key.pop(0))) % len(alf3)])
        elif ch in alf4:result.append(alf4[(alf4.index(ch) - int(key.pop(0))) % len(alf4)])
        else:result.append(ch)

    return ''.join(result)
