#1.  Based on the given string Input, print its pattern using while loop (growing pattern)
input_str = input("enter a string: ")
rev_str = input_str[::-1]
i = 0
while i < len(rev_str):
    j=0
    while j <=i:
        print(rev_str[j], end = " ")
        j+=1
    print()
    i+=1
   


#. inverse pattern
input_str = input("Enter a string: ")
rev_str = input_str[::-1]

i = len(rev_str) - 1
while i >= 0:
    j = 0
    while j <= i:
        print(rev_str[j], end=" ")
        j += 1
    print()
    i -= 1


# write a programme to change the given string by replacing if it is vowel returns next character if it is consonent returns previous one .
input_str = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in input_str:
    if ch.isalpha():
        # vowel → next letter
        if ch in vowels: 
            new_ch = 'a' if ch.lower() == 'z' else chr(((ord(ch.lower()) - ord('a') + 1) % 26) + ord('a'))
        else:
            # consonant → previous letter
            new_ch = 'z' if ch.lower() == 'a' else chr(((ord(ch.lower()) - ord('a') - 1) % 26) + ord('a'))

        # preserve case
        result += new_ch.upper() if ch.isupper() else new_ch
    else:
        result += ch   # keep non-letters unchanged

print("Transformed string:", result)


