from Stack import Stack

# Video Notes:
# Make sure it does not start with a closing character
# 4 Open should be 4 CLOSING
# As we add matching, we can remove them from consideration
# List should be empty at the end 
# We want to close all opening characters 
# Always remove from top of stack 
# As we close a character, we are always popping from the top. Closing will always be matched to the most recent opening character
# O(n) for memory and time complexity

open_to_close_hash = {"{" : "}", "<" : ">", "#" : "#"}

def balancing_characters(s):
  stack = Stack()
  if not s:
    return False
  for index in range(len(s)):
    if len(stack) > 0 and stack.stack()[-1] == "#" and s[index]== "#":
      stack.pop()
    elif s[index] in open_to_close_hash:
      stack.push(s[index])
    else:
      if len(stack) > 0:
        if stack.stack()[-1] == open_to_close_hash[stack.stack()[-1]]:
          return False
        stack.pop()
    if(index == len(s) - 1 and len(stack)==0):
      return True
    if(index  == len(s) - 1 and len(stack) != 0):
      return False

      
if __name__ == "__main__":
  print(balancing_characters("<##"))

