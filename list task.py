# # # # # Create a list of fruits and append a new fruit to the list.
numbers=[1,2,3,4,5]
print(numbers)

numbers.append('fruit')
print(numbers)

# # # # # Create a list of numbers and remove a specific number from it.

numbers.remove('fruit')
print(numbers)

# # # # Create a list of 5 cities and use pop() to remove the last city.


numbers.pop()
print(numbers)


# # # # Use extend() to combine two lists — one with fruits and another with vegetables.

numbers.extend(['apple','orange'])
print(numbers)

# # # Append three new elements to a list one by one using a loop.
num=[1,2,3]

for i in range (3):
#     element=input("enter the list")
    num.append(i)
    print(num)

# #     # Create a list of subjects and remove one subject entered by the user.

numbers=[1,2,3]
numbers.remove(2)
print(numbers)


# #     # Start with an empty list and keep appending numbers (from 1 to 5) using a loop.
num=[]

for i in range (1,5):  
    num.append(i)
    print(num)


# # #     # Create two lists: list1 = [10, 20, 30], list2 = [40, 50] → use extend() to join them.

numbers=[10,20,30]
numbers.extend([40,50])
print(numbers)

# # # # # Create a list of colors, then use pop(2) to remove the 3rd color.

numbers=[1,2,3]

numbers.pop(2)
print(numbers)
numbers.remove(1)
print(numbers)

# # Use append() inside a loop to build a list of even numbers from 2 to 10.

num=[2,4,6,8,10]

i=2
while(i<=10):
    print(i)
    i=i+2

# # Create a list [1, 2, 3, 4, 5].

# # Remove number 3 using remove().

# # Then pop the last element.

# # Finally, append two new numbers

numbers=[1,2,3,4,5]

numbers.remove(3)
print(numbers)

numbers.pop()
print(numbers)

numbers.append([5,6])
print(numbers)

# # Maintain a shopping list:

# # Append 3 new items.

# # Remove one item you no longer need.

# # Extend it with a list of “extra items”.

# # Pop the last item and print the final list.

numbers=[1,2,3,4,5]

numbers.append([1,2,3])
print(numbers)

numbers.remove(5)
print(numbers)

numbers.extend([10,20])
print(numbers)

numbers.pop()
print(numbers)

# # # Take a list of student names. Remove a name if it exists, otherwise append it.

numbers=[1,2,3,4,5,6]

numbers.remove(5)
print(numbers)

numbers.append(5)
print(numbers)

# # Combine two lists — one of names and one of marks — using extend(), and print the final combined list.

numbers=[1,2,3,4]

numbers.extend([11,12])
print(numbers)

# # Create a mixed list (numbers + strings). Remove all string elements using remove() inside a loop.

numbers=[1,2,3,4,"dinesh"]
for i in numbers[:]:
    if isinstance(i, str):
        print(numbers)

numbers.remove("dinesh")  
print(numbers)      



