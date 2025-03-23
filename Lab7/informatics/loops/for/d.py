import math

a = int(input())
b = int(input())

a_str = str(a)

cnt = 0

for i in a_str:
    if i == str(b):
        cnt += 1
        
print(cnt)