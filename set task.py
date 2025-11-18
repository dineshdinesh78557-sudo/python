# # 👉 Task 1: Find students present on both days (intersection)
# day1 = {"Ram", "Sita", "Gita", "Krishna"}
# day2 = {"Sita", "Arjun", "Krishna", "Radha"}
a={"Ram", "Sita", "Gita", "Krishna"}
b= {"Sita", "Arjun", "Krishna", "Radha"}
print(a.intersection(b))

# # 👉 Task 2: Find students who were present only on day1
a={"Ram", "Sita", "Gita", "Krishna"}
b={"Sita", "Arjun", "Krishna", "Radha"}
print(a.union(b))

# # # 👉 Task 3: Find all unique students across both days
a={"Ram", "Sita", "Gita", "Krishna"}
b={"Sita", "Arjun", "Krishna", "Radha"}
print(b.difference(a))

# # # 🔹 Tuple – Bus Seat Reservation
# # reserved_seats = (5, 12, 18, 25)
# # 👉 Task 1: Check if seat 12 is reserved

a=(5, 12, 18, 25)
if 12 in a:
    print("12 is reserved")

# #     # Task 2: Count how many reserved seats are in row 1–10

    a=(11,12,13,14,15,16,7)
    ta=a[::-1]
    print(ta)
 
#  # 👉 Task 3: Convert tuple to list and add a new reserved seat 30

a=(1,2,3,4,5)
a=list(a)
a.append(30)
print(a)

# # # cart = ["apple", "banana", "milk", "apple", "bread"]
# # # 👉 Task 1: Remove duplicates (customer shouldn’t be billed twice for same item)

dinesh = ["apple", "banana", "milk", "apple", "bread"]
print(dinesh)
 
dinesh.remove("banana") 
print(dinesh)

# # 👉 Task 2: Count total items


dinesh=["apple", "banana", "milk", "apple", "bread"]
print(dinesh.count("apple"))

# # Task 3: Sort items alphabetically

dinesh = ["apple", "banana", "milk", "apple", "bread"]
dinesh.sort()
print(dinesh)


# 🔹 Dictionary – Student Marks Report
marks = {
    "Ram": {"math": 80, "science": 70},
    "Sita": {"math": 90, "science": 95},
    "Krishna": {"math": 60, "science": 50}
}
# # 👉 Task 1: Print each student’s total marks

student={
    'ram':'80',
}
print(student)

# # 👉 Task 2: Find the topper in science

science={
    'sita':'95',
}
print(science)
 
 
   
# # Task 3: Add english subject marks for each student

english={
    'krishna':'50',
}
print(english)


# . Maintain a shopping cart (list of items). Add, remove, and update items.
   
list=[1,2,3,4,5,6]
list.append(7)
print(list)

list.remove(2)
print(list)

list.extend([8,9])
print(list)

# # # 2. Given a list of daily temperatures for a week, find the highest, lowest, and average temperature.
temperature=[10,20,30]

highest=max(temperature)
lowest=min(temperature)
average=sum(temperature)

print("highest temperature:",highest)
print("lowest temperature:",lowest)
print("average temperature:",average)

# . From a list of student names, remove duplicates and sort alphabetically.

student =["dinesh","rohit","dhoni","dhoni"]

student.remove("rohit")
print(student)

student.sort()
print(student)

# 4. Store 10 bank transactions (positive for deposit, negative for withdrawal) and calculate final balance.

withdrawal=[10,-20,30,40,-50,60,70,-80,90,100]
print(withdrawal)

positive=max(withdrawal) 
negative=min(withdrawal)
total=sum(withdrawal)

print("positive widthdrawal:",positive)
print("negative widthdrawal:",negative)
print("total balance:",total)




# 5. Given a list of words, find the longest and shortest word.

words=["dinesh","hp"]

longest=("dinesh")
print(longest)

shortest=("hp")
print(shortest)

# # Store GPS coordinates (latitude, longitude) in tuples and print them in a readable format.

gps=("latitude, longitude")
print(gps)

# # Create a tuple of months and allow the user to input a number (1–12) to display the correct month.
# Create a tuple of months

month=("jan","feb","mar","apr","may","june","july","aug","set","oct","nov","dec",)

num=int(input("enter of month(1–12):"))

if 1 <= num <=12:
    print("month:",month[num - 1])
else:

    print("invaild")    

# 3. Store employee data(ID, name, salary) in tuples and print all employee details.

data=("ID, name, salary")
num=int(input("employee details"))

id=(123,"dinesh",10000)
name=(1234,"dinesh",25000)
salary=(1,"dinesh",13000)
print(id)
print(name)
print(salary)  

# . Given a tuple of marks, calculate total and average.

marks=(10,20,30)

total=sum(marks)
average=total/len(marks)
print(total)
print(average)


# 5. Store 5 colors in a tuple and check if a user-input color exists.

color=("red","block","yellow","white","blue",)

col=int(input("enter a color:"))

if 1 <= col <=6:
    print("color:",color[3])

else:
    print("invalid")

 # From two sets of students (Cricket team, Football team), find students who play both games
  
student={"Cricket team, Football team"}

student.add("kabadi")
print(student)

# # Given a set of registered emails, check if a new email is already registered or not.

email={"dinesh@123@gmail.com"}

new_email={"dinesh@123@gmail.com"}

new=input("enter a email:")
if new_email in email:
    print("email not registered")
else:
    print("email already reg")    

# find the largest number

number=[2222,3333]
largest=number[0]

for number in number:
    if number>largest:
        largest=number
print("The largest number",largest)   

# Store unique cities visited during travel (no duplicates allowed).

cities=set()


cities.add("covai")
cities.add("covai")
print(cities)

# 4. Find common elements between two sets of numbers.

set1={10,20}
set2={10,20}

common=set1&set2
print(common)

# Create a set of all vowels in a given word.

word="dinesh"
vowels={'a','e','i','o','u'}

vowels_vowels=set(word)&vowels
print(set(word.lower()) & vowels)

# 1. Store student details (name, age, marks) in a dictionary and display them neatly.
student={
    'name':'dinesh',
    'age':"23",
    'marks':122,
}
print(student['name'])
print(student['age'])
print(student['marks'])

# Count word frequency in a sentence using a dictionary.

sentance={"apple,apple,banana,banana,mango,mango"}

word=sentance.split()
word_count={}
for word in word:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)    

# Create a phonebook dictionary (name → phone number) and allow lookup by name.

phonebook="samsung"
print(phonebook)

phone={
    'name':'galaxy',
    'phone no':'8778545600'
}
print(phone['name'])
print(phone['phone no'])

# Maintain a product inventory with product names as keys and quantities as values. Update stock when items are bought.

inventory={"apple":10,"banana":20,"orange":30}

item=input("enter product name:")
qty=input("enter qty buy")

if item in inventory:
    inventory[item]-=qty
    print("update stock:",inventory)

else:
    print("item not found")    
#  Store exam marks of 5 students in a dictionary and display topper(s).

marks={
    'a':90,
    'b':80,
    'c':70,
    'd':100
}
print(marks["d"])