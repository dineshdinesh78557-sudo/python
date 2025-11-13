class bank():
    
    def __init__(self,name,accno,bal):
        self.name=name #public
        self._accno=accno #protected
        self.__bal=bal #private

    
    def getbal(self):
        return self.__bal
    
    def setbal(self,value):
          self.__bal=value
    


bank1=bank('dinesh',34568999,500)
print(bank1.name)
print(bank1._accno)
# print(bank1.__bal) //invalid we cant acces private variable outside


print(bank1.getbal())

bank1.setbal(0)

print(bank1.getbal())