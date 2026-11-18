#Write a program that accepts a character and performs the following: 
#a. print whether the character is a letter or numeric digit or a special character. 
#b. if the character is a letter, print whether the letter is uppercase or lowercase 
#c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is 
#NINE)


ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character")

elif ch >= 'A' and ch <= 'Z':
    print("The character is a letter")
    print("The letter is uppercase")

elif ch >= 'a' and ch <= 'z':
    print("The character is a letter")
    print("The letter is lowercase")

elif ch >= '0' and ch <= '9':
    print("The character is a numeric digit")

    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
              "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    print("Digit in words:", digits[int(ch)])

else:
    print("The character is a special character")
