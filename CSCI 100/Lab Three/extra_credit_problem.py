input_string = input()
consec_number = 0
output = ""



for i in range(len(input_string)):
    output += input_string[i]
    if i == len(input_string) - 1:
        if input_string[i - 1] == input_string[i]:
            consec_number += 1
            output += str(consec_number)
        else:
            consec_number += 1
            output += str(consec_number)
        break

    
    if input_string[i] == input_string[i + 1]:
        consec_number += 1
    else:
        if consec_number >= 0:
            consec_number += 1
            output += str(consec_number)
            consec_number = 0



			

print(output)

