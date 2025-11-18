# string methods:

s = "hello Python... welcome..."

print(s.capitalize())
print(s.upper())
print(s.title())
print(s.swapcase())
print(s.lower())
print(s.strip())  # remove extra spaces
print(s.lstrip())
print(s.rstrip())
print(s.find("e"))# return index of first occurance
print(s.find("z"))
print(s.index("e"))
# print(s.index("z")) if it is not found it will raise error
print(s.count("e"))# count occurance  of a sub string
print(s.endswith(".."))
print(s.startswith("hello"))
print(s.isalpha())
print("hello".isalpha()) # it will check whether all are alphabets
print(s.isalnum()) # it will check alphabets + numerics
print("hello123".isalnum())


# s="hi python... welcome..."
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.swapcase())
# print(s.capitalize())
# print(s.strip())#removes face form both ends
# print(s.lstrip())
# print(s.rstrip())
# print(s.find("e"))#return index of first occurance
# print(s.find("z"))w
# print(s.index("e")
# print(s.index("h"))
# print(s.count("o"))
# print(s.endswith(".."))
# print(s.startswith("hi"))#check if string string with given text
# print(s.isalpha())
# print("hi".isalpha())
# print(s.isalnum())
print("hi123".isalnum())#true if only letters/numbers

# print(s.isdigit())
# d="8378874 "
# d="KKKKKK"
# d="   "
# print(d.isdigit())# true if only digits
# print(s.islower())
# print(d.isupper())#true if all uppercase
# print(d.isspace())
# print(d.istitle())

print(s.split())# split string into list
# print(s.split("o"))
# print(s.split("."))
# print(",".join(s))#join list with sperator
# print(s.splitlines())
# print(s.replace("Python","javascript"))



