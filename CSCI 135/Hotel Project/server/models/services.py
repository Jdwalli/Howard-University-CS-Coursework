# Don't know if we're using this anymore...

class Service():
  services = [] #list of dictionaries, key (Name of the service) : value (Boolean, whether it has been done or not)

  def __init__(self, name, completion):
    self.name = name
    self.completion = completion #Boolean (T or F)

  def createServiceDict(self):
    completionStatus = ''
    if self.completion == True:
      completionStatus = 'Completed!'
    else:
      completionStatus = 'Incomplete.'
    
    serviceDict = {
      'Service' : self.name, 
      'Completion Satus' : completionStatus
    }

    self.services.append(serviceDict)

  def updateServiceStatus(self, name, updatedStatus):
    for service in self.services:
      if service['Service'] == self.name:
        service['Completion Status'] = updatedStatus   
      else:
        return 
     
  def printServiceList(self):
    print(self.services)

# service1 = Service('Laundry', False)
# service1.createServiceDict()
# service1.printServiceList()