# Write a program which asks the user for student grades until the user types "done".
# The program should then compute the mean and median grades for all the students, rounded to two decimal places.
# See the instructions for further details.
def mean(grades):
    return round(sum(grades) / len(grades), 2)
def median(grades):
    if len(grades) % 2 == 0:
      Middle = int(len(grades) / 2)
      return round((grades[Middle] + grades[Middle - 1]) / 2, 2)
    else:
        return round(grades[int(len(grades) / 2)],2)
    # Your code!
    
    

# You also need to implement the rest of the code for run() below: 
def run():
    grades = []
    getting_input = True
    #Initialize a variable for a list to collect the grades 
    # Your code! 
    while getting_input:
        inp = input("Next grade: ")
        if inp == "done": 
            break
        else: 
            grades.append(float(inp))
            continue
    
    grades.sort()
            
    #print the mean grade by calling  mean(grades) function 
    print(mean(grades))
    
    #print the median grade by calling median(grades) function
    print(median(grades))
    

if __name__ == "__main__":
    run()