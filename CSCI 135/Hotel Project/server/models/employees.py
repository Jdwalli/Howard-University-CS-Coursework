import datetime
import random, json

class Employee():
  with open("data/hotel.json") as hotel_data:
    data = json.load(hotel_data)
  
  salaryMapping = data['employees']['base_salary_map']
  stepMapping = data['employees']['salary_step_map']
  employeeList = data['employees']['info']
  
  
  def __init__(self, firstName, midInitial, lastName, job, dateofBirth, phone, email, salStep, ssn):
    self.firstName = firstName 
    self.midInitial = midInitial
    self.lastName = lastName
    self.job = job
    self.dateofBirth = datetime.datetime.strptime(dateofBirth, '%Y-%m-%d')
    self.phone = phone
    self.email = email
    self.baseSal = self.salaryMapping[job]
    self.salStep = self.stepMapping[salStep]
    self.ssn = ssn  


  def _update_employee_json(self, new_employee):
    with open("data/hotel.json") as hotel_data:
      data = json.load(hotel_data)
      data['employees']['info'].append(new_employee)
    with open("data/hotel.json", "w") as hotel_data:
      json.dump(data, hotel_data, indent=4)
      
  def calcAge(self, dateofBirth):
    today = datetime.date.today()

    yearDifference = today.year - dateofBirth.year

    if ((today.month, today.day) < (dateofBirth.month, dateofBirth.day)) == 1:
      self.age = yearDifference -  1
    else:
      self.age = yearDifference

    return self.age

  def calcSalary(self, baseSal, salStep):

    self.salary = baseSal + salStep

    return self.salary
    
    #calculate employee's salary based on base salary and salary step

  def employeeID(self):
    self.idNum = ""

    for i in range(6):
      self.idNum += str(random.randint(0, 9))

    return self.idNum
    #need a randomizer to create a string full of random nums and letters
  
  def createEmployeeDict(self):
    fullName = self.firstName + " " + self.midInitial + " " + self.lastName #this is how I would want the output to show on the website
    
    employeeDict = {
      'Name' : fullName,
      'Phone' : self.phone,
      'Email' : self.email,
      'Age' : self.calcAge(self.dateofBirth),
      'SSN' : self.ssn,
      'Job Title' : self.job,
      'DOB' : str(self.dateofBirth),
      'SalStep' : self.salStep,
      'ID' : self.employeeID(),
      'Salary' : self.calcSalary(self.baseSal, self.salStep)
    }
    
    self._update_employee_json(employeeDict) 

  


class ModifyEmployee():
  with open("data/hotel.json") as hotel_data:
    data = json.load(hotel_data)
  employeeList = data['employees']['info']

  def __init__(self, ssn):
    self.employeeIndex = -1
    self.ssn = ssn.strip()
    
  def _employee_exist(self):
    for index, employee in enumerate(self.employeeList):
      if employee['SSN'] == self.ssn:
        self.employeeIndex = index
        return True
    return False

  def check_status(self):
    self.status = self._employee_exist()
    if self.status == True:
      return True
    else:
      return False

  def get_employee(self):
    self.employeeList[self.employeeIndex]["index"] = self.employeeIndex
    return self.employeeList[self.employeeIndex]


  def deleteEmployee(self): #using ssn for now because everyone's ssn is different
    with open("data/hotel.json") as hotel_data:
      data = json.load(hotel_data)

    for index, employee in enumerate(data['employees']['info']):
      if employee['SSN'] == self.ssn:
        del data['employees']['info'][index]
    with open("data/hotel.json", "w") as hotel_data:
      json.dump(data, hotel_data, indent=4)

  def modifyEmployee(self, modifiedInfo): #using ssn for now because everyone's ssn is different 
    with open("data/hotel.json") as hotel_data:
      data = json.load(hotel_data)
      salaryMapping = data['employees']['base_salary_map']
      stepMapping = data['employees']['salary_step_map']
    idNum = ""
    for i in range(6):
      idNum += str(random.randint(0, 9))
    modifiedInfo["ID"] = idNum
    modifiedInfo["Salary"] = salaryMapping[modifiedInfo['Job Title']] + stepMapping[modifiedInfo['Occupation Steps']]
    for index, employee in enumerate(data['employees']['info']):
      if employee['SSN'] == self.ssn:
        del data['employees']['info'][index]
        data['employees']['info'].insert(index, modifiedInfo)
    with open("data/hotel.json", "w") as hotel_data:
      json.dump(data, hotel_data, indent=4)
          
"""
NOTES: 
The employees class is complete but changes need to be made. There need to be methods for creating unique identification numbers for employees and creating additional attributes such as social security numbers, hire dates, and days worked.

The employee class should take in a person’s first name, middle initial, last name, job, date of birth, phone number, email, base salary, salary step, schedule, and SSN.
The employee class with have methods to calculate a person’s age, calculate someone’s salary based on their base and their step, and method to return all this data in a dictionary.
 There should be methods that handle deleting employees and modifying them within the class as well.

"""
  