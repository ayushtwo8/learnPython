
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
