'''
両方が80以上なら"S",
そうではなく，片方が80以上で片方が60以上なら"A",
そうでもなく，片方が80以上で片方が60未満,もしくは両方が60以上なら"B",
それ以外は"C"
'''
math = 90
eng = 50
if math >= 80 and eng >= 80:
    print("S")
elif (math >= 80 and eng >= 60) or (math >= 60 and eng >= 80):
    print("A")
elif (math >= 80) or (eng >= 80) or (math >= 60 and eng >= 60):
    print("B")
else:
    print("C")

'''
if math >= 80:
    if eng >= 80:
        print("S")
    elif eng >= 60:
        print("A")
    else:
        print("B")
elif math >= 60:
    if eng >= 80:
        print("A")
    elif eng >= 60:
        print("B")
    else:
        print("C")
else:
    if eng >= 80:
        print("B")
    else:
        print("C")
'''