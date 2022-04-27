# Please do not make any changes to this code!
class Node:
  def __init__(self, x , next = None):
    self.value = x
    self.next = next
    
  # for printing out the linked list
  def __str__(self):
    temp = self
    arr = []
    while temp!= None:
      arr.append(temp.value)
      temp = temp.next
    return "->".join([str(i) for i in arr])