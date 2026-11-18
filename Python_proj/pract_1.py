#Write a program to find the roots of a quadratic equation.


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c    

if d > 0:
    r1 = (-b + d**0.5) / (2*a)
    r2 = (-b - d**0.5) / (2*a)
    print("Roots are real and distinct")
    print("Root 1 =", r1)
    print("Root 2 =", r2)

elif d == 0:
    r = -b / (2*a)
    print("Roots are real and equal")
    print("Root =", r)

else:
    print("Roots are imaginary")
