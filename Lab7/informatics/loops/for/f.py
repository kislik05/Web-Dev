a = int(input())
a_str = str(a)

ans = ''

for i in a_str[::-1]:
    ans += i
        
print(int(ans))