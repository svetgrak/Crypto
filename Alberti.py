from Alf import *
import random
import re


def KeyForAlberti_Rus():
    fullAlf = []
    fullAlf.extend(alf1)
    fullAlf.extend(alf2)
    random.shuffle(fullAlf)
    return ''.join(fullAlf)[:12]

def KeyForAlberti_En():
    fullAlf = []
    fullAlf.extend(alf3)
    fullAlf.extend(alf4)
    random.shuffle(fullAlf)
    return ''.join(fullAlf)[:12]


def key_in_alf(key,alf):

    key = list(key)
    tabl_alf = []

    for ch in key:
        if ch not in tabl_alf: tabl_alf.append(ch)

    for ch in alf:
        if ch not in tabl_alf: tabl_alf.append(ch)

    return tabl_alf

def incrKey(key,text):
    text=text.replace(' ','')
    key *= len(text) // len(key) + 1
    if len(key) > len(text): key = key[:(len(text))]
    return key


def enc(text,key,keyForTable):
    result = []
    keyForTable = keyForTable.lower()

    if key[0] in alf1:tabl = key_in_alf(keyForTable,alf1)
    else:tabl = key_in_alf(keyForTable,alf3)

    key = list(incrKey(key, text).lower())
    for ch in text:
        if ch in alf1: result.append(tabl[(alf1.index(ch)-alf1.index(key.pop(0)))%len(alf1)])
        elif ch in alf2: result.append(tabl[(alf2.index(ch)-alf1.index(key.pop(0)))%len(alf2)].upper())
        elif ch in alf3: result.append(tabl[(alf3.index(ch)-alf3.index(key.pop(0)))%len(alf3)])
        elif ch in alf4: result.append(tabl[(alf4.index(ch)-alf3.index(key.pop(0)))%len(alf4)].upper())
        else: result.append(ch)

    return ''.join(result)



def dec(text,key,keyForTable):
    result = []
    keyForTable = keyForTable.lower()

    if key[0] in alf1:tabl = key_in_alf(keyForTable, alf1)
    else:tabl = key_in_alf(keyForTable, alf3)

    key = list(incrKey(key, text).lower())
    for ch in text:

        if ch in alf1: result.append(alf1[(tabl.index(ch.lower())+alf1.index(key.pop(0)))%len(alf1)])
        elif ch in alf2: result.append(alf2[(tabl.index(ch.lower())+alf1.index(key.pop(0)))%len(alf2)].upper())
        elif ch in alf3: result.append(alf3[(tabl.index(ch.lower())+alf3.index(key.pop(0)))%len(alf3)])
        elif ch in alf4: result.append(alf4[(tabl.index(ch.lower())+alf3.index(key.pop(0)))%len(alf4)].upper())
        else: result.append(ch)


    return ''.join(result)

