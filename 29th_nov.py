#2
x = 5 + 2.5
print(x)        # 7.5
print(type(x))  # <class 'float'>


#3
print("Your age is", int(input("Enter age: ")))


#4
a = 7
a % 3
x = 12
(x >= 10) and (x <= 20)


#5
temperature = int(input())
if temperature > 100:
    print("Boiling")
else:
    print("Not boiling")


#6
n = int(input("Enter number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


#7
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


#8
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if (a+b > c) and (a+c > b) and (b+c > a):
    print("Valid triangle")
else:
    print("Invalid triangle")


#9
ch = input("Enter a lowercase letter: ")
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


#10
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print("Result:", a+b)
elif op == "-":
    print("Result:", a-b)
elif op == "*":
    print("Result:", a*b)
elif op == "/":
    print("Result:", a/b)
else:
    print("Invalid operator")


#11
m1 = int(input("Enter marks1: "))
m2 = int(input("Enter marks2: "))
m3 = int(input("Enter marks3: "))
avg = (m1+m2+m3)/3

if m1>=40 and m2>=40 and m3>=40 and avg>=50:
    print("Pass")
else:
    print("Fail")
print("Average marks:", avg)


#12
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x > y and x > z:
    print("Largest is x")
elif y > x and y > z:
    print("Largest is y")
else:
    print("Largest is z")


#13
day = int(input("Enter day number (1-7): "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day number")


#14
a1 = int(input("Enter angle1: "))
a2 = int(input("Enter angle2: "))
a3 = int(input("Enter angle3: "))

if a1+a2+a3 != 180:
    print("Not a triangle")
elif a1==90 or a2==90 or a3==90:
    print("Right-angled triangle")
elif a1<90 and a2<90 and a3<90:
    print("Acute triangle")
else:
    print("Obtuse triangle")


#15
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.20
else:
    tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30

print("Tax to be paid:", tax)

# Enter annual income: 750000
# Tax to be paid: 62500.0


#16
n = int(input("Enter n: "))
i = 1
s = 0
while i <= n:
    s = s + i
    i = i + 1
print("Sum =", s)

# Enter n: 5
#  Sum = 15



#17
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# Enter number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50


#18
n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Enter n: 5
# *
# * *
# * * *
# * * * *
# * * * * *


#19
n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Enter n: 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


#20
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Enter n: 5
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1