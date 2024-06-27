# Tuple: inedexed, ordered, unchangeable(immutable) and allow duplicate values.

tuple1 = ("apple","banana","cherry")

print(tuple1)
print(len(tuple1)) #length of the tuple

# one item tuple with comma and without comma

tuple2 = ("hari",)
print(type(tuple2)) #tuple

tuple2 = ("hari")
print(type(tuple2)) #string

# tuple() constructor

tuple3 = tuple((1,2,3,4,5))
print(tuple3)

# check if items exist
if 3 in tuple3:
    print("3 is present in tuple3")

# change tuple values
# tuples ar immutable but you can convert the tuple into list,
# change the list, and convert the list back into tuple.abs

changeTuple = ("hello","welcome","bye")
changedList = list(changeTuple)
changedList[1] = "Thank you"
changeTuple = tuple(changedList)

print(changedList)
print(changeTuple)

# add tuple to tuple

tupli = ("rohan","sohan","devansh")
newTupli = ("sanvika",) #don't forget to add comma 
tupli += newTupli
print(tupli)

# delete tuple

tooople = ("ram","shyam")
del tooople
# print(tooople) # this will give error since it is deleted

# unpacking a tuple
fruits = ("apple","banana","orange","blueberry")
(a,b,c,d) = fruits
print(a,b,c,d)

# using asterisk
veggies = ("carrot","cabbage","spinach")
(x,*y) = veggies
print(x)
print(y)

# join tuples
t1 = ("hello","this")
t2 = ("is","a","tuple")
t3 = t1 + t2
print(t3)

# tuple methods
print(t3.count("is"))
print(t3.index("is"))