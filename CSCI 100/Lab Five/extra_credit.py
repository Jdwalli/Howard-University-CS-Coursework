# Extra credit) Write a function named population_growth which takes
#     three parameters, original_population, annum_growth and num_years.
#     This function returns the final population after the num_years.
#
#     Each year the population grows annum_growth from that year's.
#     population. The population grows to a value rounded to the nearest
#     whole number.
#
#     Raise a value error if years is negative with an appropriate message.
#
def population_growth(original_population, annum_growth, num_years):
    total = original_population
    
    if num_years < 0:
        raise ValueError("ERROR!")
    
    for i in range(1, num_years + 1):
        print(f"{total} -> {(total * annum_growth) + total}")
        total = round(total * annum_growth) + total 
    return int(total)
    


#17802 -> 19404.18 
#19404.18 -> 21,150.5562
#21150.5562 -> 23053