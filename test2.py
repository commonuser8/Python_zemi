# 変数の定義
a = 100
b = 1.00
c = "Hello World"
d = 'Hello Python'

print(a, b, c, d)

'''
変数名には大文字(A),小文字(a),数字(1),アンダースコア(_)が使える
ただし，変数名の頭文字に数字は使えない
○ Num, num, _num, num_1
× 1num, 01
'''

# 変数の型の確認
print(type(a))  # 変数の型を表示
print(isinstance(a, int))  # 変数の型が引数と一致するか

# 変数の型の変換
a = str(a)  # 整数型にはint(),浮動小数点型にはfloat()
print(type(a))