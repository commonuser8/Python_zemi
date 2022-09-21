# 関数の作成
def rectangle(a, b):
    return a * b

def triangle(a, b):
    return a * b / 2

a = 5
b = 10
print(rectangle(a, b), triangle(a, b))


def numprint(*args):
    i = 1
    for s in args:
        print(str(i) + ":" + s)
        i = i + 1

numprint("Java", "Python", "C++")