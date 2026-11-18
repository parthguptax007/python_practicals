#Write a function that accepts two strings and returns the indices of all the occurrences of the 
#econd string in the first string as a list. If the second string is not present in the first string 
#then it should return -1



def find_occurrences(s1, s2):
    indices = []
    start = 0

    while True:
        pos = s1.find(s2, start)

        if pos == -1:
            break

        indices.append(pos)
        start = pos + 1

    if len(indices) == 0:
        return -1

    return indices


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = find_occurrences(s1, s2)

print("Result:", result)
