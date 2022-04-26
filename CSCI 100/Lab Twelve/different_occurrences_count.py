def different_occurrences_count(items):
    s1 = set(items)
    results = []
    s1_total = 0
    total = 0
    
    for element in s1:
        count = 0
        for item in items:
            if item == element:
                count += 1
        if count > 1:
            results.append(element)
    for integer in s1:
        s1_total += integer
    
    for integer in range(1, max(items) + 1):
        total += integer
    
    diff = total - s1_total
    
    results.append(diff)
    return results
    
    