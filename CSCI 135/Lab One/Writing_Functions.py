"""
1. Double Alternate
Example
If the first list is [5,7,17,13,11,19] and the second is [12,10,2] the first list should become [5,7,12,17,13,10,11,19,2] and the second list becomes [] (or empty).
The elements of the second list should only be inserted when there are positions available in the first list. For example, if the fist list is [1,2,3] and the second list is [4,5,6,7,8] then after the function is called, the first list is [1,2,4,3] and the second list will be [5,6,7,8].
Return: Nothing but change the lists provided in-place.
"""

def doubleAlternate(arr1, arr2):
    arr1_index = 2
    arr1_length = len(arr1)
    arr2_length = len(arr2)
    
    while arr2_length > 0 and arr1_index <= arr1_length:
        arr1.insert(arr1_index, arr2[0])
        arr1_index += 3
        arr2.pop(0)
        arr1_length = len(arr1)
          
"""
2. Missing Numbers
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. Two of the integers are missing in the list. Write an efficient code to find the missing integer.
Return a tuple of the two missing numbers in ascending order.
Input: [1,4,2,3,6,9,8]
Output: (5,7)    
"""

def missing_num(nums):
    num_set = set(nums)
    solution = [i for i in range(min(nums), max(nums) + 1) if i not in nums]
    
    return tuple(solution)


if __name__ == "__main__":
    assert missing_num([1,4,2,3,6,9,8]) == (5,7)
    assert missing_num([10, 11, 13, 14, 16, 17]) == (12,15)
    assert missing_num([25, 26, 28, 29, 31]) == (27,30)

