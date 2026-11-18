#Write a program to accept a number ‘n’ and  
#   a. Check if ’n’ is prime 
#   b. Generate all prime numbers till ‘n’  
#   c. Generate first ‘n’ prime numbers  
#This program may be done using functions.


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


n = int(input("Enter a number: "))

# a. Check whether n is prime
if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")


# b. Generate all prime numbers till n
print("Prime numbers till", n, ":")

for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")

print()


# c. Generate first n prime numbers
print("First", n, "prime numbers:")

count = 0
num = 2

while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1

    num += 1
