import random
from collections import OrderedDict
from definitions import Sym, Num
from functions import oo, coerce

eg = {}
fails = 0

the = {'nums': 100}
old = {}


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


help_string = input()
the = coerce(help_string)
print(sym())
print(num())
print(bignum())