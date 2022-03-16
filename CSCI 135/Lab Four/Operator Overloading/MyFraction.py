'''Complete this class below as specified'''
from math import gcd
from MyInputError import MyInputError 
class MyFraction():
  def __init__(self, numerator, denominator):
    self.n = numerator
    self.d = denominator

    if isinstance(self.n, int) == False or isinstance(self.d, int) == False:
      raise MyInputError("These are both not numbers!")

  def get_numerator(self):
    return self.n

  def get_denominator(self):
    return self.d

  
  def _check_denominator(self, d):
    if d == 0:
     raise MyInputError("You can not divide by zero!")


  def __add__(self, otherFraction):
    self.firstN = self.n
    self.firstD = self.d
    self.secondN = otherFraction.n
    self.secondD = otherFraction.d

    self._check_denominator(self.secondD)
    self._check_denominator(self.firstD)


    lcm = self.firstD * self.secondD // gcd(self.firstD, self.secondD)

    fracSum = (self.firstN * lcm // self.firstD) + (self.secondN * lcm // self.secondD)

    finalNum = fracSum // gcd(fracSum, lcm)

    lcm = lcm // (gcd(fracSum, lcm))

    return MyFraction(finalNum, lcm)

  def __sub__(self, otherFraction):
    self.firstN = self.n
    self.firstD = self.d
    self.secondN = otherFraction.n
    self.secondD = otherFraction.d

    self._check_denominator(self.secondD)
    self._check_denominator(self.firstD)


    lcm = self.firstD * self.secondD // gcd(self.firstD, self.secondD)

    fracSum = (self.firstN * lcm // self.firstD) - (self.secondN * lcm // self.secondD)

    finalNum = fracSum // gcd(fracSum, lcm)

    lcm = lcm // (gcd(fracSum, lcm))

    return MyFraction(finalNum, lcm)



  def __mul__(self, otherFraction):
    self.firstN = self.n
    self.firstD = self.d
    self.secondN = otherFraction.n
    self.secondD = otherFraction.d
    self._check_denominator(self.secondD)
    self._check_denominator(self.firstD)

    return MyFraction(self.firstN * self.secondN,  self.firstD * self.secondD)

  def __truediv__(self, otherFraction):
    self.firstN = self.n
    self.firstD = self.d
    self.secondN = otherFraction.n
    self.secondD = otherFraction.d
    self._check_denominator(self.secondD)
    self._check_denominator(self.firstD)

    return MyFraction(self.firstN * self.secondD, self.secondN * self.firstD)
  
  def __lt__(self, otherFraction):
    self._check_denominator(self.d)
    self._check_denominator(otherFraction.d)
    return (self.n /self.d) < (otherFraction.n / otherFraction.d)

  def __gt__(self, otherFraction):
    self._check_denominator(self.d)
    self._check_denominator(otherFraction.d)
    return (self.n /self.d) > (otherFraction.n / otherFraction.d)

  def __eq__(self, otherFraction):
    self._check_denominator(self.d)
    self._check_denominator(otherFraction.d)
    return (self.n /self.d) == (otherFraction.n / otherFraction.d)
  

''' Add your tests code under this if statement only '''
''' DO NOT ADD Test code elsewhere. '''
''' DO NOT REMOVE or COMMENT OUT below this line'''
if __name__=="__main__":
  print(MyFraction)