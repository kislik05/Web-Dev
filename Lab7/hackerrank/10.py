def swap_case(s):
    swapped_string = ''
    for char in s:
        if char.isupper():
            swapped_string += char.lower()
        elif char.islower():
            swapped_string += char.upper()
        else:
            swapped_string += char
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)