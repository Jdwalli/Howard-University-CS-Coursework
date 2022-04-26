def count(lst, x):
    """
    parameters: a list of integers, and an integer
    returns: count of the integer, x, present in the input list
    """
    return len([number for number in lst if number == x])
    