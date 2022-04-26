from min_max import min_max

def test_min_max():
    # Example test, this does not count as one of your tests
    assert min_max([3, 5, 4, 8, 2]) == [2, 8]

    # Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert min_max([1, 9, 1029, 2, -1, -3]) == [-3, 1029]

    assert min_max([9, 20, 32, 3920, 10*6, 10**5]) == [9, 100000]

    assert min_max([2, 20.02, 20.03, 20.10]) == [2, 20.10]

    # Write tests above this line. Do not remove.

test_min_max()
