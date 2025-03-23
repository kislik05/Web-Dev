def pow(a, n):
    return a ** int(n)

list = list(map(float, input().strip().split()))
print(pow(list[0], list[1]))