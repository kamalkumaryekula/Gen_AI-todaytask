# for i in range(1,6):
#     for k in range(i-1):
#         print(" ",end=" ") 
#     for j in range(5,i-1,-1):
#         print(j,end= ' ')
#     print()

# s = "Today is Wednesday"
# print(s.islower())
# s. isupper()


s =\
'''\
MongoDB is a document-oriented, 
operational database built from the ground up 
as an alternative to the relational database for modern applications. 
Unlike relational databases, MongoDB allows developers to store rich 
JSON-like documents that map naturally to the objects they use in their 
code:



# print(s.replace(" ",'-'))
# n_s = ""
# for i in s:
#     if i == " ":
#         n_s +="-"
#     else:
#         n_s += i
# print(n_s)
        
# index wise  each sentence
# for ind, line in enumerate(s.splitlines()):
#     if line:
#         print(str(ind +1) + ". " + line.strip(" ,") + ".")

# for id,line in enumerate(s):
#     print(id,line,end ="")
'''


# #183.   Write a program read a string and print the occurrences of each character. 
# char = input(" enter a name: ")
# print(char.count("a"))


# #184.   Write a program to check whether the given string is palindrome or not. 
# s = input("enter a string: ")
# s1 = s[::-1]
# if s == s1:
#     print("palindrome")
# else:
#     print("not a palindrome")


# # 185.   Write a program to read ‘n’ names and print it in ascending order.  m b 
# n= int(input())
# names = []
# for i in range(n):
#     name = input()
#     names.append(name)
# names.sort(reverse = True)
# names.sort()
# for name in names:
#     print(name)


# #186.   Write a program to read ‘n’ names and print the distinct names. 
# n = int(input())
# names = []

# for i in range(n):
#     name = input()
#     names.append(name)

# distinct_names = set(names)
# for name in distinct_names:
#     print(name)


# #187 Write a program to read ‘n’ names and print the names which are occurred more than once
# n = int(input("emter a number:"))
# names = []
# for i in range(n):
#     name = input()
#     names.append(name)
# count = 0
# for name in names:
#     if name[i] == name[i+1]:
#         count +=1
#     if count > 1:
#         print(name)