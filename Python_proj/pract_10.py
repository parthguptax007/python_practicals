#Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the 
#values are cubes of the keys. 




def cube_dictionary():
    cubes = {}

    for i in range(1, 6):
        cubes[i] = i ** 3

    print(cubes)


cube_dictionary()
