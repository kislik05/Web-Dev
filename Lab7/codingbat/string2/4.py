def count_code(str):
    count, i = 0, 0
    
    while "co" in str[i:]:
        if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
            count += 1
        i += str[i:].index("co")+3
    
    return count