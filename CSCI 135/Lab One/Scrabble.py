def LongestCommonSuffix(word_list):
    longest_suffix = []
    if len(word_list) == 0: 
        return ""
    for index in range(len(word_list)):
        word_list[index] = word_list[index][::-1]
        
    for i in range(len(min(word_list))):
        character = word_list[0][i]
        if all(letter[i] == character for letter in word_list):
            longest_suffix.append(character)
        else:
            break
    
    return "".join(longest_suffix[::-1])
        
        
            
word_list = ["cable", "table", "capable", "usable"]
assert(LongestCommonSuffix(word_list)) == "able"
word_list = ["charge", "barge", "change", "range"]
assert(LongestCommonSuffix(word_list)) == "ge"
word_list = []
assert(LongestCommonSuffix(word_list)) == ""
word_list = ["laptop", "car", "mat"]
assert(LongestCommonSuffix(word_list)) == ""