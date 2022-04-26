
def anagram(word, match):
    """
    The function should return true if the word is an anagram of the match word.
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
    For instance,

    "evil" : "vile",
    "a gentleman" : "elegant man"
    "William Shakespeare" : "I am a weakish speller"

    Input: word = "evil", match = "vile"
    Output: anagram(word, match) -> True

    Input: word = "eyes ", match = "yess"
    Output: anagram(word, match) -> False

    Input: word = "Eleven Plus Two", match = "twelve plus one"
    Output: anagram(word, match) -> True

    """
    
    word = word.lower()
    match = match.lower()

    word_letters = {letter: 0 for letter in word if letter not in (" ", "")}
    match_letters = {letter: 0 for letter in match if letter not in (" ", "")}

    for letter in word:
        if letter not in (" ", ""):
            word_letters[letter] += 1
    for letter in match:
        if letter not in (" ", ""):
            match_letters[letter] += 1

    return word_letters == match_letters



