#Write a program to perform the following operations on a string 
#a. Find the frequency of a character in a string. 
#b. Replace a character by another character in a string. 
#c. Remove the first occurrence of a character from a string. 
#d. Remove all occurrences of a character from a string. 


# Accept a string
s = input("Enter a string: ")

# a. Find frequency of a character
ch = input("Enter character to find frequency: ")
print("Frequency =", s.count(ch))


# b. Replace a character with another character
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("After replacement:", s.replace(old, new))


# c. Remove first occurrence of a character
ch = input("Enter character to remove first occurrence: ")
pos = s.find(ch)

if pos != -1:
    s = s[:pos] + s[pos+1:]

print("After removing first occurrence:", s)


# d. Remove all occurrences of a character
ch = input("Enter character to remove all occurrences: ")
s = s.replace(ch, "")

print("After removing all occurrences:", s)
