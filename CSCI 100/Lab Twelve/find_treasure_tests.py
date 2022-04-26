from find_treasure import find_treasure

def test_find_treasure():
    # Example test, this does not count as one of your tests
    assert find_treasure('abAB', 'aBcDeFeDcBa') == 4

    # Write tests below this line. Do not remove.
    assert find_treasure("pp", "apple") == 2
    assert find_treasure("jO", "HELLOmyNaMeIsJoshua") == 1
    assert find_treasure("djuenjf", "zzz") == 0
    # Follow the indent for this comment

    # Write tests above this line. Do not remove.

test_find_treasure()
