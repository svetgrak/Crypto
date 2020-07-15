from Alf import *

def replace_ch(text):
    text = list(text)
    replace_ch = {'j': 'i', 'J': 'I', 'ё': 'е', 'Ё': 'Е', 'й': 'и', 'Й': 'И', 'ъ':'ь','Ъ':'Ь'}
    for ch in text:
        if ch in replace_ch.keys():
            index=text.index(ch)
            text.remove(ch)
            text.insert(index,replace_ch[ch])
    return ''.join(text)

def key_in_alf(key,alf):

    alf = ''.join(alf)
    alf = list(replace_ch(alf))
    key = list(key)

    tabl_alf = []

    for ch in key:
        if ch not in tabl_alf: tabl_alf.append(ch)

    for ch in alf:
        if ch not in tabl_alf: tabl_alf.append(ch)

    return tabl_alf

def enc (text, key):

    text = list(replace_ch(text))
    key = replace_ch(key).lower()

    tabl_alf1 = []
    tabl_alf2 = []
    countStr=5

    if text[0].lower() in alf1:
        tabl_alf1 = key_in_alf(key,alf1)
        tabl_alf2 = key_in_alf(key.upper(),alf2)

    if text[0].lower() in alf3:
        tabl_alf1 = key_in_alf(key,alf3)
        tabl_alf2 = key_in_alf(key.upper(),alf4)

    result=[]

    for ch in text:
        if ch in tabl_alf1: result.append(tabl_alf1[(tabl_alf1.index(ch)+int(len(tabl_alf1)/countStr))%len(tabl_alf1)])
        elif ch in tabl_alf2: result.append(tabl_alf2[(tabl_alf2.index(ch)+int(len(tabl_alf2)/countStr))%len(tabl_alf2)])
        else: result.append(ch)

    return ''.join(result)

def dec (text, key):
    text = list(replace_ch(text))
    key = replace_ch(key).lower()

    tabl_alf1 = []
    tabl_alf2 = []
    countStr=5

    if text[0].lower() in alf1:
        tabl_alf1 = key_in_alf(key,alf1)
        tabl_alf2 = key_in_alf(key.upper(),alf2)

    if text[0].lower() in alf3:
        tabl_alf1 = key_in_alf(key,alf3)
        tabl_alf2 = key_in_alf(key.upper(),alf4)

    result=[]

    for ch in text:
        if ch in tabl_alf1: result.append(tabl_alf1[(tabl_alf1.index(ch)-int(len(tabl_alf1)/countStr))%len(tabl_alf1)])
        elif ch in tabl_alf2: result.append(tabl_alf2[(tabl_alf2.index(ch)-int(len(tabl_alf2)/countStr))%len(tabl_alf2)])
        else: result.append(ch)
    return ''.join(result)

