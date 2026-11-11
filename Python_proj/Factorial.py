# Make a function that takes a number N as input and returns the value of factorial of N.
# Use this function to print the number of ways a set of m red and n blue balls can be
# arranged.
# something something idk what is happening but its better
while True:
    try:
        def calc_ways(N):
            if N == 0:
                return 1
            else:
                fact = 1
                for i in range(1,N+1):
                    fact *= i
                return fact
        m = int(input("Enter the Number of red balls : "))
        n = int(input("Enter the Number of blue balls : "))
        # number of ways calculation step by step 
        x = calc_ways(m)
        y = calc_ways(n)
        z = m+n
        j = calc_ways(z)
        k = x*y
        ways = j/k
        print(ways)
    except ValueError:
        print("Invalid value taken by the user !!!!!!")
    stop = False
    while True:
        q = input("Enter Your Choice <y/n> if you want to continue the operation.(Enter <y> for yes and Enter <n> for no) : ")
        if q == "y":
            break
        elif q == "n":
            stop = True
            break
        else:
            print("Invalid Choice taken by the user choose y and n only !!!!!!!!!")
    if stop == True:
        break 
