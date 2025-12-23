# #187
# n = int(input("Enter a number: "))
# names = []

# for i in range(n):
#     name = input()
#     names.append(name)

# # Count occurrences
# count_dict = {}

# for name in names:
#     if name in count_dict:
#         count_dict[name] += 1
#     else:
#         count_dict[name] = 1




# # Print names that occurred more than once
# print("Names that occurred more than once:")
# for name, count in count_dict.items():
#     if count > 1:
#         print(name)



#188.   Write a program to read a string, a substring which is to be replaced and a substring 
#which is to be placed and print the modified string.

s = input("Enter the main string: ")
old = input("Enter the substring to be replaced: ")
new = input("Enter the new substring: ")

modified = s.replace(old, new)

print("Modified string:", modified)




#189 Write a program to read two strings and find both are same or not. 
s1 = input("enter string_1:")
s2 = input("enter string_2:")
if s1 == s2:
    print("same")
else:
    print("not same")




#190  Write a program to read a line of text and find the number of blank spaces. 

s = "kamal is a good student and a good son"
print(s.count(" "))




#191 Write a program to read a line of text and find the number of words.

s = "kamal is a good student and a good son"
count = 0
for word in s:

    count += 1
print(count) 





# # Read numbers from a range and return maximum of it.
# n = int(input())
# numbers = []
# for i in range(n):
#     number = int(input())
#     numbers.append(number)
# print(max(numbers))




# # Take n numbers in a list by reading n user input.
# n = int(input("Enter a limit value: "))
# _list = []
# for i in range(n+1):
#     _list.append(i)
# print(f'list of {n} numbers is {_list}')




# _list = [1,2,3,4,5,6,7,8,9]
# #_list.append(122)
# #_list.append(122)
# _list.count(122)
# _list.insert(0,123)        #0 is index and 123 is value
# _list.pop()
# _list.pop(0)    #here  0 is index
# _list.remove(1) # 1 is removed from the list , not index
# _list.reverse()   # we have reverse() it changes the original list, reversed() it takes a copy
# _list.sort() #it changes the original data
# sorted(_list)  #it returns sorted one,but it does change the original
# _list.copy()
# deepcopy(_list) # for thos we need to import deepcopy from copy
# _list.index(2)



# list_of_numbers = [0, 2, 3, 4, 5, 6, 7, [8, 9, [12, 34, 45, [12, 54, [100, 101]]]],10,11,12,12,91]

# #print(list_of_numbers[7][2][3][2][1])
# #list_of_numbers.remove(54)
# #print(list_of_numbers[7][2][3].pop(1))
# #print(list_of_numbers)
# #print(list_of_numbers)
# list_of_numbers[7][2][3].insert(1,53)
# print(list_of_numbers) 



# n = int(input())
# m = int(input())
# even_list = []
# odd_list = []

# for i in range(n, m+1):
#     if i%3 ==0:
#         if i%2 ==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
# print(even_list,odd_list)



n = 2
m = int(input("Enter m value: "))

for i in range(n, int(m**0.5)):
    if m % i == 0:
        print(f'{i} is not prime')
    else:
        print(f'{i} is prime')
    




