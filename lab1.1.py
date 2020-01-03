import random

A=random.randint(1, 20)
B=random.randint(1, 20)
C=random.randint(1, 20)
D=random.randint(1, 20)
a = A % 2
b = B % 2
c = C % 2
d = D % 2

print (A, B, C, D)
if a == 0 or b == 0 or c == 0 or d == 0:
    print ("Есть четные числа")
else:
    print ("Нет четных чисел")