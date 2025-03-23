n = int(input())
list = list(map(int, input().strip().split()))

for i in range(int(n/2)):
    b = list[i]
    list[i] = list[n-1-i]
    list[n-1-i] = b

for i in range(len(list)):
    print(list[i], end=' ')