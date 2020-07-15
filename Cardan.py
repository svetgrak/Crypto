import random
from math import ceil
from Alf import*



def KeyForCardan(text):
    countPositions = ceil(len(text)/4)
    positions = [i for i in range (1,countPositions+1)]
    random.shuffle(positions)
    result=''
    for pos in positions: result+=str(pos)+' '
    return result

def checkKey (text,key):
    positions = []
    if key.replace(' ','').isdigit() == False: return False
    positions = key.split()
    if len(positions) < len(text)/4: return False
    else:return True

def matrixSize (key):
    countPositions = len(key.split())
    n = 1
    while countPositions > n**2: n +=1
    return 2*n

def createGrille(key,n):
    grille = [[0 for i in range(n)] for i in range(n)]
    mini = n//2
    key = key.split()
    for pos in key:
        pos = int(pos) -1
        i=0
        while pos > mini-1:
            pos -=mini
            i +=1
        grille[i][pos] = 1
        grille = rot270(grille)
    return grille

def rot90(matrix):
    result = []
    newMatrix = zip(*matrix)
    for column in newMatrix: result.append(list(reversed(column)))
    return result

def rot180(matrix): return rot90(rot90(matrix))

def rot270(matrix): return rot180(rot90(matrix))

def addRubbish(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '':
                if matrix[0][0].lower() in alf1: matrix[i][j] = alf1[random.randint(0,len(alf1)-1)]
                elif matrix[0][0].lower() in alf3: matrix[i][j] = alf3[random.randint(0,len(alf3)-1)]
    return matrix

def enc(text,key):
    n = matrixSize(key)
    result = []
    matrix = [['' for i in range(n)] for i in range(n)]
    text = text.ljust(n*n,' ')
    text = list(text)

    grille = createGrille(key,n)

    for h in range(4):
        for i in range(n):
            for j in range(n):
                if not text: break
                if grille[i][j] == 1: matrix[i][j] = text.pop(0)

        grille = rot90(grille)

    matrix = addRubbish(matrix)

    for line in matrix:
        result.append(''.join([str(ch) for ch in line]))

    return ''.join(result)

def dec(text,key):
    n = matrixSize(key)
    result = []
    text = list(text)
    matrix = [['' for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = text.pop(0)


    grille = createGrille(key,n)

    for h in range(4):
        for i in range(n):
            for j in range(n):
                if grille[i][j] == 1: result.append(matrix[i][j])
        grille = rot90(grille)

    return ''.join(result).rstrip()

