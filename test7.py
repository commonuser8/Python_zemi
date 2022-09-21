# 辞書の作成
a = {"japanese":80, "math":75, "english":50}
b = dict(Japanese = 80, math = 75, English = 50)
print(a, b)

# 辞書のキーから値の取得
print(a["math"])  # 辞書に無いキーを指定するとエラーになる
print(a.get("math"))  # 辞書に無いキーを指定するとnoneが返る

# 辞書の要素の取得
for x in a.keys():  # キーの取得
    print(x, end=" ")

for x in a.values():  # 値の取得
    print(x, end=" ")

for x, y in a.items():  # キーと値を同時に取得
    print(x, y, end=" ")

print()

# 要素を追加
a.setdefault("physics", 90)
print(a)

# 要素の変更
a["english"] = 10  # 辞書に無いキーを指定すると，そのキーと値を新しく追加する
print(a)

# 要素の削除  *popやdel，clearも利用できる
c = a.popitem()  # 辞書の要素をタプル型で一つ取り出す *ただし要素を指定できない
print(c, a)

d, e = a.popitem()  # キーと値を別々に取り出すこともできる
print(d, e, a)