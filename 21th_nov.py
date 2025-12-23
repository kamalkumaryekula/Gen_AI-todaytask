# find which is the largest number among three number.
a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))
c = int(input("Enter value of c :"))

if (a > b) and (a > c):
    print("a is the largest number")
elif (b > a) and (b > c):
    print("b is the largest number")
elif (c > a) and (c > b):
    print("c is the largest number")
elif (a == b) and (c > a):
    print(" c is the largest among all")
elif (a == b) and (c < a):
    print(" c is the smallest among all")
elif (c == b) and (c < a):
    print(" a is the largest among all")
elif (c == b) and (c > a):
    print(" a is the smallest among all")
elif (a == c) and (c < b):
    print(" b is the largest among all")
elif (a == c) and (c > b):
    print(" b is the smallest among all")
else: 
    print("all are equal")


# calculator
a = int(input())
b = int(input())
operation = input()
if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)
elif operation == "//":
    print(a//b)
elif operation == "%":
    print(a%b)


a = int(input("enter value of a:"))
b = int(input("enter value of b:"))

#a,b = int(input("Enter numbers: ")).split(",")
op_one, op_two = input("enter two operators seperated by comma: ").split(',')
print(eval('%d%s%d' % (a, op_one, b)))
print(eval('%d%s%d' % (a, op_two, b)))   

if op_one == "+":
    print("addition of a and b is:", a+b)
elif op_one == "-":
    print("subtraction a  of and b is:", a-b)
elif op_one == "*":
    print("multiplication a  of and b is:", a*b)
elif op_two == "/":
    print("division of a  and b is:", a/b)
if op_two == "+":
    print("addition of a and b is:", a+b)
elif op_two == "-":
    print("subtraction of a and b is:", a-b)
elif op_two == "*":
    print("multiplication of a and b is:", a*b)
elif op_two == "/":
    print("division of a and b is:", a/b)


#Write a program to read the marks of 3 subjects and display the total, avg, class. 
sub_1 = int(input("Enter marks of sub_1: "))
sub_2 = int(input("Enter marks of sub_2: "))
sub_3 = int(input("Enter marks of sub_3: "))

total = sub_1 + sub_2 + sub_3
average = total/3

if average >= 60:
    classification = "first class"
elif average >= 50:
    classification = "second class"
elif average >= 40:
    classification = "third class"
else:
    classification = "fail"


print(f'total marks:{total}')
print(f'average marks: {round(average ,2)}')
print(f'class of student: {classification}')    



#Write a program to check whether the given number is even or odd. 
num = int(input("Enter the number: "))
if num %2 == 0:
    print("Number is Even")
else:
    print("Number is odd")    



#Write a program to check whether the given number is positive or negative. 
num = int(input("Enter the value: "))
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is odd")
else:
    print("number is neutral")   



#Write a program to find smallest of given two numbers. 
num_1 = int(input("Enter the value num_1: "))
num_2 = int(input("Enter the value num_2: "))

if num_1 < num_2:
    print("num_1 is smallest")
elif num_2 < num_1:
    print("num_2 is smallest")
else:
    print("both are equal")   



#Write a program to check whether the given year is leap year or not. 
year = int(input("enter year:"))
if ((year%100 != 0) and (year%4 == 0)) or (year%400 == 0):
    print("it is a leap year")
else:
    print("not a leap year")  



#Write a program to find biggest of given three numbers. 
num_1 = int(input("Enter num_1: "))
num_2 = int(input("Enter num_2: "))
num_3 = int(input("Enter num_3: "))

if num_1 > num_2  and num_1 > num_3 :
    largest = num_1
elif num_2 >num_1 and num_2 > num_3:
    largest = num_2
else:
    largest = num_3

print("largest of three numbers are: ",largest)   



#Write a program to find the roots of a given quadratic equation and print the nature of roots.
a = int(input("enter value of a: "))
b = int(input("enter value of b: "))
c = int(input("enter value of c: "))

d = ((b**2)-(4*a*c))
if d > 0:
    print("two roots are distinct")
elif d == 0:
    print("one real root repeated")
else:
    print("two complex conjugate roots")

root_1 = (-b + (d**0.5))/(2*a)
root_2 = (-b - (d**0.5))/(2*a)
print(f"roots of quadratic equation are:{round(root_1,2)} and {round(root_2,2)}")  



#Write a program to read positive numbers continuously until negative number is by using ‘if’. 
while True:
    num = int(input("Enter number: "))
    if num < 0:
       print("number is negative")
       break
    else:
        print("number is positive")   


#Write a program to read ten numbers and print their sum by using ‘if’ statement. 
total = 0   
count = 0  

while count < 10:   
    num = int(input("Enter a number: "))
    if num >= 0 or num < 0:   
        total += num
        count += 1

print("The sum of 10 numbers is:", total)   



## Program to classify a triangle based on its sides

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

# First check if it's a valid triangle
if a + b > c and b + c > a and c + a > b:
    # Equilateral
    if a == b and b == c:
        print("Equilateral Triangle")
    # Right-angled
    elif (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
        print("Right-angled Triangle")
    # Isosceles
    elif a == b or b == c or c == a:
        print("Isosceles Triangle")
    # Scalene
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")     
