# 4) Write a function called is_palindrome that takes one
#    parameter (which is a string) and returns True if the
#    string is a palindrome (the same forwards and backwards).
#
#    Note that spaces do not perclude a string from being a
#    palindrome.
#
# e.g. is_palindrome("madam") -> True
#      is_palindrome("sends") -> False
#      is_palindrome("a man a plan a canal panama") -> True


def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

# 5) Write a function named first_substr which takes two parameters,
#     haystack and needle. Both parameters are strings. Your function
#     should return the first index of the first occurence of needle
#     inside haystack. If needle does not occur in haystack, return 
#     -1. Do not use the str.index method. You may use the "in"
#     keyword (but do not need to).
#
# e.g. first_substr("Haystack", "stack") -> 3
#      first_substr("Hollywood", "Hollywoo") -> 0
#      first_substr("team", "eye") -> -1


def first_substr(haystack, needle):
    return haystack.find(needle)


# 6) Write a function called similar_words which takes two
#     one-word strings as parameters. This function should return
#     True if the words are either exactly the same or one letter
#     off. Otherwise, it should print false. This function works
#     regardless of capitalization. If the words are different
#     lengths, they cannot be similar.
#
# e.g. similar_words("effect", "affect") -> True
#      similar_words("fishing", "bashing") -> False
#      similar_words("HELLO", "hella") -> True


def similar_words(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    letters_off = 0
    i = 0
    #If word is exactly the same
    if word1 == word2:
        return True

    if len(word1) != len(word2):
        return False
    else:
        while i < len(word1):
            if word1[i] != word2[i]:
	            letters_off += 1
            i += 1	    

    if letters_off > 1:
	    return False
    else:
	    return True




