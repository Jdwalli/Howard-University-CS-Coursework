from functools import reduce

"""
1. Map Function

For input1 and input2 you will be given lists
    For input1 use the map function to figure out how many even numbers there are
    For input2 use the map function to figure out how many odd numbers there are

For input3 and input4 you will be given dictionaries
    For input3 use the map function to figure out which keys have even values
    For input4 use the map function to figure out which keys have odd values

Return the output of each map input
You must use the map function for each input (4 times)
Order of inputs and inputs values MUST be preserved

input: [1,8,10], [9,3,4], {'A':1, 'B':2, 'C':3}, {'A':4, 'B':2, 'C':3}
output: ([0, 1, 1], [1, 1, 0], [None, 'B', None], [None, None, 'C'])

Explanation:
# [1,8,10] -> 8 and 10 are even so they get changed to 1
# [9,3,4] -> 9 and 3 are odd so they get changed to 1

# {'A':1, 'B':2, 'C':3} -> 'B' is the only key with an even value so it's the only one that remains unchanged
# {'A':4, 'B':2, 'C':3} -> 'C' is the only key with an odd value so it's the only one that remains unchanged

"""
def mapped(input1:list, input2:list, input3:dict, input4:dict):
    input_one_map = list(map(lambda n: 1 if n % 2 == 0 else 0, input1))
    input_two_map = list(map(lambda n: 1 if n % 2 != 0 else 0, input2))
    input_three_map = list(map(lambda key: key if input3[key] % 2 == 0 else None, input3))
    input_four_map = list(map(lambda key: key if input4[key] % 2 != 0 else None, input4))
    
    return (input_one_map, input_two_map, input_three_map, input_four_map)    
            

"""
2. Filter Function
In filtered.py complete the filtered Function

For input1 and input2 you will be given lists
    For input1 use the filter function to figure out which values are even numbers
    For input2 use the filter function to figure out which values are odd numbers
    
For input3 and input4 you will be given dictionaries
    For input3 use the filter function to figure out which keys have even values
    For input4 use the filter function to figure out which keys have odd values

You will return 2 things from filtered
    1. The sum of what you get from filtering input1 and input2
    2. One list of all keys that have even values in input3 and odd values in input4

You must use the map function for each input (4 times)

input: [1,8,10], [9,3,4], {'A':1, 'B':2, 'C':3}, {'A':4, 'B':2, 'C':3}
output: 30 ['B','C']

Explanation:
[1,8,10] -> sum of even numbers (8,10) = 18
[9,3,4] -> sum of odd numbers (9, 3) = 12
18+12 = 30
 
{'A':1, 'B':2, 'C':3} -> keys with even values = 'B'
{'A':4, 'B':2, 'C':3} -> keys with odd values = 'C'
['B', 'C']

"""
def filtered(input1:list, input2:list, input3:dict, input4:dict):
    input_one_filter = list(filter(lambda n: 1 if n % 2 == 0 else 0, input1))
    input_two_filter = list(filter(lambda n: 1 if n % 2 != 0 else 0, input2))
    input_three_filter = list(filter(lambda key: key if input3[key] % 2 == 0 else None, input3))
    input_four_filter = list(filter(lambda key: key if input4[key] % 2 != 0 else None, input4))
    
    return ((sum(input_one_filter) + sum(input_two_filter)), input_three_filter + input_four_filter)    

print(filtered([1,8,10], [9,3,4], {'A':1, 'B':2, 'C':3}, {'A':4, 'B':2, 'C':3}))

"""
3. Reduce Function

In reduced.py complete the reduced Function

For input1 you will be given a list
    If the product of values passed into reduce function is even then add those values
    If the product of values passed into reduce function is odd then subtract those values
    
For this lab assume 0 is even
You must use the reduce function at least once

input: [1,2,3,5]
output: 5

Explanation:
1*2=2 ADD (since 2 is even) 1+2=3
3*3=9 SUB (since 9 is odd) 3-3=0
0*5=0 ADD (since 0 is even) 0+5=5
"""

def reduced(input1:list):
    solution = 0
    return reduce(lambda a, b: (a + b) if (a * b) % 2 == 0 else (a-b), input1)







