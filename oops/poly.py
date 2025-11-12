class person:

    def __init__(self,name,email):
        self.name=name
        self.email=email

    def __str__(self):
        return f'hello {self.name}'
    
    def busfacility(self):
        return 'free bus provided'
    
class student:
    def __init__(self,name,email,course):
        
        self.name=name

        self.email=email
        self.course=course

    def __str__(self):
        return f'hello {self.name} with {self.course}'
    
    def busfacility(self):
        return f'perkm 5000 rs per year. minimum 20000 per year'
    


st1=student('dinesh','dinesh@gmail.com','btech it')

print(st1)
print(st1.busfacility())

#polymorphism