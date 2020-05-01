from math import *


def re(fg, d, s=0):
    for i in d:
        x = 2 * fg + sqrt(4*fg**2+i[1]**2)
        s += abs(i[0] - x)
        # s += (i[0] - x)**2
    return s


data = [(170, 66.4), (160, 52.25), (155, 44.1), (150, 27.4), (148.8, 27.7)]
result = {}
r = []
a = 35
while a < 36.5:
    result[re(a, data)] = a
    a += 0.01
    r.append(re(a, data))
print(result[min(r)])