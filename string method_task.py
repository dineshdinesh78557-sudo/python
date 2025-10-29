# Remove Extra Spaces
# 👉 Remove leading and trailing spaces from a string using .strip().

s= "remove extra...spaces..."
print(s.strip())

# # # Count Words in a Sentence
# # # 👉 Split a sentence into words using .split() and count the number of words

print(s.count("e"))

# # # Reverse Each Word
# # # 👉 Input: "hello world" → Output: "olleh dlrow"
# # # Use .split() and string slicing.

s="hello word"
print(s.split())

# # Join Words with a Separator
# # 👉 Join a list of words into a single string using .join().

s="hello word python"
print("".join(s))



# # Check Case Type
# # 👉 Check whether a string is uppercase, lowercase, or title case using .isupper(), .islower(), .istitle().

s="dinesh"
print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())
print(s.istitle())

# # # Count Vowels and Consonants
# # # 👉 Use a loop + .lower() to count vowels in a sentence.

s="dinesh messi"
print(s.lower())
print(s.count("s"))

# # Remove All Spaces
# # 👉 Remove all spaces in a string using .replace(" ", "").

s="dinesh,'f'"
print(s.strip())

# # Find the Longest Word in a Sentence
# # 👉 Split the string into words and find the longest word using len and loop

program="program"
for i in range (len(program)):
    print(i)

# # #     Check Palindrome
# # # 👉 Check if a given string reads the same forward and backward (e.g., "madam").
name=input("enter a string: ")
re =''
for i in name:
    re=i+re
if re==name:
    print("f{name}is palindrome")   
else:
    print("f{name} is not palindrome")     

# #     # Character Frequency
# # # 👉 Display how many times each character appears in a string using a loop and .count().

s="dinesh"
print(s.upper())

# # # Swap Case
# # # 👉 Convert uppercase to lowercase and vice versa using .swapcase().

s="dinesh"
print(s.swapcase())

# # # Title Case Conversion
# # # 👉 Convert every word’s first letter to uppercase using .title().

s="dinesh"
print(s.title())

# # # Check Alphanumeric
# # # 👉 Verify if a string contains only letters and numbers using .isalnum().

s='dinesh'
print(s.isalnum())


# # # Remove Digits from a String
# # # 👉 Input a string with digits → remove all digits using a loop and .isdigit().
s="1234"
print(s.isdigit())