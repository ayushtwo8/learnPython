# Dictionary: used to store data values in key:value pairs.
# ordered, changeable and do not allow duplicate.
thisdict = {
    "brand":"ford",
    "model":"model",
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