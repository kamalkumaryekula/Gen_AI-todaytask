#97

# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10
k = 1
for i in range(1,5):
    for j in range(1,i+1):
        print(k, end = " ")
        k+=1
    print()



#98

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

for i in range(1,6):
    for j in range(1,i+1):
        print(j , end = " ")
    print()


#99

# 1  
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5  5 

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end =" ")
    print()



#100

# 1 
# 1 1  
# 1 2 1 
# 1 2 3 1 
# 1 2 3 4 1 
# 1 2 3 4 5 1 

for i in range(0,6):
    for j in range(1, i+1):
        print(j, end = " ")
    print(1)



#101

# 1 2 3 4 5  
# 1 2 3 4 
# 1 2 3
# 1 2  
# 1 

for i in range(5,0,-1):
    for j in range(1, i+1):
        print(j , end = " ")
    print()



#102

# 1 1 1 1 1 
# 2 2 2 2  
# 3 3 3  
# 4 4  
# 5 

for i in range(1,6):
    for j in range(i,6):
        print(i,end = " ")
    print()



#103

# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3  
# 2 2  
# 1 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end = " ")
    print()



#104

# 5 4 3 2 1  
# 5 4 3 2 
# 5 4 3 
# 5 4  
# 5 

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j , end =" ")
    print()



#105

# 5  
# 5 4  
# 5 4 3  
# 5 4 3 2 
# 5 4 3 2 1 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j ,end = " ")
    print()



#106

# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3  
#       4 4  
#         5 

for i in range(1,6):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(i,6):
        print(i, end = " ")
    print()



#107

# 1 2 3 4 5  
#   1 2 3 4 
#     1 2 3  
#       1 2
#         1

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ", end =" ")
    for j in range(1,i+1):
        print(j, end = " ")
    print()



#108

# 1 2 3 4 5  
#   2 3 4 5 
#     3 4 5  
#       4 5 
#         5 

for i in range(1,6):
    for k in range(i-1):
        print(" ", end =" ")
    for j in range(i,6):
        print(j, end =" ")
    print()



#109

#          1 
#        1 2 
#      1 2 3 
#    1 2 3 4 
#  1 2 3 4 5 

for i in range(1,6):
    for k in range(5-i): 
        print(" ", end =" ")
    for j in range(1,i+1):
        print(j, end =" ")
    print()



#110

#  1 2 3 4 5 
#    2 3 4 5 
#      3 4 5 
#        4 5  
#          5  

for i in range(1,6):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(i,6):
        print(j, end = " ")
    print()



#111

# 5 4 3 2 1 
#   5 4 3 2 
#     5 4 3  
#       5 4
#         5  

for i in range(1,6):
    for k in range(i-1):
        print(" ", end = " ")
    for j in range(5,i-1 ,-1):
        print(j, end = " ")
    print()



#112

#          5 
#        5 4 
#      5 4 3 
#    5 4 3 2 
#  5 4 3 2 1

for i in range(5,0,-1):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(5,i-1,-1):
        print(j, end = " ")
    print()



#113

#          1 
#        2 1 
#      3 2 1 
#    4 3 2 1 
#  5 4 3 2 1 

for i in range(1,6):
    for k in range(5-i):
        print(" ", end = " ")
    for j in range(i,0,-1):
        print(j, end = " ")
    print()



#114

#          5 
#        4 5  
#      3 4 5 
#    2 3 4 5  
#  1 2 3 4 5 

for i in range(5,0,-1):
    for k in range(i-1):
        print(" ", end = " ")
    for j in range(i,6):
        print(j, end = " ")
    print()



#115

#          1 
#        2 2  
#      3 3 3 
#    4 4 4 4 
#  5 5 5 5 5 

for i in range(1,6):
    for k in range(5-i):
        print(" ",end = " ")
    for j in range(i,0,-1):
        print(i,end = " ")
    print()



#116

# 5 
# 4 4 
# 3 3 3 
# 2 2 2 2
# 1 1 1 1 1

for i in range(5,0,-1):
    for k in range(5,i-1,-1):
        print(i,end = " ")
    print()



#117

#          5 
#        4 4  
#      3 3 3 
#    2 2 2 2 
#  1 1 1 1 1 

for i in range(5,0,-1):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(5,i-1,-1):
        print(i, end = " ")
    print()



#118

# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2  
#         1 

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ",end = " ")
    for j in range(1,i+1):
        print(i, end = " ")
    print()



#119

#      1 
#     1  2  
#    1  2  3  
#   1  2  3  4 
#  1  2  3  4  5 

for i in range(1,6):
    for j in range(5-i):
        print(" ",end = " ")
    for k in range(1,i+1):
        print(k,end ="   ")
    print()



#120

# 5 5 5 5 5 
#  4 4 4 4  
#   3 3 3  
#    2 2 
#     1 

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ", end = " ")
    for j in range(i,0,-1):
        print(i, end= "   ")
    print()



#37  Program to check whether a character is uppercase or lowercase without string methods.
#39 icluding digit and if elif else ladder

ch = input("enter a character: ")
ascii_val = ord(ch)
if len(ch) > 1:
    print("enter only single character")
else:
    if 48<= ascii_val <= 57:
        print("it is a digit")
    elif 65 <= ascii_val <= 90:
        print("it is an uppercase letter")
    elif 97 <= ascii_val <= 122:
        print("it is an lowercase letter")
    else:
        print("special character")



# 1 6 11 16 21
# 2 7 12 17 22
# 3 8 13 18 23
# 4 9 14 19 24
# 5 10 15 20 25
for i in range(1,6):
    n= i
    for j in range(1,6):
        print(n,end = " ")
        n+=5
    print()


#40
# Program to find number of notes using match-case

amount = int(input("Enter the amount: "))

denominations = [500, 100, 20, 10, 5, 2, 1]

for note in denominations:
    match note:
        case 500:
            count = amount // 500
            amount = amount % 500
            print("500 notes:", count)
        case 100:
            count = amount // 100
            amount = amount % 100
            print("100 notes:", count)
        case 20:
            count = amount // 20
            amount = amount % 20
            print("20 notes:", count)
        case 10:
            count = amount // 10
            amount = amount % 10
            print("10 notes:", count)
        case 5:
            count = amount // 5
            amount = amount % 5
            print("5 notes:", count)
        case 2:
            count = amount // 2
            amount = amount % 2
            print("2 notes:", count)
        case 1:
            count = amount // 1
            amount = amount % 1
            print("1 notes:", count)

