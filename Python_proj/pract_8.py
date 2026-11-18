#Write a program to create a list of the cubes of only the even integers appearing in the input 
#list (may have elements of other types also) using the following: 
#a. 'for' loop 
#b. list comprehension 



lst = eval(input("Enter a list: "))

# a. Using for loop
cubes = []

for i in lst:
    if type(i) == int and i % 2 == 0:
        cubes.append(i ** 3)

print("Using for loop:", cubes)


# b. Using list comprehension
cubes2 = [i ** 3 for i in lst if type(i) == int and i % 2 == 0]

print("Using list comprehension:", cubes2)
