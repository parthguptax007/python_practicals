#Write a program to swap the first n characters of two strings. 



s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

n = int(input("Enter number of characters to swap: "))

if n < 0 or n > len(s1) or n > len(s2):
    print("Invalid value of n")

else:
    temp1 = s1[:n]
    temp2 = s2[:n]

    s1 = temp2 + s1[n:]
    s2 = temp1 + s2[n:]

    print("First string after swapping:", s1)
    print("Second string after swapping:", s2)
