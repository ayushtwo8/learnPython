#List : indexed, ordered, changeable and allow duplicate values.


list1 = ["hello","welcome","bye","hello"]
list2 = [3,6,3,9,8]
list3 = [True, False, True]
list4 = ["bonjour",True,28]

print(list1)
print(len(list4))

# list() constructor
thislist = list(("apple","banana","mango"))
print(thislist)

print(thislist[2])
print(thislist[0:2])

thislist[1] = "pineapple"

print(thislist)

#insert() method

thislist.insert(2,"watermelon")
print(thislist)

thislist.append("orange")
print(thislist)

thislist.extend(list2)
print(thislist)

thislist.remove(3)
print(thislist)

thislist.pop()
print(thislist)

del thislist[3]
print(thislist)

# del thislist #deletes entire list
thislist.clear() # empties the list
print(thislist)

print(range(len(thislist)))

# List comprehension

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

newlist = [x for x in fruits if "a" in x]
#syntax : newlist = [expression for item in iterable if condition == True]

print(newlist)        

newlist = [x for x in fruits if x != "apple"]
print(newlist)

# sort()
thislist = ["orange","apple","custard apple","mango"]
thislist.sort()
print(thislist)

onelist = thislist.copy()
print(onelist)