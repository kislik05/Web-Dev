n = int(input())
list = list(map(int, input().strip().split()))

cnt=0
for i in range(1, len(list)-1):
    if (list[i-1]<list[i] and list[i]>list[i+1]):
        cnt += 1

print(cnt)