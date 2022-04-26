#Prompt the user to enter a positive number 
Number = int(input("Enter a positive number: "))

#Implement the steps for Collatz conjecture using loop

while True:
  print(Number)
  if Number % 2 == 0:
    Number = Number / 2
  else:
    Number = (Number * 3)  + 1

  if Number == 1:
    print(Number)
    break
  