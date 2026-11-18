#Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). Write a program to perform following 
#operations: 
#a. Print half the values of the tuple in one line and the other half in the next line. 
#b. Print another tuple whose values are even numbers in the given tuple. 
#c. Concatenate a tuple t2=(11,13,15) with t1. 
#d. Return maximum and minimum value from this tuple



t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# (a) Print tuple in two halves
mid = len(t1) // 2
print("First half:", t1[:mid])
print("Second half:", t1[mid:])

# (b) Create a tuple of even numbers
even = ()
for i in t1:
    if i % 2 == 0:
        even = even + (i,)
print("Even numbers:", even)

# (c) Concatenate t2 with t1
t2 = (11, 13, 15)
t3 = t1 + t2
print("Concatenated tuple:", t3)

# (d) Find maximum and minimum
print("Maximum value:", max(t1))
print("Minimum value:", min(t1))