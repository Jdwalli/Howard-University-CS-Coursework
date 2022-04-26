def less_than_six(words):
    """
    the function takes a list of words and returns a list of words with length
    less than 6. 
    """
    return [word for word in words if len(word) < 6]

def divisible_by_thirteen():
    """
    the function generates numbers from 1 to 1000 which are only divisible by 13.
    """
    return [i for i in range(1, 1001) if i % 13 == 0]

def filter_vowels(sentence):
    """
    The function takes a string returns a list of all vowel letters present 
    in that string.
    """
    return [letter for letter in sentence if letter in ("a", "e", "i", "o", "u")]

def count_spaces(sentence):
    """
    The function takes a string, and returns a count of all spaces present
    in the string.
    """
    count = 0
    
    for char in sentence:
        if char == " ":
            count += 1
    return count

def word_lengths(words):
    """
    the function takes a list of words/strings, and returns a dictionary 
    with keys as the words, and values as the length of the key/word.
    """
    return {element : len(element) for element in words}
        