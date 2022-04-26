from different_occurrences_count import different_occurrences_count

def test_different_occurrences_count():
    # Example test, this does not count as one of your tests
    assert different_occurrences_count([2, 5, 4, 4, 1]) == [4, 3]

    # Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert different_occurrences_count([2, 5, 2, 2, 1]) == [2, 7]
    assert different_occurrences_count([1, 4, 3,4,5]) == [4, 2]
    assert different_occurrences_count([1, 3, 4, 3]) == [3, 2]

    # Write tests above this line. Do not remove.

test_different_occurrences_count()
