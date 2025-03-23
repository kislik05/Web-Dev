def min(a, b, c, d, ans):
    if ans > b: 
        ans = b
    if ans > c: 
        ans = c
    if ans > d: 
        ans = d
    return ans


list = list(map(int, input().strip().split()))
print(min(list[0], list[1], list[2], list[3], list[0]))