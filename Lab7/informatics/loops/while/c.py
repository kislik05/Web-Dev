n = int(input())
        
i, a = 0, 2

while i <= n:
    if a ** i <= n:
        print(a ** i)
    i += 1