def xor(x, y):
    return x != y
    
list = list(map(int, input().strip().split()))

if(xor(list[0], list[1])): 
    print(1)
else: 
    print(0)