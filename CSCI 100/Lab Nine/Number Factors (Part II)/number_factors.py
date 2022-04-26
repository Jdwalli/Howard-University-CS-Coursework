
def number_factors(number):
    """
    The function should return a list of factors for a given number.
    A factor for a number divides the number.

    For instance,
    factors of 6 -> [1, 2, 3, 6]
    factors of 20 -> [1, 2, 4, 5, 10, 20]

    Input: number = 25
    Output: number_factors(number) -> [1, 5, 25]
    
    """
    return [i for i in range(1, number  + 1) if number % i == 0]

