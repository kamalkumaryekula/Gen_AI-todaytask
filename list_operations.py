
# data structures on python .
# list , tuple , set , dictionary .


## list:
# 1
l = [4, 7, 8, 9, 2, 1] 
print("l : ", type(l))

# 2
# List Examples

# Store homogeneous data items
l1 = [30, 32, 31, 35.5, 30, 36, 34] 

# Store multiple data items (non-homogeneous)
l2 = [1234, 'John', 230000.05, True] 

# List with single value
l3 = [99]

# Create empty list
l4 = []

# Create empty list using list()
l5 = list()

# Creating list using list()
l6 = list([4, 5, 6]) 

# 3
fruits = ["Apple", "Orange", "Banana", "Peach", "Grape"]
print (fruits[0], fruits[1]) # Accessing list elements using index

# 4
fruits = ["Apple", "Orange", "Banana", "Peach", "Grape"]
print (fruits[-1], fruits[-2]) #using negative indexing

# 5
fruits = ["Apple", "Orange", "Banana", "Peach", "Grape"]
print (fruits[5])  # index error: out of range

# 6
l = [2, 4, 3, 1, 7, 9, 8, 0, 6, 5]
print(l[:5]) # returns a list with first five elements
print(l[7:]) # returns a list with first seven elements
print(l[-3:]) # returns last three elements

# 7
l = [3, 4, 5, 8, 2, 1, 55, 4, 3, 12]
print(12 in l)
print(7 in l)
print(12 not in l)
print(7 not in l)

# 8
l = [3, 4, 5, 8, 2, 1]
print(len(l))  # length of list

# 9
l = [6, 7, 9, 5, 2, 5, 2, 1, 5]
print(l.count(5)) # count occurances of 5 in a list

# 10
# Modify value at specific index
i = 3
l = [6, 4, 5, 8, 2, 1]
l[i] = 99
print(l)

# 11
# Add an element at the end
l = [6, 4, 5, 8, 2, 1]
l.append(99)
print(l)

# 12
l = [3, 4, 5]
s = [99, 55, 88]
l.append(s)
print(l)
print(l[3])
print(type(l[3]))
print(l[3][1])

# 13
# Extending a list with other sequences using extend()
l = [3, 4, 5]
s = [99, 55, 88]
l.extend(s)
print(l)
print(l[3])
print(type(l[3]))

# 14
l = [3, 4, 5]
l.extend(6)
print(l)  # type error : int is not iterable
# list.extend() expects an iterable (like another list, tuple, or string)

# 15
# Add an element at a specific index
l = [6, 4, 5, 8, 2, 1]
l.insert(2, 99)
print(l)

# 16
# Delete an element from the end
l = [6, 4, 5, 8, 2, 1]
rem = l.pop()
print ('Element removed is:', rem)
print(l)

# 17
# Delete an element from a specific index
l = [6, 4, 5, 8, 2, 1]
rem = l.pop(3)
print('Element removed from l is:', rem)
print(l)
# pop() function throws IndexError, if the index is invalid or if applied on an empty list

# 18
l = [6, 4, 5, 8, 2, 1]
rem = l.pop(6)
print('Element removed from l is:', rem)
print(l)  # indexerror : pop index out of range

# 19
l = [] 
rem = l.pop(0)
print('Element removed is:', rem)
print(l) # index eroor : because it is an empty list

# 20
# Find and delete an element with specified value
l = [6, 4, 5, 25, 2, 1, 25, 7]
l.remove(25)
print(l)

# 21
# Find the index of the given element
l = [6, 7, 9, 5, 2]
print(l.index(5))

# 22
# Concatenate lists
l1 = [3, 4, 6] 
l2 = [7, 8, 9]
print(l1 + l2)

fruits_1 = ["Apple", "Orange" ]
fruits_2 = ["Banana", "Peach"]
fruits_3 = ["Grape", "Pine Apple" ]
fruits_total =  fruits_1 + fruits_2 + fruits_3
print(fruits_total)

# 23
# We can also use "*" operator to join lists.
l1 = [3, 4, 6] 
l2 = [7, 8, 9]
l3 = [*l1, *l2]
print(l3)

fruits_1 = ["Apple", "Orange" ]
fruits_2 = ["Banana", "Peach"]
fruits_3 = ["Grape", "Pine Apple" ]
fruits_total =  [*fruits_1, *fruits_2, *fruits_3]
print(fruits_total)

# 24
# Multiplying list with a scalar
l = [3, 4, 6]
print (l * 3)  # repeates three times in the list

# 25
# Find the largest element
l = [6, 4, 5, 8, 2, 13, 3, 7, 9]
print(max(l))

# 26
# Find the smallest element
l = [6, 4, 5, 8, 2, 13, 3, 7, 9]
print(min(l))

# 27
# Add all the elements
l = [6, 4, 5, 8, 2, 13, 3, 7, 9]
print(sum(l))

# 28
# Reverse a list
l = [3, 4, 5, 2, 1]
l.reverse()
print(l)

# 29
# Reverse a list using slicing
l = [3, 4, 5, 2, 1]
print("Reverse: ", l[::-1])
print("Original: ", l)

# 30
# Convert to list
print(list('Apple'))

# 31
# List Unpacking
l = [2, 3, 4]
x, y, z = l

print("x : {} y : {} z : {}".format(x, y, z))

# 32
# Iterate elements in a list using "while" loop
i = 0
l = [6, 4, 5, 8, 2]

while i < len(l):
    print (l[i])
    i += 1

# 33
#Iterate elements in a list using "for" loop
l = [6, 4, 5, 8, 2]

for x in l:
    print(x)
##While iterating through a list using "for" loop, we cannot remove an element.

# 34
# Iterate elements in a list using "for" loop with enumerate()
fruits = ["Apple", "Orange", "Grape", "Banana", "Peach"]

for idx, fruit in enumerate(fruits):
    print(idx, fruit) 

# 35


