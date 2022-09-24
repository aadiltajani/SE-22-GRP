import path
import sys




# importing

from functions import *
from definitions import *



eg = {}
#fails = 0
the={'eg':'','dump':False,'file':'../data/auto93.csv','help':False,'nums':512,'seed':10019,'seperator':','}

#the = {'nums': 100}
old = {}
row = {}

def runs(k):
    if (not eg.get(k)):
        return

    # the['seed'] = random.seed(10)
    random.seed(10)
    for k, v in the.items():
        old[k] = the[k]

    if ('dump' in the.keys()):
        status = True
        out = eg[k]
    # Else statement is remaining
    else:
        status = False
        out = eg[k]
    for k in old:
        the[k] = old[k]

    msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
    print("!!!!!!", msg, k, status)
    return out


def BAD():
    print('eg dont have this field')


def LIST():
    t = {}
    for k in eg:
        t[1 + len(t)] = k
    t = OrderedDict(sorted(t.items()))
    return t


def LS():
    print("\nExamples lua csv −e ...")
    lst = LIST()
    for _, k in lst.items():
        print("\t", k)
    return True


def ALL():
    fails = 0
    lst = LIST()
    for _, k in lst.items():
        if (k != "ALL"):
            print("\n−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−")
            if not runs(k):
                fails = fails + 1
    return True


# def the():
#   oo(the)
#   return true

def sym():
    sym = Sym()
    lst = ["a", "a", "a", "a", "b", "b", "c"]
    for x in lst:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = (1000 * entropy) // 1 / 1000
    oo({'mid': mode, 'div': entropy})
    return mode == "a" and 1.37 <= entropy <= 1.38


def bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1, 1000):
        num.add(i, the)
    print('nums', num.nums())
    oo(num.nums())
    return 32 == len(num.has)


def num():
    num = Num()
    for i in range(1, 100):
        num.add(i, the)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    return 50 <= mid <= 52 and 30.5 < div < 32

def func(n,row):
    n = n + 1
    if n>10:
        return
    else:
        oo(row)
    return True

def csv(fileName):
    if(fileName==None or len(fileName.strip())==0):
        raise Exception("FILE NOT FOUNDED")
    rows=[]
    with open(fileName,'r',encoding='utf-8') as file:
        row_eles=file.readlines()
        for row_ele in row_eles:
            k=list(map(coerce,row_ele.split(',')))
            rows.append(k)
    return rows

def data():
    d = Data(the['file'])
    for col in d.cols.y:
        oo(col)
    return True

def divfunc(col):
    return col.div()

def midfunc(col):
    return col.mid()


def stats():
    
    data = Data(the['file'])
    
    
    #print("xmid", oo( data.stats(2,data.cols.x, mid)))
    #print("xdiv", oo( data.stats(3,data.cols.x, div)))
    #print("ymid", oo( data.stats(2,data.cols.y, mid)))
    #print("ydiv", oo( data.stats(3,data.cols.y, div)))    


    print('xmid:',str(data.stats('x','mid')))
    print('xdiv:',str(data.stats('x','div')))
    print('ymid:',str(data.stats('y','mid')))
    print('ydiv:',str(data.stats('y','div')))

#help_string = input()
#the = coerce(help_string)
#print(sym())
#print(num())
#print(bignum())
#print(csv())
print(stats())