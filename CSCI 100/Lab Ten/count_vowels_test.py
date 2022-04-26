from count_vowels import count_vowels

def test_count_vowels():
    # Write tests below this line. Do not remove.
    # Follow the indent for this comment
    assert count_vowels([['y', 'i'], ['x', 't', 'm'], ['r', 'a', 'p', 's'], ['e']]) == 3
    assert count_vowels([['a', 'p', "p", 'p', 'l', "e"], ['p', 'e', 'e'], ['a', 'a', 'k', 's'], ['e']]) == 7
    assert count_vowels([['a', "e", "a", "e"], ["k" 'e', 'e'], ['a', 'a', 'k', 's'], ['e'], ["p"]]) == 8
    
    
  # Write tests above this line. Do not remove.

test_count_vowels()
