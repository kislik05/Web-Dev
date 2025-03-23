a = int(input())

cnt = 2

for i in range(2, int(a / 2) + 1):
    if a % i == 0:
        cnt += 1

print(cnt)