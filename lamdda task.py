# # Task 1: Convert all strings in a list to uppercase

name=['python','hi','hello','welcome']
result=list(map(lambda n: n.upper(),name))
(result)

# #Task 2:Add 5 to every element in the list

every=[1,2,3,4,5]
element=list(map(lambda every:every*5,every))
print(element)

# #Task 3: Convert a list of temperatures in Celsius to Fahrenheit

Celsius=[10,20,30]
fahrenheit=list(map(lambda c:(c*3/4)+67 ,Celsius))
print(fahrenheit)


# # Task 4:Square of all even numbers in the list

even=[2,4,5]
num=list(map(lambda even:even*8,even))
print(num)

# # Task 5: Extract first character from each string in a list

str=["dinesh"]
ch=list(map(lambda str:str.upper(),str))
print(ch)

# # Task 6: Get length of each word

words=['apple','banana','orange']
len=list(map(len,words))
print(len)


# # Task 7: Multiply corresponding items in two lists

list1=[1,2,3]
list2=[4,5,6]
multiply=list(map(lambda x,y:x*y,list1,list2))
print(multiply)


# # Task 8: Remove spaces from each string

string=["he llo","py thon","di nesh"]
space=list(map(lambda s:s.replace(" ",""),string))
print(space)

# # Task 1: Filter only even numbers from the list

even=[1,2,3,4]
number=list(filter(lambda even:even*5,even))
print(number)

 

# Task 2: Filter words with length > 3

words=['apple','banana','orange','mango']
result=list(filter(lambda w:len(w) > 4,words))
print(result)

# Task 3: Filter numbers greater than 50

number=[10,55,79,90]
greater_than_50=list(filter(lambda x:x > 50,number))
print(greater_than_50)

# # Task 4: Remove empty strings from a list

name=['dinesh','hope'," "]
non_empty=list(filter(lambda n:n!=' ',name))
print(non_empty)

# Task 5: Filter names starting with 'A'

name=['Ashok','Amla']
starting_with_A=list(filter(lambda n:n .startswith('A'),name))
print(starting_with_A)

# Task 6: Keep only positive numbers

number=[-10,0,30,40-3]
positive_numbers=list(filter(lambda n: n >0,number))
print(positive_numbers)


# Task 7: Keep only palindromes from a list

word=['dinesh','fort','copy','dart','mam','malayalam']
palindromes=list(filter(lambda w:w ==w[::-1],word))
print(palindromes)
                 