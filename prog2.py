'''
2進数が格納されている配列がある．
list0 = [0, 0, 0, 1, 0, 0, 0, 0]

その配列を元に，0なら空白(" ")，1ならアスタリスク("*")を表示する．
(   *    )

次に，前の配列の同じインデックスの隣の値で片方のみが1だったときに1，
それ以外が0となる配列を作る．配列の端の場合はもう片方を0とする．
list1 = [0, 0, 1, 0, 1, 0, 0, 0]

その配列を元に，0なら空白(" ")，1ならアスタリスク("*")を表示する．
(  * *   )

これをx行表示されるまで繰り返す．ここで， xは15とする．
'''

def nextList(list0):
    nextlist = []
    for i in range(len(list0)):
        if (i > 0 and list0[i - 1] == 1) and (i < len(list0) - 1 and list0[i + 1] == 0):
            nextlist.append(1)
        elif (i > 0 and list0[i - 1] == 0) and (i < len(list0) - 1 and list0[i + 1] == 1):
            nextlist.append(1)
        else:
            nextlist.append(0)
    return nextlist

def sellPrint(list0):
    for i in list0:
        if i == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print() 

'''
# (応用)10進数yから2進数配列を作る
def changeBinList(y):
    z = bin(y)
    list1 = []
    if len(z) < 10:  # 8桁以上になるように調整
        for i in range(10 - len(z)):
            list1.append(0)
    for i in range(len(z) - 2):
        list1.append(int(z[i + 2:i + 3]))
    return list1

y = 16
list1 = changeBinList(16)
'''

x = 15
list0 = [0, 0, 0, 1, 0, 0, 0, 0]
for i in range(x):
    sellPrint(list0)
    list0 = nextList(list0)