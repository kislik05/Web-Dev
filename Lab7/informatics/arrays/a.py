n = int(input())
list = list(map(int, input().strip().split()))

for i in range(0, len(list), 2):
    print(list[i], end=' ')