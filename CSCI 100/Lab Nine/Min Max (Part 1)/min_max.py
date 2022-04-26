
def min_max(given_list):
    """
    The function takes a list of integers and return the minimum and maximum number from the input list.
    The function should return a list containing two numbers, the minimum and the maximum number (in this order)

    eg:
    input: given_list = [3, 5, 4, 8, 2],
    output: min_max(given_list) -> [2, 8]

    """
    # write your code here!
    return [min(given_list), max(given_list)]


print(min_max([9, 20, 32, 3920, 10*6, 10**5]))
