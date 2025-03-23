n = int(input())
list = list(map(int, input().strip().split()))

cnt = 0

for i in list:
    if i > 0:
        cnt += 1
        
print(cnt)