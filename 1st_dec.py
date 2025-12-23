
#array
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# to print the given values into a list
print(numbers)
#to find the biggest element in the list
biggest = numbers[0]  # assume first number is biggest
for num in numbers:
    if num > biggest:
        biggest = num

print("The biggest number is:", biggest)



# *
# * *
# * * *
# * * * *
# * * * * * 

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end= " ")
    print()


# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end= " ")
    print()


# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end = " ")
    print()   


print("Your age is", int(input("Enter age: ")))

n = int(input())
s = 0
for i in range(1,n//2+1):
    if n % i == 0:
        s+= i
    #print(s)
if s == n:
    print("perfect number")
else:
        print("not  a perfect number")    

n = int(input())
for i in range(2,int(n**0.5)+1):
    if n %i == 0:
        print("not prime")
        break
else:
    print("prime")


num = int(input())
length = len(str(num))
_sum = 0
for i in str(num):
    _sum += int(i)**length
if _sum == num:
        print("armstrong number")
else:
        print("not an armstrong number")





