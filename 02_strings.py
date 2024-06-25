
# Strings - Strings in python are arrays of bytes representing unicode characters

str1 = "Hello, Ayush"
print(str1[1])

for i in "banana":
    print(i)

print(len(str1))  # to find the length of a string
print("hello" in str1) #checking string

# Slicing string

str2 = " This is a sample string."
print(str2[2:20])
print(str2[:20]) #slice from the start
print(str2[10:]) #slice from the end
print(str2[-15:-5]) #Negative indexing
print(str2.upper()) #Upper case 
print(str2.lower()) #Lower case
print(str2.strip()) #remove whitespace
print(str2.replace("sample","premium")) #replace
print(str2.split(" ")) #split string on the basis of space

# String concatenation
str3 = "Radhe"
str4 = "Shyam"
str5 = str3 + str4
str6 = str3 +" "+ str4
print(str6)

#String format
age = 45
# txt = "Rahul's age is " + age #we can't combine number and string like this
txt1 = f"Rahul's age is {age}" #F-Strings in python

# Placeholder and modifiers

price = 99.9
txt2 = f"The price of earphones is {price:.2f}"
print(txt2)

txt3 = f"The price is {20*40} dollars."
print(txt3)

# Escape characters
esc1 = "This is a \"double quote\" and this is \'single quote\'"
esc2 = "\\ backslash \n \t tab \n \b backspace \n "
print(esc2)

#String methods

string1 = "welcome to this codebase."
string2 = "banana"

print(len(string1))
print(string1.capitalize()) #first character upper case
print(string1.center(27,'+'))

# visit this link for more string methods or you can also go to official documentation:
#https://www.w3schools.com/python/python_strings_methods.asp
