class AccessModifiers():
    def __init__(self, publicInstanceVariable, protectedInstanceVariable, privateInstanceVariable):
      # Public ( list of palindromes (all elements are not guaranteed to be palindromes though) )
      self.publicInstanceVariable = publicInstanceVariable
      # Protected ( given protected variable will be a list of anagrams (all elements are not guaranteed to be anagrams though) )
      self._protectedInstanceVariable = protectedInstanceVariable
      # Private ( given private variable will be a list of integers (all elements are not guaranteed to be integers though) )
      self.__privateInstanceVariable = privateInstanceVariable
    
    def _strip_characters(self, element):
        """
            Remove characters that do not matter
            For both palindromes and anagrams punctuation and/or special characters 
            and/or integers could be included BUT should be IGNORED
        """
        clean_string = ""
        for character in element.lower():
            if character.isalpha():
                clean_string += character
        return clean_string

    def _is_palindrome(self, word):
      if word == "":
        return False
      else:
        return word == word[::-1]

    def _create_frequency_dict(self, string):
        freq = {char : 0 for char in string}
        for char in string:
            freq[char] += 1
        return freq

    def _is_anagram(self, element1, element2, k):
        freq1 = self._create_frequency_dict(element1)
        freq2 = self._create_frequency_dict(element2)

        if freq1 == freq2:
            return True
        else:
            pass

    def __privateInstanceMethod(self) -> int:
        odd_add = True
        even_add = False
        odd_sum = 0
        even_sum = 0
        for element in self.__privateInstanceVariable:
            if isinstance(element, int):
                if element % 2 == 0:
                    if even_add:
                        even_sum += element
                        even_add = False
                    else:
                        even_sum -= element
                        even_add = True
                else:
                    if odd_add:
                        odd_sum += element
                        odd_add = False
                    else:
                        odd_sum -= element
                        odd_add = True
        return even_sum * odd_sum

    def publicInstanceMethod(self) -> tuple:
        valid_palindromes = []
        valid_anagrams = []
        
        for index, element in enumerate(self.publicInstanceVariable):
            if isinstance(element, str):
                element = self._strip_characters(element)
                if self._is_palindrome(element):
                    valid_palindromes.append(self.publicInstanceVariable[index]) 
        
        for index, element in enumerate(self._protectedInstanceVariable):
            word1, word2, k = element
            if len(self._strip_characters(word1)) - k == len(self._strip_characters(word2)):
                valid_anagrams.append(element)
            if len(self._strip_characters(word2)) - k == len(self._strip_characters(word1)):
                valid_anagrams.append(element)
        return (valid_palindromes, valid_anagrams, self.__privateInstanceMethod())
