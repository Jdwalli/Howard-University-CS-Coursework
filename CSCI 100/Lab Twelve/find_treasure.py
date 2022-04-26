def find_treasure(treasure, stuff):
    s1 = set(treasure)
    count = 0
    
    for char in s1:
        for letter in stuff:
            if char == letter:
                count += 1
    return count
    
            