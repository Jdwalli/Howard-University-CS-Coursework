"""
    An anagram is a string formed by rearranging the characters of a different string. For example: “santa” is an anagram of “satan” and “below” is an anagram of “elbow”
    Problem
    Given 2 strings and an integer k≥ 0. By removing at most k number of character from either string, check if they are anagram of one another. Example: “string” is anagram of “gin” if we remove 3 characters ie "str". If we remove “str” we get “ing” which is an anagram of “gin”
    You cannot remove from both strings
"""

def almost_anagram(str1, str2, k):
    # Get a dict of all letter freqs for both list
    str1_freq = {i : 0 for i in str1}
    str2_freq = {i : 0 for i in str2}
    bad_letters = []
    
    for char in str1:
        str1_freq[char] += 1
    
    for char in str2:
        str2_freq[char] += 1
    
    if len(str1) > len(str2):
        for letter in str1:
            # test to see if the letter count in string2 is not greater 
            
            if letter not in str2_freq.keys():
                bad_letters.append(letter)
            else:
                if str2_freq[letter] > str1_freq[letter]:
                    return False
        return k >= len(bad_letters)
    else:
        for letter in str2:
            if letter not in str1_freq.keys():
                bad_letters.append(letter)
            else:
                if str1_freq[letter] > str2_freq[letter]:
                    return False  
        return k >= len(bad_letters)

if __name__ == "__main__":
    assert(almost_anagram("gable", "able", k = 1)) == True
    # You should be able to remove the g from string open so it should be true
    assert(almost_anagram("lable", "able", k = 10)) == True
    #You can remove one ‘l’ from str1 to get “abel” or "labe". Both of which can be rearraged to be 'able’. Since we were able to do it in 1 removal the output will be true. Note that the output will be true for k≥1 but not for k=0
    assert(almost_anagram("a", "able", k = 100)) == True
    #You can remove one 'ble from str2 to get “a” which is anagram of str1.
    assert(almost_anagram("aa", "able", k = 100)) == False
    #No matter how many character you remove from either string, since you cannot remove from both strings you cannot get a string that is the anagram of the other. So the output is False.
    assert(almost_anagram("hello", "world", k = 100)) == False
    assert(almost_anagram("ggable", "able", k = 1)) == False
    assert(almost_anagram("aaaa", "aaaaable", k = 100)) == True
