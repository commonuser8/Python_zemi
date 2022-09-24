'''
1~100までの整数のうち，
3の倍数または5の倍数で，偶数ではなくかつ15の倍数ではないものをリストで表示する．
'''

list1 = []
for i in range(1, 101):
    if (i % 3 == 0 or i % 5 == 0) and i % 2 == 1 and i % 15 != 0:
        list1.append(i)
print(list1)