# https://projecteuler.net/problem=42

def readFile():
    with open('p042_words.txt') as f:
        s = f.readline()
        s = s.replace("\"", "")
        li = s.split(',')
        return li

def isTriangle(k):
    a = 0.5*(pow(8*k + 1, 0.5) - 1)
    return a == int(a)

def wordToNum():
    di = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    li = readFile()
    a = []
    for i in li:
        su = 0
        for j in i:
            su += di[j.lower()]
        a.append(su)
    return a

def isWordTriangle():
    a = wordToNum()
    count = 0
    for i in a:
        if isTriangle(i):
            count += 1
    print(count)


isWordTriangle()
