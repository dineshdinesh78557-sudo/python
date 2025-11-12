
# Goal:
# Create a parent class Employee with attributes name and salary.
# Child class Manager should inherit Employee and add a new attribute department.

# ðŸªœ Instructions:

# Use super().__init__(name, salary)

# Add method show_details() to print all three values.



class parant:


    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __str__(self):
        return f'name---{self.name} salary----{self.salary}'   
    def greet(self):
        return f'boy {self.name}' 

class goal (parant):


    def __init__(self, name, salary,details):
        super().__init__(name, salary,) 
        self.details=details 

    def __str__(self):
        return f'name ----{self.name} salary----{self.salary} details----{self.details}'  
    def providedetails(self):
        return f'182,a covai{self.details} with salary{self.salary}.with name{self.name}'
    
st1=goal("dinesh","100000","xcxscdc")

print(st1)
print(st1.salary)
print(st1.providedetails())


# # # Instructions:

# # # Use super().__init__(title, author)

# # # Add method display() to print book and file info.

# class book:

#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
        
#     def __str__(self):
#         return f'title----{self.title} author----{self.author} display-----{self.display}'
#     def greet(self):
#         return f'india {self.display}'  
    
# class use (book):
 
#     def __init__(self, title, author,display):
#         super().__init__(title, author)  
#         self.display=display
        

#     def __str__(self):
#         return f'title {self.title} author---{self.author} display----{self.display} '  
#     def providedisplay(self):
#         return f'dinesh {self.display} one{self.author} python{self.title} '
    
# st1=use('dinesh','one','python') 

# print(st1)
# print(st1.title)
# print(st1.providedisplay())

        
# # # # Goal:
# # # # Parent class Vehicle â†’ attributes brand, model.
# # # # Child class Bike(Vehicle) â†’ add cc (engine capacity).

# # # ðŸªœ Instructions:

# # # Initialize parent attributes using super()

# # # Add a method show_bike() â†’ print all details.

# class vehicle:

#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def __str__(self):
#         return f'brand---{self.brand} model----{self.model}'
#     def greet(self):
#         return f'2002 {self.model}' 

# class parent(vehicle):

#     def __init__(self, brand, model,bike):
#         super().__init__(brand, model) 
#         self.bike=bike  
#     def __str__(self):
#         return f'brand---{self.brand} model-----{self.model} bike----{self.bike}' 
#     def providebike(self):
#         return f'honda {self.brand} 2025 {self.model} splender {self.bike}'   

# st1=parent('honda','2025','splendar')  
# print(st1) 
# print(st1.brand)  



# # Parent class Teacher with attributes name and subject.
# # Child class MathTeacher(Teacher) adds experience_years.

# # ðŸªœ Instructions:

# # Use super().__init__(name, subject)

# # Add method show_info() â†’ print all 3 details.

# class parent:


#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject

#     def __str__(self):
#         return f'name----{self.name} subject----{self.subject}' 
     
#     def greet(self): 
#         return f'tamil {self.subject}'
     
# class tech(parent):

#     def __init__(self, name, subject,mark,rank,years):
#         super().__init__(name, subject)
#         self.mark=mark
#         self.rank=rank
#         self.years=years


#     def _str_(self):
#         return f' {self.mark} ---- {self.rank}--- {self.years} '  
    
#     def provideinfo(self):
#         return f' 100 {self.rank}  a {self.mark}  10 {self.years}'
    
# st1=tech("dinesh","maths",90,"A",2000) 
# print(st1)   
# print(st1.provideinfo())


# Goal:
# Parent class Customer â†’ attributes cust_name, mobile.
# Child class PremiumCustomer(Customer) â†’ add membership_level.

# ðŸªœ Instructions:

# Use super().__init__(cust_name, mobile)

# Add a method welcome_message() â†’ print "Welcome Premium Customer!" along with name and level.



class customer:


    def __init__(self,cust_name,mobile):
        self.cust_name=cust_name
        self.mobile=mobile

    def __str__(self):
        return f'cust_name----{self.cust_name} mobile----{self.mobile}'
    def greet(self):
        return f'9876654567 {self.mobile}'    
    

class child(customer):

    def __init__(self, cust_name, mobile,level):
        super().__init__(cust_name, mobile)
        self.level=level

    def __str__(self):
        return f'welcome_message----{self.level}'
    def providemessage(self):
        return f'Welcome Premium Customer! along with {self.cust_name} and level {self.level}'
    
st1=child('dinesh',9877655444,'platinum')
print(st1)
    




        