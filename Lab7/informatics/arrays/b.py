n = int(input())
list = list(map(int, input().strip().split()))

for i in list:
    if i % 2 == 0:
        print(i, end=' ')