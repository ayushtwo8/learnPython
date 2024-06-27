# Dictionary: used to store data values in key:value pairs.
# ordered, changeable and do not allow duplicate.
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year" : 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

# you can also use dict() constructor to make dictionary

x = thisdict.get("year")
print(x)

print(thisdict.keys())

thisdict["color"] = "green"
print(thisdict)

print(thisdict.values())

# items() method 
print(thisdict.items())

# update() method
thisdict.update({"year":1920})
print(thisdict)

#pop() method
student = {
    "name":"Rohan",
    "age":25,
    "college":"IIT Delhi",
    "friend":"Sohan"
}

print(student.pop("friend"))
print(student)

#popitem() - removes the last inserted item
print(student.popitem())
print(student)

#del keyword
del student["age"]
print(student)

del student #student dictionary is deleted here

#clear() method can be used to empty dictionary

#copy a dictionary
car1 = {
    "brand" : "tesla",
    "model" : "tesla x",
    "year" : 2020
}

car2 = car1.copy()
print(car2)

# using dict function
car3 = dict(car1)
print(car3)