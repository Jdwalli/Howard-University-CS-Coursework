

"""
1. Nested Factorials

Factorials

Your math professor introduced a new topic in class called factorials. After the class ended your friend asks you if you could explain the topic better as they are struggling to understand.
You explain that factorials only work with integers. The factorial of a non-negative integers n, denoted by n!, is the product of all positive integers less than or equal to n. The factorial of n also equals the product of n with the next smaller factorial.

Problem

Write a nested function explaining factorial to your friend. 
The first function goes through the giving list and checks items in the list are integers or not. 
If the items are not numbers, they are removed from the list. If they are integers however, 
they are passed on to the inner function which finds its factorial and returns a list with the factorials of all the number items in the list.

Example Test Cases

Test Case #1:
list = [0, 3, 2, "a", "1"] returns [1, 6, 2]
0 factorial is 1, 3 factorial is 6, 2 factorial is 2, “a” and “1” are strings.

Test Case #2:
list = [-5, -4, "word"] returns []
There are no positive integers

Test Case #3:
list = [1, 2, 3, 4, 5, 6] returns [1, 2, 6, 24, 120, 720]

Constraint

You must use the functions created. Do NOT change the names.
Negative numbers should be removed from the list
Do NOT use 3rd party libraries or anything you need to import.
If there are no integers return an empty list
"""

def factorial_finder(a):
    solution = []
    def fact(n):
        if n == 0 or n == 1:
            solution.append(1)
        else:
            factorial = 1
            while(n > 1):
                factorial = factorial *  n
                n = n - 1
            solution.append(factorial)
    for element in a:
        if isinstance(element, int) and element >= 0:
            fact(element)
        else:
            a.remove(element)
    return solution


if __name__=="__main__":
    assert factorial_finder([0, 3, 2, "a", "1"]) == [1, 6, 2]
    assert factorial_finder([-5, -4, "word"]) == []
    assert factorial_finder([]) == []
    assert factorial_finder([1, 2, 3, 4, 5, 6]) == [1, 2, 6, 24, 120, 720]
