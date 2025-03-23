n = int(input())
        
k, ans = 1, 0

while k < n:
    k = k * 2
    ans = ans + 1
    
print(ans)