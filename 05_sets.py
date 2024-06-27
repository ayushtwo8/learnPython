# Sets: unindexed, ordered, unchangeable(except remove and add) 
# and don't allow duplicate values.

set1 = {"appe","dosa","idli"}
print(set1)

set2 = {"fulki","chaat","samosa","kachori","fulki"}
print(set2)

# set considers (True and 1) and (False and 0) as same

set3 = {True,1,"Ram Mohan Singh"}
print(set3)

# the set() constructor

fruitsBasket = set(("apple","banana","cherry"))
print(fruitsBasket)

# accessing the set
toPrintSet = {"ram","mohan","sohan"}
for x in toPrintSet:
    print (x)

# add method in set
toPrintSet.add("himanshu")
print(toPrintSet)   

setNo1 = {"akshat","krishna","shekhar"}
setNo2 = {"pankaj","kshitij","devansh","aman"}

setNo1.update(setNo2)

print(setNo1)

# remove set items

sports = {"cricket","football","tennis","kabaddi"}
sports.remove("football")

print(sports)

# discard set items

games = {"ludo","snake&ladder","sudoku"}
games.discard("snake&ladder")

print(games)

# if item to remove does not exist then
# remove() will raise error but discard() will not raise any error

games.pop()
print(games)

games.clear()
print(games)

# del games 
# print(games)

# operations in set

A = {"a","b","c","d","hello"}
B = {1,2,3,4,"hello"}
L = ["ram","hari"]

C = A.union(B) #or C = A | B
print(C)

# with union() method we can join a set with other datatypes
# but with | we cannot join set with other datatypes

D = A.union(B,L)
print(D)

E = A.intersection(B) #or E = A & B
print(E)

F = A.difference(B) #difference: -
print(F)

G = A.symmetric_difference(B) #symmetric_difference: ^
print(G)