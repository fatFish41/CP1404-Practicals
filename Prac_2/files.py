"""
CP1404/CP5632 - Practical - Suggested Solution
Quick file opening/writing/reading exercises
"""

#1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file = out_file.write(name))  # or out_file.write(name)
out_file.close()

#2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)

#3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)