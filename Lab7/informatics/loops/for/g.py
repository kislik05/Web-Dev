a = int(input())

i = 2

for i in range(2, a + 1):
    if a % i == 0:
        print(i)
        break