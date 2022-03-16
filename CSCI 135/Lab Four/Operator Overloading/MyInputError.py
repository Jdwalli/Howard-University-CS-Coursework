'''Complete this class below as specified'''
class MyInputError(Exception):
  def __init__(self, string):
    self.string = string

  def __str__(self):
    return self.string

''' Add your tests code under this if statement only '''
''' DO NOT ADD Test code elsewhere. '''
''' DO NOT REMOVE or COMMENT OUT below this line'''
if __name__=="__main__":
  print(MyInputError)