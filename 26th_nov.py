#102
#1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5
for i in range(1,6):
    for j in range(6-i):
        print(i ,end = " ")
    print()


#103
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3  
# 2 2  
# 1 

for i in range(5,0,-1):
    for j in range(i):
        print(i, end = " ")
    print()    



#104
# 5 4 3 2 1  
# 5 4 3 2 
# 5 4 3 
# 5 4  
# 5 

for i in range(0 ,6):
    for j in range(5,i ,-1):
        print(j , end = " ")
    print()   



#105

# 5  
# 5 4  
# 5 4 3  
# 5 4 3 2 
# 5 4 3 2 1

for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j , end = " ")
    print()


#106

# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3  
#       4 4  
#         5 

#perfect number
num = int(input(" enter a number: "))
s = 0
for i in range(1,num):
    if num % i == 0:
        s += i
if s == num:
        print("it is a  perfect number")
else:
        print("not a perfect number")



# #arnstrong number.
num =int(input("enter a number: "))
length = len(str(num))
_sum = 0
for i in str(num):
    _sum += int(i)**length
if _sum == num:
    print("armstrong number")
else:
    print("not an arnstrong number")

    

# #check fibnocci
num = int(input("enter a number: "))
a, b = 0, 1
while a < num:
    a, b = b, a+b
if a == num:
    print("it is fibnocci")
else:
    print("it is not a fibnocci number")   



# fibnocci series.
n = int(input("Enter how many terms: "))
m = int(input("enter a number: "))
a, b = 0, 1

for i in range(m):
    while a <= m:
            print(a, end=" ")
        
            a, b = b, a + b   



#prime number.
n = int(input("enter a number: "))
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        print("it is not a prime")
else:
        print("it is a prime")


#check letter in word
for i in "apple":
    if i == "p":
        continue
    print(i)




 
    



