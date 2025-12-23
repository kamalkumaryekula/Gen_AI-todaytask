
#Write a program that asks "name" as an input for infinite times.
#  Break the cycle if the user enters anything other than a valid name and
#  print all the entered list of names which are stored till then, if the cycle breaks

l = []
while True:
    name = input("Enter a name: ")
    if name.isalpha():
        l.append(name)
       
    else:
        break
print("list of names", l)


#fibnocci of non-prime.

n = int(input())
a = 0
b = 1
l = []
c= 0
for i in range(0,n):
    l.append(a)
    a,b = b, a+b
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            c+=1
            if c==2:
                print(tuple(l))


