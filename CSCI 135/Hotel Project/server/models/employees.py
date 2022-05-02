from datetime import date
import random

class Employee():
  employeeList = []
  
  def __init__(self, firstName, midInitial, lastName, job, dateofBirth, phone, email, baseSal, salStep, schedule, ssn):
    self.firstName = firstName
    self.midInitial = midInitial
    self.lastName = lastName
    self.job = job
    self.dateofBirth = dateofBirth
    self.phone = phone
    self.email = email
    self.baseSal = baseSal
    self.salStep = salStep
    self.schedule = schedule
    self.ssn = ssn  

  def calcAge(self, dateofBirth):
    today = date.today()

    yearDifference = today.year - dateofBirth.year

    if ((today.month, today.day) < (dateofBirth.month, dateofBirth.day)) == 1:
      self.age = yearDifference -  1
    else:
      self.age = yearDifference

    return self.age

  def calcSalary(self, baseSal, salStep):
    stepsDict = {
      1 : 500,
      2 : 1000,
      3 : 2500,
      4 : 4000,
      5 : 5000
    } #May change values later. Just a foundation for the diff steps

    self.salary = baseSal + stepsDict[salStep]

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
      'Age' : self.age,
      'SSN' : self.ssn,
      'Job Title' : self.job,
      'ID' : self.idNum,
      'Salary' : self.salary
    }
    self.employeeList.append(employeeDict) 

  def modifyEmployee(self, ssn, itemsToUpdate): #using ssn for now because everyone's ssn is different 
    employeeToUpdate = None
    for employee in self.employeeList:
      if employee['SSN'] == ssn:
        employeeToUpdate = employee
        break

      if employeeToUpdate:
        invalidItemsToUpdate = ['Name', 'Age', 'SSN']
        updates = {}

        for item in itemsToUpdate:
          itemKey = list(item.keys())[0]
          if itemKey in invalidItemsToUpdate:
            return 'You cannot update this item.' #or pass (do nothing)
          else:
            itemValue = list(item.values())[0]
            updates.update({itemKey : itemValue})
        employeeToUpdate.update(updates)
          
    #find the ssn and modify something about the employee 

  def deleteEmployee(self, ssn): #using ssn for now because everyone's ssn is different
    employeeToDelete = None
    employeeIndex = 0

    for employee in self.employeeList:
      if employee['SSN'] == ssn:
        employeeToDelete = employee
        break
      employeeIndex += 1

      if employeeToDelete:
        self.employeeList.pop(employeeIndex)
        
    #find the ssn and delete the entire 


"""
NOTES: 
The employees class is complete but changes need to be made. There need to be methods for creating unique identification numbers for employees and creating additional attributes such as social security numbers, hire dates, and days worked.


The employee class should take in a person’s first name, middle initial, last name, job, date of birth, phone number, email, base salary, salary step, schedule, and SSN.
The employee class with have methods to calculate a person’s age, calculate someone’s salary based on their base and their step, and method to return all this data in a dictionary.
 There should be methods that handle deleting employees and modifying them within the class as well.

"""
  