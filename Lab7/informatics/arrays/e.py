n = int(input())
list = list(map(int, input().strip().split()))
temp = False
for i in range(1, len(list)):
    if (list[i] > 0 and list[i - 1] > 0) or (list[i] < 0 and list[i - 1] < 0):
        temp = True
if temp :
    print('YES')
else:
    print('NO')