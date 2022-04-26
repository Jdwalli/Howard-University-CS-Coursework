def single_number(lst):
    s1 = set(lst)
    
    for element in s1:
        count = 0
        for integer in lst:
            if element == integer:
                count += 1
        if count == 1:
            return element