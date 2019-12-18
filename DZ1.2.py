import numpy

c = 2.1
r = 4 * (10 ** (-4))
m = 7
j = (4.2, 0.3, 1.7)

for i in range(len(j)):
    h = (10 * r - j[i]) / (c ** 2 + numpy.e ** (-m))
    y = (h * m - (j[i] ** 2)) + ((0.1 * c) ** 2)
    print(y)

w = 0
while w <= 1.7:
    h = (10 * r - w) / (c ** 2 + numpy.e ** (-m))
    y = (h * m - (w ** 2)) + ((0.1 * c) ** 2)
    w += 0.1
    print(y)

j = (9, 1.8, 15, -3)
m = 1
for n in range(len(j)):
        while m <= 2:
            h = (10 * r - m) / (c ** 2 + numpy.e ** (-m))
            y = (h * m - (m ** 2)) + ((0.1 * c) ** 2)
            m += 0.5
            print(y)