#prompt the user to enter a whole number 
number = int(input("Enter a whole number: "))

#calculate the two values, x egg cartons full and y eggs left over
egg_cartons_full = int(number / 12)
eggs_left_over = number % 12

#print the two values; first x egg cartons full, then y eggs left over 

print(egg_cartons_full)
print(eggs_left_over)