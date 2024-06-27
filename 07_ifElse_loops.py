# if...else

num1 = 500
num2 = 100

if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num1==num2:
    print(f"{num1} is same as {num2}")
else:
    print(f"{num1} is smaller than {num2}")    


#one line if-else statement:
a = 2
b = 350

print("A") if a>b else print("B")

# loops..

i = 0
while i<10:
    i+=1
    if i==3:
        continue
    if i==7:
        break
    print(i)
print("\n")

for x in range(6):
    print(x)
print("\n")    

for x in range(5,10):
    print(x)
print("\n")    

for x in range(5,50,3):
    print(x)
print("\n")    

# else keyword in for loop:

for x in range(10):
    print(x)
else:
    print("Finally finished..")   
print("\n")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!") #this will not printed
print("\n")    
