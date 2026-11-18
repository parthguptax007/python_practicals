#Write a program to read a file and 
#a.  Print the total number of characters, words and lines in the file. 
#b.  Calculate the frequency of each character in the file. Use a variable of dictionary type 
#to maintain the count. 
#c.  Print the words in reverse order. 
#d.  Copy even lines of the file to a file named ‘File1’ and odd lines to another file named 
#‘File2’. 





filename = input("Enter file name: ")

# Read the file
with open(filename, "r") as f:
    data = f.read()

# a. Count characters, words and lines
characters = len(data)
words = data.split()
lines = data.splitlines()

print("Total characters:", characters)
print("Total words:", len(words))
print("Total lines:", len(lines))


# b. Frequency of each character
freq = {}

for ch in data:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print("Character frequency:")

for ch in freq:
    print(repr(ch), ":", freq[ch])


# c. Print words in reverse order
print("Words in reverse order:")

for word in reversed(words):
    print(word, end=" ")

print()


# d. Copy even lines to File1 and odd lines to File2
with open("File1", "w") as f1:
    with open("File2", "w") as f2:
        for i in range(len(lines)):
            if (i + 1) % 2 == 0:
                f1.write(lines[i] + "\n")
            else:
                f2.write(lines[i] + "\n")

print("\nEven lines copied to File1")
print("Odd lines copied to File2")
