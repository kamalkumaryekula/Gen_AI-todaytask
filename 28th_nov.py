
#111

# 5 4 3 2 1 
#   5 4 3 2 
#     5 4 3  
#       5 4  
#         5  

for i in range(1,6):
    for k in range(i-1):
        print(" ",end = " ")
    for j in range(5,i-1,-1):
        print(j, end = " ")
    print()  



#112

#          5 
#        5 4 
#      5 4 3 
#    5 4 3 2 
#  5 4 3 2 1 

for i in range(1,6):
    for k in range(5-i):
        print(" ",end = " ")
    for j in range(5,5-i,-1):
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
        print(" ",end = " ")
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
        print(" ",end = " ")
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
    for j in range(i):
        print(i, end = " ")
    print()  



#116

#  5 
#  4 4 
#  3 3 3 
#  2 2 2 2 
#  1 1 1 1 1 

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i, end = " ")
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
    for j in range(5-i+1):
        print(i,end = " ")
    print()



#118

# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2  
#         1

for i in range(5,0,-1):
    for k in range(5-i):
        print(" ", end = " ")
    for j in range(i):
        print(i , end = " ")
    print()



#119

#        1 
#      1  2  
#     1  2  3  
#   1  2  3  4 
#  1  2  3  4  5

for  i in range(1,6):
    for k in range(5-i):
        print(' ' , end = " ")
    for j in range(1,i+1):
        print(j,end = "   ")
    print()



#120

# 5  5  5  5  5 
#  4  4  4  4  
#    3  3  3   
#     2  2 
#       1 

for  i in range(5,0,-1):
    for k in range(5-i):
        print(' ' , end = " ")
    for j in range(1,i+1):
        print(i,end = "   ")
    print()

'''#121

#          1 
#        2 3 2 
#      3 4 5 4 3 
#    4 5 6 7 6 5 4 
#  5 6 7 8 9 8 7 6 5 


def number_pyramid(n):
    for i in range(1, n + 1):
        # left padding for centering (tuned for space-separated numbers)
        pad = "  " * (n - i)  # two spaces per pad for better alignment
        asc = list(range(i, 2 * i))           # i to (2i-1)
        desc = list(range(2 * i - 2, i - 1, -1))
        row = asc + desc
        print(pad + " ".join(map(str, row)))

number_pyramid(5)           




#122

#  5  5  5  5  5  
#   4  4  4  4  
#     3  3  3 
#      2  2 
#        1  
#      2  2 
#     3  3  3 
#    4  4  4  4 
#  5  5  5  5  5 

def repeat_diamond(n):
    def row(k, pad):
        print(" " * pad + ("  ".join([str(k)] * k)))
    # upper (including center)
    for k in range(n, 0, -1):
        pad = (n - k) * 2  # tune padding to your spacing style
        row(k, pad)
    # lower
    for k in range(2, n + 1):
        pad = (n - k) * 2
        row(k, pad)

repeat_diamond(5)    '''
