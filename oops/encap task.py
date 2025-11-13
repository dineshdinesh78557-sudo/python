# # ðŸ”¹ Task 1: Vehicle Info System

# # Base Class: Vehicle â†’ attributes: brand, model, year
# # Child Classes:

# # Car â†’ adds seating_capacity

# # Bike â†’ adds engine_cc

# # ðŸŽ¯ Goal: Create objects for both Car and Bike and print their details.

# # class vehicle():


# #     def __init__(self,brand,mod,date):
# #         self.brand=brand
# #         self._mod=mod
# #         self.__date=date

       

# #     def getmod(self):
# #         return self.__date
    
# #     def setmod(self,value):
# #         self.__date=value


        
       
    
# # vehicle1=vehicle('hero',2000,15)
# # print(vehicle1.brand)
# # print(vehicle1._mod)

# # print(vehicle1.getmod())
# # vehicle1.setmod(0)
# # print(vehicle1.getmod())


# # # ðŸ”¹ Task 2: School Management

# # # Base Class: Person â†’ attributes: name, age
# # Child Classes:

# # Student â†’ adds roll_number, grade

# # Teacher â†’ adds subject, salary

# # ðŸŽ¯ Goal: Create objects for a student and a teacher, and display their information.


# class student():

#     def __init__(self,name,age,grade):
#         self.name=name
#         self._age=age
#         self.__grade=grade
       
#     def getgrade(self):
#         return self.__grade
#     def setgrade(self,value):
#         self.__grade=value


# student1=student('dinesh',20,90)
# print(student1.name)
# print(student1._age)

# print(student1.getgrade())
# student1.setgrade(0)
# print(student1.getgrade())


# # mobile number address

class person():

    def __init__(self,mobile,address,number):
        self.mobile=mobile
        self._address=address
        self.__number=number

    def getnumber(self):
        return self.__number
    def setnumber(self,value):
        self.__number=value

person1=person('mi','covai',190) 
print(person1.mobile) 
print(person1._address) 

print(person1.getnumber())
person1.setnumber(0)
print(person1.getnumber())
        



        