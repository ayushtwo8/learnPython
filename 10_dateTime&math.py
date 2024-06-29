import datetime

currentTime = datetime.datetime.now()

print(currentTime)
print(currentTime.year)
print(currentTime.strftime("%A"))  # strftime() takes one parameter to specify the format of the returned string. 
print(currentTime.strftime("%B")) 

# %A : full weekday name
# %B : full month name
# similarly there are many formats, you can google

# create a date object

currentDate = datetime.datetime(2024,6,29)
print(currentDate)


#+++++++++++++ Math +++++++++++++#

print(min(5,19,20))
print(max(5,19,20))
print(abs(-7.25))
print(pow(2,10))

# for more math functions you can include math module. 

import math

print(math.sqrt(225))
print(math.ceil(1.4))
print(math.floor(1.4))
print(math.pi)