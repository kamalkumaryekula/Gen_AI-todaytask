
#1. Insert a new element into tuple at specified position.
t = (1, 2, 3, 4, 5, 6)
t_list = list(t)
t_list.insert(2, 8)   # index 2 లో 8 insert
t = tuple(t_list)
print("After insert:", t)


#2. Count even and odd numbers in a tuple.
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_count = 0
odd_count = 0

for num in tuple1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


#3. Modify or replace an element in a tuple.
t = (1, 2, 3, 4, 5, 6)
t_list = list(t)
t_list[2] = 8   # index 2 లోని element ని 8 తో replace
t = tuple(t_list)
print("After replace:", t)


#4. Find dissimilar elements in two tuples.
tuple1 = (3, 4, 5, 6)
tuple2 = (5, 7, 4, 10)

dissimilar = tuple(set(tuple1) ^ set(tuple2))
print("Dissimilar elements =", dissimilar)


#5. Addition of tuples (pair‑wise).
tuple1 = (10, 4, 5)
tuple2 = (2, 5, 18)

new_tuple = tuple(a + b for a, b in zip(tuple1, tuple2))
print("New tuple =", new_tuple)


#6. Remove duplicates from a tuple.
t = (1, 2, 2, 3, 4, 4, 5)
t_unique = tuple(set(t))
print("Tuple without duplicates:", t_unique)


#7. Sort employee data by salary.
data = [
    (1234, 'Abishek', 32, 35000),
    (4532, 'Barathi', 27, 29000),
    (3455, 'Charan', 31, 37000),
    (9863, 'Devi', 42, 52000),
    (4852, 'Eswar', 37, 56000),
    (6481, 'Fathima', 40, 65000),
    (2793, 'Ganesh', 28, 45000)
]

sorted_data = sorted(data, key=lambda x: x[3])  # salary is at index 3
print("Sorted by salary:")
for emp in sorted_data:
    print(emp)


#8. Count students having "Computers" subject.
students = [
    ("John", ["Computers", "Physics", "Maths"]),
    ("Wasim", ["Maths", "Computers", "Statistics"]),
    ("Naresh", ["Computers", "Accounting", "Economics"]),
    ("SaiTeja", ["English", "Accounting", "Economics", "Law"]),
    ("Sravani", ["Sociology", "Economics", "Law", "Stats", "Music"])
]

count = 0
for name, subjects in students:
    if "Computers" in subjects:
        count += 1

print("Number of students having Computers subject:", count)


#Exercise: Print all friends and their emails who's last name is 'barner'.
contacts = [('John', 'john.deer@gmail.com'),
('Alex', 'alex.barner@yahoo.com'),
('Brad', 'brad.cooper@hotmail.com'),
('Cindy', 'cindy.barner@hotmail.com'),
('Matt', 'matt.damon@gmail.com'),
('George', 'george.cloony@yahoo.com'),('Mec', 'mc.barner@hotmail.com')]

contacts2 = []
for name, email in contacts:
    if 'barner' in email:
        contacts2.append((name, email))
        
contacts2.sort()
print(contacts2)


#Program: Print the details of youngest employee among the employees.
employees = [
(1239, 'John', 23000, 25),
(1235, 'Samantha', 13000, 21),
(1238, 'Amanda', 45000, 30),
(1237, 'Alex', 57000, 31),
(1236, 'Vicky', 40000, 24)
]

print ('Min age:', min(employees, key = lambda x : x[3]))


#Program: Print the details of employee with maximum salary.  
employees = [
(1239, 'John', 23000, 25),
(1235, 'Samantha', 13000, 21),
(1238, 'Amanda', 45000, 30),
(1237, 'Alex', 57000, 31),
(1236, 'Vicky', 40000, 24)
]

print('Max sal:', max(employees, key=lambda x:x[2]))


#Program: Sorting list of employees based on their salaries.
employees = [
(1239, 'John', 23000, 25),
(1235, 'Samantha', 13000, 21),
(1238, 'Amanda', 45000, 30),
(1237, 'Alex', 57000, 31),
(1236, 'Vicky', 40000, 24)
]

sorted_records = sorted(employees, key=lambda x:x[2], reverse=True)
for rec in sorted_records:
    print(rec)






