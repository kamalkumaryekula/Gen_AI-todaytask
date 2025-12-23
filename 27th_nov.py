
#106

# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3  
#       4 4  
#         5 

for i in range(1,6):
    for k in range(i-1):
        print("@",end = " ")
    for j in range(i,6):
        print(i, end = " ")
    print()   



#p-y-t-h-o-n  
name = input("enter a string: ")

for i in name:
    print(i,end = "-")                              

name = input("enter a string")
print("-".join(name))                                                                                



#107
# 1 2 3 4 5  
#   1 2 3 4 
#     1 2 3  
#       1 2 
#         1

for i in range(1,6):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(1,(6+1)-i):
        print(j, end = " ")
    print()  



#109
#          1 
#        1 2 
#      1 2 3 
#    1 2 3 4 
#  1 2 3 4 5  

for i in range(1,6):
    for k in range(5-i):
        print(" ", end = " ") 
    for j in range(1,i+1):
        print(j, end = " ")
    print()




#110  #108
# 1 2 3 4 5 
#   2 3 4 5
#     3 4 5
#       4 5
#         5

for i in range(1,6):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(i,6):
        print(j, end = " ")
    print()  



#101

# 1 2 3 4 5  
# 1 2 3 4 
# 1 2 3
# 1 2  
# 1 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()



#102

# 1 1 1 1 1 
# 2 2 2 2  
# 3 3 3  
# 4 4  
# 5 

for i in range(1,6):
    for j in range(i,6):
        print(i, end = " ")
    print()

    

#palindrome check
num = int(input())
temp = num
rev = 0

while temp > 0:
    d = temp% 10
    rev = rev*10 +d
    temp//=10
print(rev)
if num == rev:
    print("it is palidrome")
else:
    print("it is not a palindrome")


#palindrome string. 
a = input()
if a == a[::-1]:
    print("it is a palindrome")
else:
    print("not a palindrome")



#Program: Print the first three digit multiple of a given number.
num = int(input("enter a number: "))
for i in range(0,1000, num):
    if len(str(i)) ==3:
        print(i)
        break   


#prime

n = int(input("Enter Value: "))
rt = int(n**0.5)

for i in range(2, rt+1):
    if n%i == 0:
        print ("Not Prime")
        break

else:
    print ("Prime")