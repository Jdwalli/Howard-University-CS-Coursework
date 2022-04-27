#Copy and paste your stack implementation here
#Use this class to implement balancing_characters
from collections import deque

class Stack:
  def __init__(self):
    self.__data = deque()

  def stack(self):
    return self.__data

  def push(self, obj):
    self.__data.append(obj)
  
  def __len__(self):
    return len(self.__data)

  def pop(self):
    if len(self.__data) > 0:
      return self.__data.pop()
    return "Your stack is empty!!"   
