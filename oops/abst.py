from abc import ABC, abstractmethod


class person(ABC):

    def __init__(self,name,email):
        self.name=name
        self.email=email

    def __str__(self):
        return f'hello {self.name}'
    
    def busfacility(self):
        return 'free bus provided'
    
    @abstractmethod   #important method complysy it should call in child fn
    def coursedetails(self):
        pass

    
class student(person):
    def __init__(self,name,email,course):
        super().__init__(name,email)
        self.course=course

        
      

    def __str__(self):
        return f'hello {self.name} with {self.course}'
    
    def busfacility(self):
        return f'perkm 5000 rs per year. minimum 20000 per year'
    
    def coursedetails(self):
        return 'hello this is your course details'
    


st1=student('dinesh','dinesh@gmail.com','btech it')

print(st1)
print(st1.busfacility())

#polymorphism