from Alf import *
from datetime import datetime
import re

def randint(num,a,c,m):
    return (a*num + c)%m

def gamma_gen(text):
    result = ''
    count = len(text)*5

    while len(result) < count:
        now_time = datetime.now().time().microsecond
        next_num = bin(randint(now_time,67,7,33))
        result+=str(next_num)[2:]

    result = result[:count]
    return result

def replace_ch(text):
    text = list(text)
    replace_ch = {'ё': 'е', 'Ё': 'Е'}
    for ch in text:
        if ch in replace_ch.keys():
            index=text.index(ch)
            text.remove(ch)
            text.insert(index,replace_ch[ch])
    return ''.join(text)

def xor (num1,num2):
    result = ''
    for i in range(5):result+= str(int(num1[i])^int(num2[i]))
    return result

def return_dict_key(val,dict):
    for key,value in dict.items():
        if val == value: return key

def enc(text,key):
    result = ''
    text = list(replace_ch(text))
    key = [key[x:x + 5] for x in range(0, len(key), 5)]

    for ch in text:
        if ch.islower(): low = True
        else: low = False
        if ch.upper() in bin_en.keys():
            code = xor(bin_en[ch.upper()],key.pop(0))
            if low: result+=return_dict_key(code,bin_en).lower()
            else: result+=return_dict_key(code,bin_en)
        elif ch.upper() in bin_rus.keys():
            code = xor(bin_rus[ch.upper()], key.pop(0))
            if low:result += return_dict_key(code, bin_rus).lower()
            else:result += return_dict_key(code, bin_rus)
        else:result+=ch

    return result

def dec(text,key):
    return enc(text,key)



