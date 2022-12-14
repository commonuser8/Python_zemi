# 集合の作成
a = {1, 1, 1, 2, 2, 3, 4, 4.0}  # 重複は除去される  *intやfloatは型が別でも値が等しければ重複扱い
b = {4, 3, 1, 2}  # 集合には要素の順序がない
print(a, b)

list_a = [1, 4, 4, 2, 1, 3, 2]
print(set(list_a))  # リストからも作成できる

# 要素の追加
a.add(5)  # 集合aに5を追加
print(a)

# 要素の削除  * popやremove,clearも利用できる  * ただし，popで要素の指定は出来ない
a.discard(2)  # 集合aにある値が2の要素を削除
print(a)
# * 要素にない値を指定してもエラーにならない(removeではエラーになる)
a.discard(10)  # 集合aにない要素(10)を削除しようとしているがエラーは起きない(何も起きない)
print(a)