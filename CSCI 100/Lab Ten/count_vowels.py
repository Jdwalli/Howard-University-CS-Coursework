def count_vowels(items):
    """
    the function takes a 2D list of lower case alphabets and returns 
    a total count of vowels in the 2D list. 
    """
    vowels = ("a", "e", "i", "o", "u")
    vowel_count = 0

    for row in items:
        for char in row:
            if char in vowels:
                vowel_count += 1

    return vowel_count