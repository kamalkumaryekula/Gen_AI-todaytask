## 1.a

#         #
#       @ @
#     # # #
#   @ @ @ @
# # # # # #


for i in range(1,6):
    for k in range(5-i):
        print(" ",end = " ")
    for j in range(1,i+1):
        if i%2 !=0:
            print("#",end = " ")
        else:
            print("@",end = " ")
    print()


## 1.b

# 1                 1 
# 2 2             1 2
# 3 3 3         1 2 3
# 4 4 4 4     1 2 3 4
# 5 5 5 5 5 1 2 3 4 5

for i in range(1,5+1):
    for j in range(1, i+1):
        print(i, end = " ")
    for k in range(5-i):
        print(" ", end = " ")
    for l in range(5-i):
        print(" ", end = " ")
    for m in range(1, i+1):
        print(m, end = " ")
    print()



## 5

# a
# B B
# c c c
# D D D D
# e e e e e

i = 1 
while i<=5:
    if i%2 != 0:
        print((chr(96+i) +" ")*i)
    else:
        print((chr(64+i) +" ")*i)
    i=i+1




## 2

def prime_factors(n):
    """Return the list of prime factors of n (with multiplicity)."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_ruth_aaron(n):
    """Check if n is a Ruth_Aaron number."""
    sum_n = sum(set(prime_factors(n)))       # sum of distinct prime factors of n
    sum_next = sum(set(prime_factors(n+1)))  # sum of distinct prime factors of n+1
    return sum_n == sum_next

# Example usage:
num = int(input("Enter a number: "))
if is_ruth_aaron(num):
    print(f"{num} is a Ruth_Aaron number.")
else:
    print(f"{num} is NOT a Ruth_Aaron number.")



## 3



str_nums = ['1', '2', '32', '45.5', '6565', '12.66']
converted_nums = []
for s in str_nums:
    num = float(s)
    rounded = round(num)
    converted_nums.append(rounded) 

print("Converted list:", converted_nums)




## 6.

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    """Return a list of prime numbers in the given range."""
    return [n for n in range(start, end+1) if is_prime(n)]

def print_triangle(primes, rows):
    """Print primes in right-angled triangle format, fill with '#' if insufficient."""
    index = 0
    for row in range(1, rows+1):
        for col in range(row):
            if index < len(primes):
                print(primes[index], end=" ")
                index += 1
            else:
                print("#", end=" ")
        print()

# Example usage:
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
rows = int(input("Enter number of rows: "))

prime_list = primes_in_range(start, end)
print("Prime numbers in triangle format (filled with # if insufficient):")
print_triangle(prime_list, rows)



## 1.c

# A                 a
# B B             b b
# C C C         c c c
# D D D D     d d d d
# E E E E E e e e e e


rows = 5
for i in range(1, rows+1):
    
    for j in range(i):
        print(chr(64+i), end=" ")
    for m in range(rows-i):
        print(" ",end = " ")
    for k in range(rows - i):
        print(" ", end=" ")
    
    for l in range(i):
        print(chr(96+i), end=" ")
    
    print()
