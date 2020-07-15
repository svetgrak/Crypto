from Alf import *
import re

def replace_ch(text):
    text = text.replace('j','').replace('J', '')
    text = text.replace('ё', '').replace('Ё','')

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

def text_del_symb(text):
    return ''.join(re.findall('[A-Za-zА-Яа-я]', text))

def text_to_bigram(text,ch):
    text = text_del_symb(text)
    result = []
    while len(text)!=0:
        bigram = list(text[:2])
        if len(bigram) == 1:
            bigram.append(ch)
            text = text[1:]
        elif bigram[0].lower()==bigram[1].lower():
            bigram[1] = ch
            text = text[1:]
        else:
            text = text[2:]
        result.append(''.join(bigram))
    return result

def bigram_to_text(bigrams,ch):
    result =[]
    pred = ''

    while len(bigrams)!=1:

        if bigrams[0][1] == ch and bigrams[1][1] == ch and bigrams[0][0]==bigrams[1][0]:

            result.append(bigrams[0][0]+bigrams[1][0])
            pred = bigrams[1]
            bigrams.pop(0)
            bigrams.pop(0)

        elif  bigrams[0][1] == ch and pred[1] == ch and bigrams[0][0]==pred[0] :
            result.append(bigrams[0][0])
            pred = bigrams[0]
            bigrams.pop(0)

        else:
            result.append(bigrams.pop(0))
            pred = bigrams[0]

    if bigrams[0][1] == ch: result.append(bigrams[0][0])
    else:result.append(bigrams.pop(0))


    return ''.join(result)


def enc(text,key):
    text = replace_ch(text)
    if text_del_symb(text)[0].lower() in alf1:
        alf = alf1
        count_symb_str = 8

        bigramms = text_to_bigram(text,'х')
    else:
        alf = alf3
        count_symb_str = 5
        bigramms = text_to_bigram(text,'x')

    tabl = key_in_alf(key.lower(),alf)
    count_symb_stlb = len(tabl) // count_symb_str

    result_bigramms = []

    for bigram in bigramms:
        symb1,symb2 = bigram[0],bigram[1]
        position_symb1, position_symb2 = tabl.index(symb1.lower()), tabl.index(symb2.lower())
        position_symb1, position_symb2 = divmod(position_symb1,count_symb_str), divmod(position_symb2,count_symb_str)

        res = []
        if position_symb1[0] == position_symb2[0]:
            res.append(tabl[(position_symb1[1]+1)%count_symb_str + position_symb1[0]*count_symb_str])
            res.append(tabl[(position_symb2[1]+1)%count_symb_str + position_symb2[0]*count_symb_str])
            if bigram[0].isupper(): res[0]=res[0].upper()
            if bigram[1].isupper(): res[1]=res[1].upper()

        elif position_symb1[1] == position_symb2[1]:
            res.append(tabl[((position_symb1[0]+1)%count_symb_stlb)*count_symb_str+position_symb1[1]])
            res.append(tabl[((position_symb2[0]+1)%count_symb_stlb)*count_symb_str+position_symb2[1]])
            if bigram[0].isupper(): res[0] = res[0].upper()
            if bigram[1].isupper(): res[1] = res[1].upper()

        else:
            res.append(tabl[(position_symb1[0]*count_symb_str)+position_symb2[1]])
            res.append(tabl[(position_symb2[0]*count_symb_str)+position_symb1[1]])
            if bigram[0].isupper(): res[0] = res[0].upper()
            if bigram[1].isupper(): res[1] = res[1].upper()

        result_bigramms.append(''.join(res))

    return ''.join(result_bigramms)


def dec(text,key):

    if text_del_symb(text)[0].lower() in alf1:
        alf = alf1
        count_symb_str = 8
        ch = 'х'

    else:
        alf = alf3
        count_symb_str = 5
        ch = 'x'

    bigramms = text_to_bigram(text, ch)

    tabl = key_in_alf(key.lower(), alf)
    count_symb_stlb = len(tabl) // count_symb_str

    result_bigramms = []

    for bigram in bigramms:
        symb1, symb2 = bigram[0], bigram[1]
        position_symb1, position_symb2 = tabl.index(symb1.lower()), tabl.index(symb2.lower())
        position_symb1, position_symb2 = divmod(position_symb1, count_symb_str), divmod(position_symb2, count_symb_str)

        res = []
        if position_symb1[0] == position_symb2[0]:
            res.append(tabl[(position_symb1[1] - 1) % count_symb_str + position_symb1[0] * count_symb_str])
            res.append(tabl[(position_symb2[1] - 1) % count_symb_str + position_symb2[0] * count_symb_str])
            if bigram[0].isupper(): res[0] = res[0].upper()
            if bigram[1].isupper(): res[1] = res[1].upper()

        elif position_symb1[1] == position_symb2[1]:
            res.append(tabl[((position_symb1[0] - 1) % count_symb_stlb) * count_symb_str + position_symb1[1]])
            res.append(tabl[((position_symb2[0] - 1) % count_symb_stlb) * count_symb_str + position_symb2[1]])
            if bigram[0].isupper(): res[0] = res[0].upper()
            if bigram[1].isupper(): res[1] = res[1].upper()

        else:
            res.append(tabl[(position_symb1[0] * count_symb_str) + position_symb2[1]])
            res.append(tabl[(position_symb2[0] * count_symb_str) + position_symb1[1]])
            if bigram[0].isupper(): res[0] = res[0].upper()
            if bigram[1].isupper(): res[1] = res[1].upper()

        result_bigramms.append(''.join(res))

    return bigram_to_text(result_bigramms,ch)



