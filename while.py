# while文
num = 0
while (num <= 5):
    print(num)
    num += 1

while (num):
    print

# while ~ else
num = 0
while (num <= 5):
    print(num)
    num += 1
else:
    print("繰り返し処理終了")

# break
num = 0
while(True):
    print(num)
    num += 1
    if (num == 5):
        break