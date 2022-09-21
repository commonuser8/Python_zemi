# 集合の作成
a = {1, 1, 1, 2, 2, 3, 4, 4.0}
b = set({1.0, 2.00, 3.000, 4.0000})
c = {4, 3, 1, 2}  # 集合には要素の順序がない
print(a, b, c)

list_a = [1, 4, 4, 2, 1, 3, 2]
print(set(list_a))  # リストからも作成できる

# 要素の追加
a.add(5)
print(a)

# 要素の削除  *popやremove,clearも利用できる *ただし，popで要素の指定は出来ない
a.discard(2)  # removeと同じように使う
print(a)

a.discard(10)  # 要素にない値を指定してもエラーにならない(removeではエラーになる)
print(a)


''' 集合演算 '''
set_a = {0, 1, 2}
list_b = [2, 3, 4]
touple_c = (2, 4, 6)
set_b = set(list_b)
set_c = set(touple_c)

# 和集合
union_a = set_a | set_b | set_c  # 集合同士の和集合
print(union_a)

union_b = set_a.union(list_b, touple_c)  # 集合以外でも和集合に利用できる
print(union_b)

# 差集合
difference_a = set_a - set_b - set_c
print(difference_a)

difference_b = set_a.difference(list_b, touple_c)
print(difference_b)

# 積集合
intersection_a = set_a & set_b & set_c
print(intersection_a)

intersection_b = set_a.intersection(list_b, touple_c)
print(intersection_b)

# 対称差集合
symmetric_diff_a = set_a ^ set_b ^ set_c
print(symmetric_diff_a)

symmetric_diff_b = set_a.symmetric_difference(list_b)  # 引数が一つしか取れない
symmetric_diff_b = symmetric_diff_b.symmetric_difference(touple_c)
print(symmetric_diff_b)


''' 集合比較 '''
s1 = {1 ,2 ,3}
s2 = {3, 2, 1}
s3 = {4, 5, 6}
s4 = {1, 2, 3, 4, 5, 6}

# 完全一致
print(s1 == s2)

# 完全不一致
print(s1.isdisjoint(s3))

# 部分集合
print(s1.issubset(s4))  # s1 <= s4

# 上位集合
print(s4.issuperset(s1))  # s4 >= s1