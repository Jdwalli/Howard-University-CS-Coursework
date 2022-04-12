"""

Background
The CS department has hired you to calculate the Graduation checklist for all CS majors.
Your job is to create a record of all the students in the department, id, their classification and number of credits.
Instruction
Complete the functions in student_record.py.
Do NOT use any third party libraries
This lab MUST be completed before you can do the next lab
In your __init__ function you are to create a dictionary to store the information of each student.
The information in the init function should then be used to make the student dictionary
In the add_info function, the student dictionary built in create_info should be added to the student_record.
Explanation
Your code should add these information in the create_info function
'name': 'James Anderson', 'classification': "Sophomore", 'id': "02228211", 'number_of_credit': 70
'name': 'Sam Barnes', 'classification': "Freshman", 'id': "03258411", 'number_of_credit': 20
'name': 'Ashley Summers', 'classification': "Senior", 'id': "01429895", 'number_of_credit': 110
After each info has been created they should then be added to the student_record list in the add_info function and the student record should be returned.



"""




class StudentRecord:
  student_record = []
  

  def __init__(self):
    self.student_dict = {}

  def create_info(self, name, id, classification, number_of_credit):
    self.name = name
    self.id = id
    self.classification = classification
    self.number_of_credit = number_of_credit

    self.student_dict = {
      "name" : self.name,
      "id" : self.id,
      "classification" : self.classification,
      "number_of_credit" : self.number_of_credit
    }

  def add_info(self):
    StudentRecord.student_record.append(self.student_dict)
    return StudentRecord.student_record