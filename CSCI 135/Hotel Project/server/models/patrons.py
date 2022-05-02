from datetime import date

class Patron():
  patronList = [] 
  
  def __init__(self, firstName, lastName, email, phone, address, cardNum, expMon, expYear, cvvNum, zipCode, orderConf, roomNum, roomType):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.phone = phone
    self.address = address
    self.cardNum = cardNum
    self.expMon = expMon
    self.expYear = expYear
    self.cvvNum = cvvNum
    self.zipCode = zipCode
    self.orderConf = orderConf
    self.roomNum = roomNum
    self.roomType = roomType
    self.fullName = self.firstName + " " + self.lastName

  def calcAge(self, dateofBirth):
    today = date.today()

    yearDifference = today.year - dateofBirth.year

    if ((today.month, today.day) < (dateofBirth.month, dateofBirth.day)) == 1:
      self.age = yearDifference -  1
    else:
      self.age = yearDifference

    return self.age
  
  def createBasicInfo(self):    
    basicInfo = {
      'Name' : self.fullName,
      'Phone' : self.phone,
      'Email' : self.email,
      'Age' : self.age,
      'Address' : self.address,
      'Room #' : self.roomNum,
      'Room Type': self.roomType
    }

    self.patronList.append(basicInfo)

  def paymentInfo(self):
    card = {
      'Name on Card' : self.fullName,
      'Card Number' : self.cardNum,
      'Expiration Month' : self.expMon,
      'Expiration Year' : self.expYear,
      'CVV Number' : self.cvvNum,
      'Zip Code' : self.zipCode
    }

    return card
    # I don't know what I want to do with this

  def modifyPatron(self, roomNum, itemsToUpdate): #using roomNum for now because there should only be one patron assigned to a room
    patronToUpdate = None
    for patron in self.patronList:
      if patron['Room #'] == roomNum:
        patronToUpdate = patron
        break

      if patronToUpdate:
        invalidItemsToUpdate = ['Name', 'Age', 'Room Type']
        updates = {}

        for item in itemsToUpdate:
          itemKey = list(item.keys())[0]
          if itemKey in invalidItemsToUpdate:
            return 'You cannot update this item.' #or pass (do nothing)
          else:
            itemValue = list(item.values())[0]
            updates.update({itemKey : itemValue})
        patronToUpdate.update(updates)
          
  def deletePatron(self, roomNum): #using roomNum for now because there should only be one patron assigned to a room
    patronToDelete = None
    patronIndex = 0

    for patron in self.employeeList:
      if patron['Room #'] == roomNum:
        patronToDelete = patron
        break
      patronIndex += 1

      if patronToDelete:
        self.patronList.pop(patronIndex)

    