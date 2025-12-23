
'''#anagram or not
s1 = input("enter string_1:")
s2 = input("enter string_2:")
s11 = sorted(s1)
s22 = sorted(s2)
if s11 == s22:
    print("anagram")
else:
    print("not anagram")



#replacing a substring in a given string.

s = input("Enter the main string: ")
old = input("Enter the substring to be replaced: ")
new = input("Enter the new substring: ")

modified = s.replace(old, new)

print("Modified string:", modified)     


#190.   Write a program to read a line of text and find the number of blank spaces. 
s = "kamal is an unemployee"
count = 0
for i in s:
    if i == " ":
        count+=1
print(count)    



#191.   Write a program to read a line of text and find the number of words. 
s = 'kamal  is   an unemployee'
words = s.split(" ")
print(f'No of words in agiven string: {len(words)}')



#192.   Write a program to read a line of text and find the number of words when the words are separated by more than one space. 
s = 'kamal    is   an   unemployee'   # multiple spaces included
words = s.split()   # split() without arguments handles multiple spaces
count = len(words)

print(f'No of words in a text: {count}')



#193.   Write a program to read a line of text and find the words which are occurred more than once.
from collections import Counter

s = 'kamal is an unemployee kamal is is'
words = s.split()
counter = Counter(words)

print("Repeated words in the text:")
for word, count in counter.items():
    if count > 1:
        print(f"{word} -> {count} times")   



#194.   Write a program to read a line of text and delete the characters which are occurred more than once.
s = input("Enter text: ")
result = ""
for char in s:
    if s.count(char)==1:
        result +=char

print(s,result)

#195.   Write a program to read a line of text and convert all the lowercase into uppercase and vice versa.
s = input("Enter text: ")
s1 = s.upper()
print(s,s1)     '''



#196.   Write a program to read a line of text and change the each word into upper and lowercase alternatively.
s = input("Enter text: ")
for ch in s:
    if ch.isupper():
        print(ch.lower(),end = " ")
    else:
        print(ch.upper(),end = " ")
