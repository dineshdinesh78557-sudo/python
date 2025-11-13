# # ðŸ”¹ Task 1: Vehicle Info System

# # Base Class: Vehicle â†’ attributes: brand, model, year
# # Child Classes:

# # Car â†’ adds seating_capacity

# # Bike â†’ adds engine_cc

# # ðŸŽ¯ Goal: Create objects for both Car and Bike and print their details.

from abc import ABC, abstractmethod


# # class student(ABC):

# #     def __init__(self,brand,model,year):
# #         self.brand=brand
# #         self.model=model
# #         self.year=year

# #     def __str__(self):
# #         return f'2013 {self.year}' 
# #     def phone(self):
# #         return f'mi samsung' 
# #     @ abstractmethod

# #     def digital(self):
# #         pass

# # class person(student):
# #     def __init__(self, brand, model, year,bike):
# #         super().__init__(brand, model, year)
# #         self.bike=bike
# #     def __str__(self):
# #         return f' {self.brand}   {self.year}  '
# #     def phone(self):
# #         return f'mi 10000,samsung 2000' 
# #     def digital(self):
# #         return f'airtel,jio,bsnl'
# # st1=person('hero',2000,2010,'ktm') 
# # print(st1)  
# # print(st1.phone()) 


# # ðŸ”¹ Task 2: School Management

# # Base Class: Person â†’ attributes: name, age
# # Child Classes:

# # Student â†’ adds roll_number, grade

# # Teacher â†’ adds subject, salary

# # ðŸŽ¯ Goal: Create objects for a student and a teacher, and display their information

# # class student(ABC):

# #     def __init__(self,name,age ):
# #         self.name=name
# #         self.age=age
# #     def __str__(self):
# #         return f'dinesh {self.name}' 
# #     def school_manage(self):
# #         return f'pass ,fail'
# #     @ abstractmethod
    

# #     def tech(self):
# #         pass
# # class person(student):
# #     def __init__(self, name, age,rollno,grade,salary,subject):
# #         super().__init__(name, age) 
# #         self.rollno=rollno
# #         self.grade=grade
# #         self.salary=salary
# #         self.subject=subject
# #     def __str__(self):
# #         return f' {self.grade}  {self.salary}' 
# #     def school_manage(self):
# #         return f'pass 50,fail40'   
# #     def tech(self):
# #         return f'tamil,english'
       
# # st1=person('dinesh',23,111,'a',10000,'tamil')
# # print(st1)  
# # print(st1.school_manage())  

# # ðŸ”¹ Task 3: Online Shopping

# # Base Class: Product â†’ attributes: name, price
# # Child Classes:

# # Electronics â†’ adds warranty_years

# # Clothing â†’ adds size, material

# # ðŸŽ¯ Goal: Create objects for each category and print their product details


# # class student(ABC):

# #     def __init__(self,name,price,years):
# #         self.name=name
# #         self.price=price
# #         self.years=years
# #     def __str__(self):
# #         return f'dinesh {self.name}' 
# #     def warrenty(self):
# #         return f'10 year' 
# #     @ abstractmethod

# #     def add():
# #         pass

# # class person(student):
# #     def __init__(self, name, price, years,size):
# #         self.size=size
# #         self.name=name
# #         self.price=price
# #         self.years=years
# #     def __str__(self):
# #         return f' {self.size} {self.price}' 
# #     def warrenty(self):
# #         return f'10 year'
# #     def add():
# #         return f'one two '
# # st1=person('dinesh',1000,7,12)   
# # print(st1)
# # print(st1.warrenty())

# # # ðŸ”¹ Task 4: Banking

# # # Base Class: Account â†’ attributes: account_number, balance
# # # Child Classes:

# # # SavingsAccount â†’ adds interest_rate

# # # FixedDeposit â†’ adds duration_years

# # # ðŸŽ¯ Goal: Create objects for both account types and print all details.

# class person(ABC):

#     def __init__(self,accno,balance,interest):
#         self.accno=accno
#         self.balance=balance
#         self.interest=interest
       
#     def __str__(self):
#         return f'10 {self.interest}'
#     def duration_years(self):
#         return f'welcome '
#     @ abstractmethod
#     def add(self):
#         pass

# class student(person):

#     def __init__(self, accno, balance, interest,year):
#         super().__init__(accno, balance, interest)  
#         self.year=year
#     def __str__(self):
#         return f' {self.year}' 
#     def duration_years(self):
#         return f'{self.accno} {self.balance}' 
#     def add(self):
#         return f'save is form'
# st1=student(111,1000,100,10)   
# print(st1)
# print(st1.duration_years())     


# ðŸ”¹ Task 5: Library Management

# Base Class: Book â†’ attributes: title, author
# Child Classes:

# FictionBook â†’ adds genre

# Magazine â†’ adds issue_month

# ðŸŽ¯ Goal: Create objects for both classes and show their details.

class student(ABC):

    def __init__(self,title,author,book):
        self.title=title
        self.author=author
        self.book=book
    def __str__(self):
        return f'smith {self.author}' 

    def issue_month(self):
        return f'2026'

    @ abstractmethod

    def year():
        pass

class person(student):

    def __init__(self, title, author, book,month):
        super().__init__(title, author, book)
        self.month=month
    def __str__(self):
        return f' {self.title} {self.author} {self.book} {self.month}' 
    def issue_month(self):
        return f' {self.month} ' 
    def year():
        return f'2025 month in ,2026'
st1=person('online','cook','python',2025)  
print(st1)
print(st1.issue_month())        

            

        


            
       




        
        


    
        