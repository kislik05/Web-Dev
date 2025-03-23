n = input()

new_num = 0

for i in range(len(n)):
    new_num += int(n[i]) * (2 ** (len(n) - i - 1))

print(new_num)