#Paste your Queue class implementation from previous module here
from collections import deque

class QueueLL:
  def __init__(self):
    self.__data = deque()

  def __len__(self):
    return len(self.__data)

  def enqueue(self, object):
    self.__data.append(object)

  def dequeue(self):
    if len (self.__data) > 0:
      return self.__data.popleft()
    return "Queue is empty!"
  
  def queue(self):
    return self.__data

