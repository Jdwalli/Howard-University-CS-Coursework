from number_factors import number_factors

def test_number_factors():
    # Example test, this does not count as one of your tests
    assert number_factors(6) == [1, 2, 3, 6]

    # Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert number_factors(200) == [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200]
    assert number_factors(22) == [1, 2, 11, 22]
    assert number_factors(1) == [1]

    
    # Write tests above this line. Do not remove.

test_number_factors()
