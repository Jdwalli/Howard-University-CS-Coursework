from student_record import StudentRecord



"""
Background
After adding the students to the record, you are to access the record and determine how much required credits they need to graduate. You should also determine the minimum number of courses the student would need to take to reach this requirement.
You are to return a string with the students full name, numbers of credits needed, and number of courses.
Instruction
Complete the functions in student_result.py.
You are to return the student_records after deleting the student’s dictionary.
Do NOT use any third party libraries
This lab MUST be completed before you can do the next lab
Hint
A course can be a 4 credit, 3 credit or 1 credit course
Helper functions can be very useful
Make sure your returning from your functions and not printing
For this lab, assume a student needs 120 credits to graduate

3. Student Result
Explanation
From the records made in the previous question, you are to look for a particular student in the list. If the student is not in the list return "Student does not exist".
When the student has been found return the dictionary they are in.
From the information in the dictionary, find the number of credits they need to graduate and the minimum number of courses they need to take. Return both of these information. From the values you get return the flowing statement: "studentdict[name] needs credit_value credits and courses_value courses to graduate"
After this the student should be deleted from the records and the records should be returned.
For example if the student we are looking for is James Anderson, your print_message function is expected to return: "James Anderson needs 50 credits and 14 courses to graduate."



"""

class StudentResult(StudentRecord):
  student_records = [{"name":"James Anderson", "id":"02228211", "classification":"Sophomore", "number_of_credit":30},{'name': 'Sam Barnes', 'classification': "Freshman", 'id': "03258411", 'number_of_credit': 20},{'name': 'Ashley Summers', 'classification': "Senior", 'id': "01429895", 'number_of_credit': 110}]
  def student_finder(self, name):
    for index in range(0, len(StudentResult.student_records)):
      if StudentResult.student_records[index]["name"] == name:
        return StudentResult.student_records[index]

    return "Student does not exist"

  def credits_left(self, name):
    for student in range(0, len(StudentResult.student_records)):
      if StudentResult.student_records[student]["name"] == name:
        return 120 - StudentResult.student_records[student]["number_of_credit"]
    
  def courses_left(self, name):
    current_credits = self.credits_left(name)
    courses = 0

    four_credit_classes = current_credits // 4
    courses += four_credit_classes
    current_credits -= four_credit_classes * 4

    three_credit_classes = current_credits // 3
    courses += three_credit_classes
    current_credits -= three_credit_classes * 3

    if current_credits > 0:
      courses += current_credits
    
    return courses

  def return_message(self, name):
    return f"{name} needs {self.credits_left(name)} credits and {self.courses_left(name)} courses to graduate"
  
  def remove(self, name):
    for student in StudentResult.student_records:
      if name in student.values():
        StudentResult.student_records.remove(student)
    return StudentResult.student_records