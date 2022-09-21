# リストの作成
a = [1, 2, 3]
b = ["one", "two", "three"]
c = [1, "two", 'THREE']
d = []

print(a, b, c, d)

# リストの要素にアクセス
print(a[1])

# リストの要素の変更
a[0] = -1
print(a)

# リストに要素を追加
a.append(5)
print(a)

# リストに要素を挿入
a.insert(2, 10)
print(a)

# リストの要素の削除
del a[1]  #指定したインデックスの要素を削除する
print(a)

a.pop(1)  #指定したインデックスの要素を取り出す(指定しなかった場合は末尾の要素)
print(a)

a.remove(5)  #指定した値の要素を削除
print(a)

# リストの結合
a.extend(b)
print(a)

# リストのソート
e = [2, 1, 8, -1, 5]

e.sort()  # 昇順にソート
print(e)

e.sort(reverse=True)  # 降順にソート
print(e)

# スライス
f = e[1:3]
g = e[:3]
h = e[1:]
i = e[:-1]  # 負の値は末尾から数える
j = e[::2]  # 3個目の引数を指定すると，何個おきに取り出すか決められる
print(f, g, h, i, j)

k = [1, 9, 4, 6, 2]
l = k[::-1]  # 並びを簡単に逆順に出来る
print(k, l)

# リストの初期化
l.clear()
print(l)