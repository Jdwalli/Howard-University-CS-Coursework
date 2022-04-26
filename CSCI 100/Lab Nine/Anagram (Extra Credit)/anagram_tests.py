from anagram import anagram

def test_anagram():
    # Example test, this does not count as one of your tests
    assert anagram('anagram', 'nag a ram') == True
    assert anagram('AnAgRaM', 'nag a ram') == True
    assert anagram('hello', 'world') == False

    # Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert anagram("hello", "OLEHL") == True
    assert anagram("part", "traps") == False
    assert anagram("Mother in law", "Hitler woman") == True

    # Write tests above this line. Do not remove.

test_anagram()
