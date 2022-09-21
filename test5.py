# for文
prog = ["Python", "Java", "C#"]
for s in prog:  # for(String s: prog)
    print(s)

# range関数
for i in range(0, 5, 1):  # for(int i = 0; i < 5; i = i + 1)
    print(i)

#for i in range(5):
#for i in range(0, 5):


# break
a = []
for i in range(5):
    if i == 2:
        break
    a.append(i)
print(a)

# continue
b = []
for i in range(5):
    if i == 2:
        continue
    b.append(i)
print(b)