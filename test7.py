# 辞書の作成
a = {"japanese": 80, "math": 75, "english": 50}
b = dict(japanese=80, math=75, english=50)
print(a, b)

# 辞書のキーから値の取得
print(a["math"])  # 辞書aのキー"math"の値を取得
#print(a["physics"])  # 辞書に無いキーを指定するとエラーになる

print(a.get("math"))  # 辞書aのキー"math"の値を取得
print(a.get("physics"))  # 辞書に無いキーを指定するとNoneが返る

# 辞書の要素の取得
for x in a.keys():  # キーの取得
    print(x)

for x in a.values():  # 値の取得
    print(x)

for x, y in a.items():  # キーと値を同時に取得
    print(x, y)

# 要素の変更
a["english"] = 10  # 辞書aのキー"english"の値を10に変更
print(a)
# * 辞書に無いキーを指定すると，そのキーと値を新しく追加する
a["chemistry"] = 40  # 辞書aにキー"chemistry"が無いので、そのキーを値40として追加
print(a)

# 要素の削除  * popやclearも利用できる
del a["chemistry"]  # 辞書aにあるキー"chemistry"を削除
print(a)