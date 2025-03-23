import math

a = int(input())
b = int(input())

ans = 0

for i in range(a, b + 1):
    if(math.sqrt(i) % 1 == 0):
        print(i)