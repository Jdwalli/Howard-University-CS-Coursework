from single_number import single_number

def test_single_number():
    # Example test, this does not count as one of your tests
    assert single_number([4, 1, 2, 1, 2]) == 4

    # Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert single_number([3, 4, 2, 3, 1, 4, 2, 1, 0]) == 0
    assert single_number([0.25, 0.45, 0.252, 0.25, 0.45]) == 0.252
    assert single_number([-1, -4, -4, -4, -4]) == -1

  # Write tests above this line. Do not remove.

test_single_number()
