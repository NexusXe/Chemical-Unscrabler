from mendeleev import element


def RemoveFromList(thelist, val):
    return [value for value in thelist if value != val]

def GetDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return 
    
def Word2Vect(word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v

def Vect2Int(vect):
    pv = 0
    f = 0
    for i in range(0, len(vect)):
        wip = (vect[i]*(2**pv))
        f += wip
        pv += 4
    return f

    
def Ints2Dic(dic):
    d = {}
    for i in range(0, len(dic)):
        v = Word2Vect(dic[i])
        Int = Vect2Int(v)
        if Int in d:
            tat = d.get(Int)
            tat.append(dic[i])
            d[Int] = tat
        elif Int not in d:
            d[Int] = [dic[i]]
    return d
        


def Convert(string): 
    li = list(string.split(" ")) 
    return li

def listToString(s):  
    str1 = ""    
    for ele in s:  
        str1 += ele     
    return str1 

d = GetDic()
ind = Ints2Dic(d)


while True:
    try:
        wordScrambled = []
        elementList = input('Enter element names as a list. >>')
        elementList = elementList.title()
        elementList = Convert(elementList)
        # print(elementList)
        for i in range(len(elementList)):
            elementWanted = elementList[i]
            elementWanted = element(str(elementWanted))
            wordScrambled.append(elementWanted.symbol)
        print(wordScrambled)
        wordScrambled = listToString(wordScrambled)
        # print(wordScrambled)
        
        s = wordScrambled
        v = Vect2Int(Word2Vect(s))
        tp = ind.get(v, 'Word Not in Dictionary.')
        print(tp)
        pass
    except:
        continue
